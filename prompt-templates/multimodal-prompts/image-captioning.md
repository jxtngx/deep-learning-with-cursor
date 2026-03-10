<!-- Copyright 2025 jxtngx | Apache 2.0 License | https://github.com/jxtngx/claude-code-pytorch -->

# Image Captioning

Build an image captioning system using encoder-decoder or autoregressive architectures trained on COCO Captions. The system should generate captions up to 50 tokens with BLEU-4 score above 0.35, using beam search with width 3-5. Implement diverse caption generation with length normalization, attention visualization, real-time inference, multiple caption sampling options, and a web interface where users can upload images and receive instant captions.

## Requirements

- Architecture: Encoder-decoder or autoregressive
- Dataset: COCO Captions or custom annotations
- Beam search: Width 3-5
- Maximum caption length: 50 tokens

## Success Criteria

- BLEU-4 score >0.35
- Diverse caption generation
- Attention visualization
- Real-time inference capability

## Deliverables

- Caption generation model
- Multiple caption sampling
- Web interface with upload
- Evaluation suite with metrics
