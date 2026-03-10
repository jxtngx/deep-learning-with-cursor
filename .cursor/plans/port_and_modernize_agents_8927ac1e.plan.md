---
name: Port and Modernize Agents
overview: Port 10 specialized PyTorch ML agents from `.claude/agents/` to `.cursor/agents/`, fire 5 redundant ones, and update the Chief Architect to understand `prompt-templates/` and `prompting-guide/`.
todos:
  - id: hire-fire
    content: Document the hire/fire decision in a comment or changelog (optional, for traceability)
    status: completed
  - id: port-compute
    content: Port ComputeOrchestrator from .claude/agents/compute.md to .cursor/agents/compute-orchestrator.md in Cursor format
    status: completed
  - id: port-expert
    content: Port DomainExpert from .claude/agents/expert.md to .cursor/agents/domain-expert.md in Cursor format
    status: completed
  - id: port-network
    content: Port NetworkArchitect from .claude/agents/network.md to .cursor/agents/network-architect.md in Cursor format
    status: completed
  - id: port-dataloader
    content: Port DataEngineer from .claude/agents/dataloader.md to .cursor/agents/data-engineer.md in Cursor format
    status: completed
  - id: port-datasets
    content: Port DatasetCurator from .claude/agents/datasets.md to .cursor/agents/dataset-curator.md in Cursor format
    status: completed
  - id: port-models
    content: Port ModelArchitect from .claude/agents/models.md to .cursor/agents/model-architect.md in Cursor format
    status: completed
  - id: port-transforms
    content: Port TransformSpecialist from .claude/agents/transforms.md to .cursor/agents/transform-specialist.md in Cursor format
    status: completed
  - id: port-runner
    content: Port RunnerOrchestrator from .claude/agents/runner.md to .cursor/agents/runner-orchestrator.md in Cursor format
    status: completed
  - id: port-metrics
    content: Port MetricsArchitect from .claude/agents/metrics.md to .cursor/agents/metrics-architect.md in Cursor format
    status: completed
  - id: port-trainer
    content: Port TrainingOrchestrator from .claude/agents/trainer.md to .cursor/agents/training-orchestrator.md in Cursor format
    status: completed
  - id: update-test-dev
    content: Merge TestArchitect PyTorch testing expertise into .cursor/agents/test-developer.md
    status: completed
  - id: update-chief-team
    content: "Update chief-architect.md: add 10 new agents to Team table, update architecture mermaid diagram with ML pipeline subgraph"
    status: completed
  - id: update-chief-prompts
    content: "Update chief-architect.md: add Prompt Templates section mapping to prompt-templates/ with INVEST+CRPG overview"
    status: completed
  - id: update-chief-guide
    content: "Update chief-architect.md: add Prompting Guide section mapping to prompting-guide/ progressive complexity model"
    status: completed
  - id: update-chief-delegation
    content: "Update chief-architect.md: update Authority, Delegation, and Sync Flow sections for ML workflows"
    status: completed
isProject: false
---

# Port and Modernize Claude Agents to Cursor

## Phase 1: Chief Architect's Hiring Decision

Consulting with the [Chief Fullstack Architect](.cursor/agents/chief-architect.md), the following hire/fire decisions are based on overlap analysis between the 15 tenured Cursor agents and the 15 Claude agent candidates.

### HIRE -- 10 Agents (unique PyTorch ML expertise)

These Claude agents bring deep specialization that no tenured Cursor agent covers:

- **ComputeOrchestrator** (`compute.md`) -- GPU instance selection (P5, P4, G5, Trn1, Inf2), EFA/NVLink, NCCL, auto-scaling for ML. AWS Engineer lacks GPU-specific ML compute depth.
- **DomainExpert** (`expert.md`) -- Domain-to-ML translation (biology, physics, chemistry, finance, etc.). No Cursor equivalent.
- **NetworkArchitect** (`network.md`) -- Custom neural architectures (transformers, GNNs, attention, NAS). No Cursor equivalent.
- **DataEngineer** (`dataloader.md`) -- PyTorch DataLoader, custom datasets/collate, WebDataset, distributed sampling. No Cursor equivalent.
- **DatasetCurator** (`datasets.md`) -- HuggingFace dataset discovery, licensing, quality assessment. ML Engineer touches this lightly but not with this depth.
- **ModelArchitect** (`models.md`) -- HuggingFace model selection, tokenizer config, quantization. ML Engineer is more general.
- **TransformSpecialist** (`transforms.md`) -- TorchVision, Albumentations, Kornia, audio/text transforms. No Cursor equivalent.
- **RunnerOrchestrator** (`runner.md`) -- End-to-end pipeline orchestration with Hydra, MLflow, W&B, DVC. No Cursor equivalent.
- **MetricsArchitect** (`metrics.md`) -- Domain-specific metrics (mAP, BLEU, FID, BERTScore) via TorchMetrics. No Cursor equivalent.
- **TrainingOrchestrator** (`trainer.md`) -- Training loops, DDP/FSDP, mixed precision, gradient accumulation, curriculum learning. ML Engineer is MLOps-focused; this is training-loop-focused.

### FIRE -- 5 Agents (redundant with tenured team)

- **CloudEngineer** -- Covered by [AWS Engineer](.cursor/agents/aws-engineer.md) (both handle AWS services, APIs, IaC, deployment)
- **Supervisor** -- Covered by [Product Manager](.cursor/agents/product-manager.md) (requirements) + [Scrum Master](.cursor/agents/scrum-master.md) (sprint process)
- **InterfaceDesigner** -- Covered by [Designer](.cursor/agents/designer.md) (diagrams/wireframes) + [Frontend Engineer](.cursor/agents/frontend-engineer.md) (implementation)
- **TestArchitect** -- Covered by [Test Developer](.cursor/agents/test-developer.md), BUT: merge TestArchitect's PyTorch testing expertise (`torch.testing`, `gradcheck`, `make_tensor`, shape validation, numerical stability) into Test Developer
- **LocalStackEmulator** -- Covered by [AWS Engineer](.cursor/agents/aws-engineer.md) (already owns LocalStack config)

---

## Phase 2: Port and Modernize Hired Agents

### Format Conversion (Claude to Cursor style)

Each ported agent needs structural changes. The Claude agents use YAML frontmatter + copyright headers:

```markdown
---
name: TrainingOrchestrator
description: Training loop implementation...
tools: Read, Write, Edit, Bash
---
<!-- Copyright ... -->
You are TrainingOrchestrator, a specialist in...
```

The Cursor agents use a consistent markdown pattern:

```markdown
# [Agent Name]
You are the [Agent Name] for deep-learning-with-claude, reporting to the Chief Fullstack Architect.
## Scope (mermaid diagram)
## Ownership (directory tree)
## Skills (table)
## Responsibilities
## Authority
## Constraints
## Collaboration
```

Reference the Cursor pattern from [ml-engineer.md](.cursor/agents/ml-engineer.md), [test-developer.md](.cursor/agents/test-developer.md), and [aws-engineer.md](.cursor/agents/aws-engineer.md).

### Content Updates for Each Ported Agent

Every hired agent must be updated with:

1. **Header**: Replace YAML frontmatter with `# [Name]` heading and "reporting to the Chief Fullstack Architect" line
2. **Project context**: Replace "claude-code-pytorch" references with "deep-learning-with-claude"
3. **Scope diagram**: Add a mermaid graph showing the agent's scope (matching Cursor style)
4. **Collaboration references**: Update short names to full agent names and add cross-references to tenured Cursor team members where roles intersect:
  - "Trainer" references become "TrainingOrchestrator" and/or "ML Engineer"
  - "Compute" references become "ComputeOrchestrator" and/or "AWS Engineer"  
  - "Manager" references become "Product Manager" and/or "Scrum Master"
  - "Frontend" references become "Designer" and/or "Frontend Engineer"
  - "Expert" remains "DomainExpert"
  - Testing references point to "Test Developer" (since TestArchitect is fired)
5. **Remove**: Copyright headers, tools frontmatter
6. **Add**: Skills table (placeholder paths), Authority section, Constraints section

### Specific File Mapping


| Claude Source                  | Cursor Target                             |
| ------------------------------ | ----------------------------------------- |
| `.claude/agents/compute.md`    | `.cursor/agents/compute-orchestrator.md`  |
| `.claude/agents/expert.md`     | `.cursor/agents/domain-expert.md`         |
| `.claude/agents/network.md`    | `.cursor/agents/network-architect.md`     |
| `.claude/agents/dataloader.md` | `.cursor/agents/data-engineer.md`         |
| `.claude/agents/datasets.md`   | `.cursor/agents/dataset-curator.md`       |
| `.claude/agents/models.md`     | `.cursor/agents/model-architect.md`       |
| `.claude/agents/transforms.md` | `.cursor/agents/transform-specialist.md`  |
| `.claude/agents/runner.md`     | `.cursor/agents/runner-orchestrator.md`   |
| `.claude/agents/metrics.md`    | `.cursor/agents/metrics-architect.md`     |
| `.claude/agents/trainer.md`    | `.cursor/agents/training-orchestrator.md` |


---

## Phase 3: Update Tenured Agent -- Test Developer

Merge TestArchitect's PyTorch ML testing expertise into [test-developer.md](.cursor/agents/test-developer.md):

- Add a **PyTorch ML Testing** section covering: `torch.testing.assert_close()`, `make_tensor()`, `gradcheck()`, numerical stability, shape validation, reproducibility testing, property-based testing for ML
- Add `tests/ml/` to the Ownership tree for ML-specific test files
- Add a PyTorch Testing skill to the Skills table
- Update Scope mermaid diagram to include ML test branch
- Add collaboration notes for the 10 new ML agents (TDD workflow: tests before implementation)

---

## Phase 4: Update Chief Architect

Update [chief-architect.md](.cursor/agents/chief-architect.md) with three major additions:

### 4a. Expanded Team

Add all 10 new agents to the Team table with their ownership areas. Update the architecture mermaid diagram to include an ML/DL pipeline subgraph alongside the existing frontend/backend/infra/integrations subgraphs:

```mermaid
subgraph mlPipeline [ML/DL Pipeline]
    DatasetCurator --> DataEngineer --> TransformSpecialist
    ModelArchitect --> NetworkArchitect
    TrainingOrchestrator --> MetricsArchitect
    RunnerOrchestrator
    ComputeOrchestrator
    DomainExpert
end
```



### 4b. Prompt Templates Mapping

Add a **Prompt Templates** section that maps to `prompt-templates/` and explains the INVEST+CRPG framework:

- Vision Prompts (3 templates): Image classification, object detection, semantic segmentation
- NLP Prompts (4 templates): Text classification, NER, text generation, question answering
- Multimodal Prompts (5 templates): Vision-language, captioning, VQA, AV-ASR, document AI
- Pretraining Prompts (3 templates): Language model, vision model, foundation model
- Finetuning Prompts (4 templates): Full, PEFT, domain adaptation, instruction tuning
- Interface Prompts (9 templates): Playground, dashboards, monitoring, annotation
- Test Prompts (7 templates): Data pipeline, architecture, training, API, performance, integration, regression

Include the agent routing pattern: `@agent-[Name]` triggers the appropriate specialist.

### 4c. Prompting Guide Integration

Add a **Prompting Guide** section that maps to `prompting-guide/` and describes the progressive complexity model:

- Level 1: INVEST+CRPG foundation (`01-foundation.md`)
- Level 2: Chain of Thought integration (`02-chain-of-thought.md`)
- Level 3: ReAct framework (`03-react-framework.md`)
- Level 4: Hybrid techniques (`04-hybrid-techniques.md`)
- Level 5: PyTorch automation path (`05-pytorch-automation.md`)
- MLE learning path (`06-mle-learning-path.md`)

Include the core flow: `User Request -> INVEST Story -> CoT Reasoning -> ReAct Actions -> CRPG Optimization -> PyTorch Code`

### 4d. Update Authority and Delegation

- Add ML workflow delegation guidelines (e.g., "For training pipeline tasks, delegate to TrainingOrchestrator with test-first requirement via Test Developer")
- Update the "Sync Flow" to include ML experiment tracking alongside sprint planning
- Reference prompt-templates as the starting point for new ML task requests

