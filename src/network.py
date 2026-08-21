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
Neural network architecture design and model instantiation.

This module provides a unified interface for creating and configuring
neural network models, supporting both custom PyTorch architectures and
pre-trained models from HuggingFace. It handles model initialization,
architecture composition, and configuration management.

Key responsibilities:
- Custom neural network architecture implementation
- HuggingFace model integration and fine-tuning setup
- Model factory pattern for configuration-based instantiation
- Architecture search and neural architecture design
- Model compression and optimization techniques
- Transfer learning and domain adaptation strategies

Core components:
- ModelFactory: Configuration-driven model instantiation
- load_pretrained_model(): HuggingFace model loading with custom heads
- CustomVisionModel: Vision-specific architectures (CNN, ViT)
- CustomTextModel: NLP architectures (Transformer, RNN)
- MultiModalModel: Cross-modal architectures for vision-language tasks
- Layer modules: Attention, convolution, normalization components

Integration points:
- HuggingFace transformers for pre-trained models
- timm library for vision model architectures
- torchvision.models for standard computer vision models
- Custom CUDA kernels for optimized operations

Agent ownership:
- ml-engineer: custom architectures and HuggingFace model selection
"""
