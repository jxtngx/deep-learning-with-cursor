<!-- Copyright 2025 jxtngx | Apache 2.0 License | https://github.com/jxtngx/claude-code-pytorch -->

# Image Classification

I need to build an image classification system using PyTorch and HuggingFace. The system should leverage pre-trained Vision Transformers or ResNet models to classify images from either ImageNet-1K or CIFAR-10. I have access to GPUs but need to keep training under 8 hours. The model must achieve over 90% accuracy while maintaining fast inference speeds below 50ms per image. Please help me set up the complete pipeline including data loading, model selection, training loop, and API deployment.

## Requirements

- Dataset: ImageNet-1K or CIFAR-10
- Model family: Vision Transformers or ResNet variants
- Training budget: 8 GPU hours maximum
- Inference latency: <50ms per image

## Success Criteria

- Achieve >90% top-1 accuracy on validation set
- Model size under 100MB
- Support mixed precision training
- Implement data augmentation pipeline

## Deliverables

- Trained model with checkpoints
- Evaluation metrics dashboard
- Inference API endpoint
- Documentation of hyperparameters
