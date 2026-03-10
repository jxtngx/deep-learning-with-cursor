<!-- Copyright 2025 jxtngx | Apache 2.0 License | https://github.com/jxtngx/claude-code-pytorch -->

# Language Model Pre-training (PyTorch Native)

Pre-train a transformer-based language model from scratch using native PyTorch. The model should have [6-24] layers, [768-1024] hidden dimensions, and support sequences up to [512-2048] tokens. Training data consists of [your corpus description] totaling [X GB] of text. The model should achieve perplexity below [target value] on validation data within [GPU hours budget]. Implement the complete pre-training pipeline including tokenizer training, data preprocessing, model architecture, distributed training setup, and checkpoint management.

## Requirements

- Architecture: Transformer decoder or encoder-decoder
- Model size: [100M-1B] parameters
- Sequence length: [512-2048] tokens
- Training data: [10GB-1TB] text corpus
- Hardware: [specify GPU type and count]

## Success Criteria

- Achieve target perplexity on validation set
- Efficient tokenizer with [vocab size] tokens
- Gradient accumulation for large batch training
- Checkpoint saving every [N] steps
- Training loss visualization

## Deliverables

- Pre-trained model checkpoints
- Custom tokenizer files
- Training curves and metrics
- Model card documentation
- Inference benchmark results
