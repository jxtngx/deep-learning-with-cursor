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
Training loop orchestration and optimization strategies.

This module implements the core training logic for neural networks,
managing the complete training lifecycle from initialization through
convergence. It handles distributed training, mixed precision, gradient
accumulation, and integrates with experiment tracking systems.

Key responsibilities:
- Training loop execution with configurable strategies
- Distributed training coordination (DDP, FSDP, DeepSpeed)
- Optimization algorithm selection and scheduling
- Loss computation and backward propagation
- Gradient clipping and accumulation strategies
- Checkpointing and model state management
- Early stopping and convergence detection

Core components:
- Trainer: Main training orchestrator class
- TrainingConfig: Configuration dataclass for training parameters
- DistributedTrainer: Multi-GPU training coordinator
- OptimizerFactory: Creates optimizers from configuration
- SchedulerFactory: Learning rate scheduler instantiation
- CheckpointManager: Model and training state persistence
- MetricsTracker: Real-time metrics aggregation

Optimization features:
- Mixed precision training (AMP, bfloat16)
- Gradient accumulation for large batch simulation
- Gradient checkpointing for memory efficiency
- Dynamic loss scaling for numerical stability
- Weight decay and regularization strategies
- Warm-up and cosine annealing schedules

Agent ownership:
- ml-engineer: training loops, metrics, and loss functions
"""
