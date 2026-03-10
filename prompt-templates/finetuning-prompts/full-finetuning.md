<!-- Copyright 2025 jxtngx | Apache 2.0 License | https://github.com/jxtngx/claude-code-pytorch -->

# Full Fine-tuning (PyTorch Native)

I need to implement full fine-tuning of a pre-trained [model type] using native PyTorch. Starting from [checkpoint/weights], the model should be adapted for [task description] with [dataset size] labeled examples. Training should complete within [hours] on [GPU type] while achieving [metric] > [target]. Please build the complete pipeline including model loading, layer freezing strategies, learning rate scheduling with warmup, early stopping, and comprehensive evaluation metrics.

## Requirements

- Base model: [model name and size]
- Dataset: [size] samples with [classes/labels]
- Hardware: [GPU memory] available
- Training time: [hours] maximum
- Batch size: [range based on memory]

## Success Criteria

- Achieve target performance metric
- Gradual unfreezing strategy
- Discriminative learning rates
- Validation-based checkpointing
- Confusion matrix and error analysis

## Deliverables

- Fine-tuned model weights
- Training history plots
- Performance metrics report
- Best checkpoint selection
- Deployment-ready model
