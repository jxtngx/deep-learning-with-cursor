<!-- Copyright 2025 jxtngx | Apache 2.0 License | https://github.com/jxtngx/claude-code-pytorch -->

# Text Classification

I need to build a text classification system using BERT, RoBERTa, or DistilBERT variants. The system should handle sequences up to 512 tokens and achieve F1 score above 0.85 on custom labeled data. Training must complete within 4 hours on a single GPU. Please implement the complete pipeline including efficient tokenization, class weight balancing for imbalanced datasets, attention weight visualization for interpretability, confidence calibration, and a REST API with batch inference capabilities.

## Requirements

- Model: BERT, RoBERTa, or DistilBERT variants
- Maximum sequence length: 512 tokens
- Dataset: Custom labeled data or benchmark dataset
- Training time: <4 hours on single GPU

## Success Criteria

- F1 score >0.85 on validation set
- Efficient tokenization strategy
- Class weight balancing
- Interpretability via attention weights

## Deliverables

- Fine-tuned classifier with saved tokenizer
- Confusion matrix and classification report
- REST API with batch inference
- Error analysis documentation
