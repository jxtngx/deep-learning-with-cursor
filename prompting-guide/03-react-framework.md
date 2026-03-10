# ReAct Framework Integration

## Overview

ReAct (Reasoning + Acting) combines thought processes with concrete actions. In our ML development context, this means agents don't just think about solutions—they actively use tools, fetch data, run experiments, and verify results.

## Human Analogy

ReAct mirrors how a researcher works: think about the problem, consult references, run experiments, observe results, adjust approach. It's like having a conversation with someone who can actually look things up and test hypotheses instead of just theorizing.

## The ReAct Cycle

```mermaid
graph LR
    A[Thought] --> B[Action]
    B --> C[Observation]
    C --> D[Thought]
    D --> E[Action]
    E --> F[Observation]
    F --> G[Solution]

    style A fill:#e8f5e9
    style D fill:#e8f5e9
    style B fill:#fff3e0
    style E fill:#fff3e0
    style C fill:#e1f5fe
    style F fill:#e1f5fe
```

## ReAct Components in ML Development

### Thought
Reasoning about the current state and next steps:
- "I need to check if this dataset exists on HuggingFace"
- "The model might be overfitting, let me verify"
- "This error suggests a shape mismatch"

### Action
Using tools and capabilities:
- Searching documentation
- Running code
- Fetching datasets
- Executing tests
- Profiling performance

### Observation
Processing results from actions:
- "The dataset has 50,000 samples"
- "Test accuracy is 20% lower than training"
- "Memory usage peaks at 15GB"

## ReAct in Practice: Model Selection

```markdown
## Task: Find the best pretrained model for a classification task while minimizing training time

**Thought 1**: I need to identify suitable models on HuggingFace
**Action 1**: Search HuggingFace for models trained on similar data
**Observation 1**: Found 5 models: BERT, RoBERTa, DeBERTa, ELECTRA, ALBERT

**Thought 2**: I should compare their performance metrics
**Action 2**: Fetch benchmark scores for each model
**Observation 2**: DeBERTa shows best accuracy, ELECTRA fastest inference

**Thought 3**: Need to verify compatibility with our constraints
**Action 3**: Check model sizes and requirements
**Observation 3**: DeBERTa-base fits within 8GB memory constraint

**Thought 4**: Should test with our specific data
**Action 4**: Load model and run validation
**Observation 4**: Achieves 92% accuracy on our validation set

**Conclusion**: DeBERTa-base selected based on performance and constraints
```

## ReAct Templates for ML Tasks

### Template 1: Dataset Exploration

```markdown
**Thought**: Need to understand dataset characteristics
**Action**: Load dataset and compute statistics
**Observation**: [size, distribution, missing values]

**Thought**: Check for data quality issues
**Action**: Run validation checks
**Observation**: [findings]

**Thought**: Determine preprocessing needs
**Action**: Test preprocessing pipeline
**Observation**: [results]
```

### Template 2: Model Debugging

```markdown
**Thought**: Model not converging, need to diagnose
**Action**: Check gradient flow
**Observation**: [gradient statistics]

**Thought**: Might be learning rate issue
**Action**: Plot loss curves
**Observation**: [loss behavior]

**Thought**: Test different learning rates
**Action**: Run quick experiments
**Observation**: [convergence patterns]
```

### Template 3: Performance Optimization

```markdown
**Thought**: Training too slow, need profiling
**Action**: Run profiler on training loop
**Observation**: [bottleneck identification]

**Thought**: Data loading seems slow
**Action**: Benchmark dataloader
**Observation**: [loading times]

**Thought**: Try optimization techniques
**Action**: Implement and measure improvements
**Observation**: [performance gains]
```

## Agent-Specific ReAct Patterns

### DatasetCurator Agent
```markdown
**Thought**: User needs image classification data
**Action**: Search HuggingFace datasets
**Observation**: Found 15 relevant datasets

**Thought**: Need to filter by size and quality
**Action**: Check dataset cards and statistics
**Observation**: CIFAR-10, ImageNet, and Food101 meet criteria

**Thought**: Verify compatibility with task
**Action**: Load sample batches
**Observation**: All datasets compatible with standard transforms
```

### NetworkArchitect Agent
```markdown
**Thought**: Designing architecture for sequence modeling
**Action**: Review recent papers and benchmarks
**Observation**: Transformers dominate, but RNNs efficient for long sequences

**Thought**: Need to balance performance and resources
**Action**: Calculate memory requirements for each
**Observation**: Transformer feasible with gradient checkpointing

**Thought**: Implement and validate design
**Action**: Build model and check shapes
**Observation**: Forward pass successful, 45M parameters
```

## Advanced ReAct Patterns

### Multi-Step Investigation

```markdown
## Task: Fix Training Instability

**Thought 1**: Losses becoming NaN, likely numerical issue
**Action 1**: Add logging to track when NaN appears
**Observation 1**: NaN first appears in attention scores

**Thought 2**: Attention scores might be too large
**Action 2**: Check value ranges before softmax
**Observation 2**: Some values exceed 1e10

**Thought 3**: Need gradient clipping or scaling
**Action 3**: Implement gradient clipping at 1.0
**Observation 3**: NaN still occurs

**Thought 4**: Try attention score scaling
**Action 4**: Add temperature scaling to attention
**Observation 4**: Training stable, no NaN

**Thought 5**: Verify fix doesn't hurt performance
**Action 5**: Compare metrics with and without scaling
**Observation 5**: Negligible impact on accuracy
```

### Parallel Actions

```markdown
## Task: Comprehensive Model Evaluation

**Thought**: Need multiple evaluation metrics
**Actions** (parallel):
  - Action A: Calculate accuracy and F1
  - Action B: Generate confusion matrix
  - Action C: Compute inference time
  - Action D: Measure memory usage

**Observations**:
  - Obs A: Accuracy 94.2%, F1 0.941
  - Obs B: Main confusion between similar classes
  - Obs C: 12ms per sample
  - Obs D: Peak memory 4.2GB

**Thought**: Results meet requirements
**Action**: Package results for deployment
```

## ReAct with Tool Usage

### Available Tools in Context

```markdown
**Thought**: Need to find optimal hyperparameters
**Action**: Use Optuna for hyperparameter search
**Tool**: optuna.create_study()
**Observation**: Best params: lr=0.001, batch_size=64

**Thought**: Should verify on different seeds
**Action**: Run training with found parameters
**Tool**: trainer.train(config=best_params)
**Observation**: Consistent results across seeds
```

## Human Parallel

Like a senior researcher working on a problem:
1. Forms hypothesis (Thought)
2. Designs experiment (Action)
3. Analyzes results (Observation)
4. Iterates based on findings

This is more powerful than pure reasoning because it grounds decisions in actual data and results.

## Benefits of ReAct in ML

1. **Grounded Decisions**: Based on actual data, not assumptions
2. **Debugging Power**: Can investigate and test hypotheses
3. **Adaptive Problem-Solving**: Adjusts based on observations
4. **Reproducible Process**: Actions can be repeated

## Navigation

[Previous: Chain of Thought](02-chain-of-thought.md) | [Up: Prompting Guide](README.md) | [Next: Hybrid Techniques](04-hybrid-techniques.md)