<!-- Copyright 2025 jxtngx | Apache 2.0 License | https://github.com/jxtngx/claude-code-pytorch -->

# Prompt Templates

## Overview

This directory contains ready-to-use prompt templates for common machine learning tasks. These templates are designed to work with the specialized agents in this PyTorch ML project, providing structured requests with clear requirements, success criteria, and deliverables.

## How to Use

1. **Browse** the template files to find a task matching your needs
2. **Copy** the task description from the relevant template
3. **Customize** the requirements and success criteria to match your project
4. **Submit** to trigger the appropriate agent workflow

## Template Categories

<table>
<thead>
<tr>
<th>Category</th>
<th>Templates</th>
<th>Description</th>
<th>Key Features</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="vision-prompts/">Vision Prompts</a></td>
<td>3</td>
<td>Computer vision tasks</td>
<td>Image Classification, Object Detection, Semantic Segmentation</td>
</tr>
<tr>
<td><a href="nlp-prompts/">NLP Prompts</a></td>
<td>4</td>
<td>Natural language processing</td>
<td>Text Classification, NER, Text Generation, Question Answering</td>
</tr>
<tr>
<td><a href="multimodal-prompts/">Multimodal Prompts</a></td>
<td>5</td>
<td>Cross-modal understanding</td>
<td>Vision-Language, Image Captioning, VQA, AV-ASR, Document AI</td>
</tr>
<tr>
<td><a href="pretraining-prompts/">Pre-training Prompts</a></td>
<td>3</td>
<td>Pre-training from scratch</td>
<td>Language Models, Vision Models, Foundation Models</td>
</tr>
<tr>
<td><a href="finetuning-prompts/">Fine-tuning Prompts</a></td>
<td>4</td>
<td>Model adaptation strategies</td>
<td>Full Fine-tuning, PEFT, Domain Adaptation, Instruction Tuning</td>
</tr>
<tr>
<td><a href="interface-prompts/">Interface Prompts</a></td>
<td>9</td>
<td>Web interface development</td>
<td>ML Playground, Dashboards, Monitoring, Annotation Studio</td>
</tr>
<tr>
<td><a href="test-prompts/">Test Prompts</a></td>
<td>7</td>
<td>Test-driven development</td>
<td>Data Pipeline, Architecture, Training, API, Performance Tests</td>
</tr>
</tbody>
</table>

## Template Structure

Each template follows a consistent three-section structure:

```markdown
# [Task Name]

[Task description with specific requirements]

## Requirements
- Technical limitations and resource boundaries
- Compatibility and framework requirements

## Success Criteria
- Performance targets and quality indicators
- Measurable goals

## Deliverables
- Expected outputs and artifacts
- Validation methods
```

## Customization Guide

When adapting templates:

1. **Be specific**: Replace placeholder values with actual requirements
2. **Set realistic targets**: Adjust performance metrics to your hardware
3. **Include your data**: Specify your dataset or provide sample data
4. **Define success**: Clear metrics help agents optimize correctly

## Agent Routing

Templates automatically route to appropriate agents:

- **@agent-NetworkArchitect**: For custom model architectures
- **@agent-TestArchitect**: For TDD workflows
- **@agent-DatasetCurator**: For dataset selection
- **@agent-TrainingOrchestrator**: For training pipelines
- **@agent-InterfaceDesigner**: For UI/UX tasks

Agents not explicitly mentioned are selected automatically based on task requirements.

## Best Practices

### DO:
- Start with test prompts for TDD workflow
- Include specific performance targets
- Specify hardware constraints upfront
- Mention preferred libraries/frameworks
- Set clear success criteria

### DON'T:
- Use vague requirements ("make it fast")
- Combine unrelated tasks in one prompt
- Omit hardware or resource constraints
- Skip success criteria

## Examples

### Quick Start: Image Classification
```bash
# 1. Copy prompt from vision-prompts/image-classification.md
# 2. Replace "ImageNet-1K or CIFAR-10" with your dataset
# 3. Adjust "8 GPU hours" to your budget
# 4. Submit to Cursor
```

### Test-First Development
```bash
# 1. Start with a test-prompts/ template
# 2. Let Test Developer write tests first
# 3. Then use vision/nlp/multimodal prompts for implementation
# 4. Ensure all tests pass before deployment
```

## Template Combinations

Common workflows:

1. **Full Pipeline**: Test -> Data -> Model -> Training -> Deployment
2. **Research**: Data exploration -> Model experimentation -> Metrics
3. **Production**: Model optimization -> API -> Interface -> Testing
4. **Iteration**: Metrics analysis -> Model refinement -> A/B testing

## Support

- Review `.cursor/agents/chief-architect.md` for team overview and agent capabilities
- Check `.cursor/agents/` for detailed agent documentation
