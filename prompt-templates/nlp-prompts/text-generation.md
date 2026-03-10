<!-- Copyright 2025 jxtngx | Apache 2.0 License | https://github.com/jxtngx/claude-code-pytorch -->

# Text Generation

I need to implement a text generation system using GPT-2, T5, or LLaMA variants with a context window of at least 2048 tokens. The model should achieve perplexity below 20 and support multiple decoding strategies (greedy, beam search, nucleus sampling). Please implement controllable generation with repetition penalties, efficient KV-cache, streaming output, content safety filters, and a parameter playground UI for experimentation. Include comprehensive metrics for generation quality and diversity.

## Requirements

- Model: GPT-2, T5, or LLaMA variants
- Context window: 2048 tokens minimum
- Decoding: Support multiple strategies
- Safety: Content filtering required

## Success Criteria

- Perplexity <20 on validation
- Controllable generation parameters
- Efficient KV-cache implementation
- Multiple decoding strategies

## Deliverables

- Generation model with streaming
- Parameter playground UI
- Quality metrics dashboard
- Prompt engineering guide
