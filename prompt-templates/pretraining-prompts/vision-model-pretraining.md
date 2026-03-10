<!-- Copyright 2025 jxtngx | Apache 2.0 License | https://github.com/jxtngx/claude-code-pytorch -->

# Vision Model Pre-training (PyTorch Native)

Implement self-supervised pre-training for vision models using [SimCLR/MoCo/BYOL/MAE] approach in native PyTorch. The model should work with [ResNet/ViT] backbone processing images at [224-384] resolution. Pre-training will use [dataset size] unlabeled images and should achieve [target metric] on linear evaluation within [GPU hours]. Build the complete pipeline including augmentation strategies, contrastive loss implementation, momentum encoders if applicable, and distributed training across multiple GPUs.

## Requirements

- Method: [SimCLR/MoCo/BYOL/MAE]
- Backbone: [ResNet50/ViT-B]
- Image resolution: [224-384] pixels
- Batch size: [256-4096] depending on method
- Training duration: [100-800] epochs

## Success Criteria

- Linear probe accuracy > [target]%
- Efficient negative sampling strategy
- Strong augmentation pipeline
- Multi-GPU synchronization
- Temperature scheduling for contrastive methods

## Deliverables

- Pre-trained encoder weights
- Training dynamics visualization
- Linear evaluation results
- Transfer learning benchmarks
- Augmentation configuration
