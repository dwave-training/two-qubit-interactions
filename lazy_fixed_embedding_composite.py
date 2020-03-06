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

from dwave.system.samplers import DWaveSampler
from dwave.system.composites import LazyFixedEmbeddingComposite

# Set up the QUBO. Start with the equations from the slides:
chainstrength = 4
numruns = 100
Q = {(0, 0): 2, (0, 1): -2, (0, 2): -2, (1, 2): 2}

sampler = LazyFixedEmbeddingComposite(DWaveSampler())
response = sampler.sample_qubo(Q, chain_strength=chainstrength, num_reads=numruns)
print(sampler.properties['embedding'])

for smpl, energy in response.data(['sample', 'energy']):
    print(smpl, energy)
