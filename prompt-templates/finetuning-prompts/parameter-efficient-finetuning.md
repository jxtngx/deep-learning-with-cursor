# Parameter-Efficient Fine-tuning (HuggingFace + PyTorch)

I need to implement parameter-efficient fine-tuning using [LoRA/QLoRA/Prefix Tuning/Adapters] with HuggingFace PEFT and PyTorch. Starting with [base model name], adapt it for [task] using only [0.1-1%] of parameters. The model should be quantized to [4/8]-bit if using QLoRA. Dataset contains [size] examples in [format]. Training should fit within [GPU memory] GB and achieve [metric] comparable to full fine-tuning. Please set up the complete workflow including PEFT configuration, quantization setup, training with gradient checkpointing, and adapter merging.

## Requirements

- Method: [LoRA/QLoRA/Prefix Tuning/Adapters]
- Base model: [HF model name]
- Trainable parameters: [0.1-1%] of total
- Quantization: [none/4-bit/8-bit]
- Memory budget: [GPU memory] GB

## Success Criteria

- Memory usage < [threshold] GB
- LoRA rank optimization
- Gradient checkpointing enabled
- Adapter merging for deployment
- Performance within [X%] of full fine-tuning

## Deliverables

- PEFT adapter weights
- Merged model option
- Memory usage report
- Performance comparison table
- Inference optimization guide
