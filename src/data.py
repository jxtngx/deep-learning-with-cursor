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
Data pipeline orchestration for machine learning workflows.

This module manages the complete data pipeline from raw datasets to
optimized PyTorch DataLoaders. It handles dataset discovery, preprocessing,
augmentation, and efficient batch loading for training and inference.

Key responsibilities:
- Dataset loading from HuggingFace Hub and custom sources
- DataLoader creation with optimized sampling and batching strategies
- Transform pipeline composition for data augmentation
- Memory-efficient data loading with prefetching and caching
- Distributed data loading for multi-GPU training
- Dataset versioning and reproducibility management

Core components:
- create_dataloaders(): Factory function for train/val/test DataLoaders
- get_transforms(): Task-specific transformation pipelines
- HFDatasetWrapper: Adapter for HuggingFace datasets to PyTorch format
- Custom dataset classes for specialized data formats
- Collation functions for variable-length sequences

Integration points:
- Interfaces with HuggingFace datasets library for dataset discovery
- Leverages torchvision.transforms for image augmentations
- Integrates with NVIDIA DALI for GPU-accelerated preprocessing
- Supports distributed sampling for DDP training
- Provides reproducible data splits with configurable seeds

Agent ownership:
- data-engineer: datasets, loaders, transforms, quality
"""
