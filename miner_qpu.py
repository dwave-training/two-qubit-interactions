# Copyright 2020 D-Wave Systems, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from minorminer import find_embedding
from dwave.system.samplers import DWaveSampler
from dwave.system.composites import FixedEmbeddingComposite

# Set up the QUBO. Start with the equations:
# x + y - 2xy -1
# 2yz - y - z
# -2zx + z + x - 1
# QUBO: 2x - 2xy + 2yz - 2zx - 2
Q = {(0, 0): 2, (0, 1): -2, (0, 2): -2, (1, 2): 2}

chainstrength = 2
numruns = 1000

dwave_sampler = DWaveSampler()
A = dwave_sampler.edgelist
embedding = find_embedding(Q, A)
print(embedding)

response = FixedEmbeddingComposite(DWaveSampler(), embedding).sample_qubo(Q, chain_strength=chainstrength, num_reads=numruns)

for sample, energy, num, cbf in response.data(['sample', 'energy', 'num_occurrences', 'chain_break_fraction']):
    print(sample, energy, num, cbf)
