<!-- Copyright 2025 jxtngx | Apache 2.0 License | https://github.com/jxtngx/claude-code-pytorch -->

# Foundation Model Pre-training (HuggingFace + PyTorch)

Pre-train a [model architecture] foundation model using HuggingFace Transformers and PyTorch. Starting from [config/scratch], the model should have [parameter count] parameters and handle [modality: text/vision/multimodal]. Training will use [dataset names or custom data] with HuggingFace datasets library. Target compute budget is [GPU hours] using [hardware specs]. Set up the complete workflow including dataset streaming, model initialization, training with HF Trainer or Accelerate, mixed precision training, and model hub integration.

## Requirements

- Architecture: [GPT/BERT/T5/ViT/CLIP variant]
- Parameters: [100M-10B]
- Dataset: HF datasets or custom format
- Training framework: HF Trainer or Accelerate
- Precision: fp16/bf16/fp32

## Success Criteria

- Streaming large datasets efficiently
- Gradient checkpointing for memory optimization
- WandB/TensorBoard integration
- Model card generation
- Hub upload with proper tags

## Deliverables

- Pre-trained model on HuggingFace Hub
- Training metrics and logs
- Model card with performance details
- Conversion scripts for deployment
- Benchmark comparisons
