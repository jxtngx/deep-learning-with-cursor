# Copyright 2025 jxtngx
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

"""
EC2 instance management for distributed ML compute.

This module handles spinning up and tearing down EC2 instances for
machine learning workloads. It provides a simple interface for provisioning
GPU instances and coordinating distributed training clusters.

Key responsibilities:
- EC2 instance lifecycle management (spinup/teardown)
- GPU instance provisioning for ML workloads
- Distributed training cluster setup
- Spot instance management with fallback strategies
- Basic cost optimization through instance selection

Supported instance types:
- P4/P5: High-performance GPU training (A100/H100)
- G4/G5: Cost-effective training and inference (T4/A10G)
- Standard CPU instances for data preprocessing

Core components:
- spin_up_instance(): Launch EC2 instances with specified configuration
- tear_down_instance(): Terminate instances and cleanup resources
- create_cluster(): Setup multi-node training clusters
- manage_spot_fleet(): Handle spot instance requests and interruptions

Agent ownership:
- ml-engineer: EC2/GPU resource management and optimization
"""
