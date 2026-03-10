# Agent Team Changelog

## 2026-03-09 -- Port Claude ML Agents to Cursor

### Hired (10 agents ported from `.claude/agents/`)

Unique PyTorch ML expertise not covered by tenured Cursor team:

| Agent | Source | Rationale |
|-------|--------|-----------|
| ComputeOrchestrator | `compute.md` | GPU instance selection, EFA/NVLink, NCCL -- AWS Engineer lacks ML compute depth |
| DomainExpert | `expert.md` | Domain-to-ML translation (biology, physics, finance, etc.) -- no equivalent |
| NetworkArchitect | `network.md` | Custom neural architectures, NAS -- no equivalent |
| DataEngineer | `dataloader.md` | PyTorch DataLoader, distributed sampling -- no equivalent |
| DatasetCurator | `datasets.md` | HuggingFace dataset discovery and licensing -- ML Engineer too general |
| ModelArchitect | `models.md` | HuggingFace model selection, quantization -- ML Engineer too general |
| TransformSpecialist | `transforms.md` | TorchVision, Albumentations, Kornia -- no equivalent |
| RunnerOrchestrator | `runner.md` | Pipeline orchestration with Hydra, MLflow, W&B -- no equivalent |
| MetricsArchitect | `metrics.md` | Domain-specific metrics via TorchMetrics -- no equivalent |
| TrainingOrchestrator | `trainer.md` | Training loops, DDP/FSDP, mixed precision -- ML Engineer is MLOps-focused |

### Fired (5 agents -- not ported)

Redundant with tenured Cursor team members:

| Agent | Covered By | Notes |
|-------|------------|-------|
| CloudEngineer | AWS Engineer | Both handle AWS services, APIs, IaC |
| Supervisor | Product Manager + Scrum Master | Requirements and sprint process covered |
| InterfaceDesigner | Designer + Frontend Engineer | Diagrams/wireframes + implementation covered |
| TestArchitect | Test Developer | PyTorch testing expertise merged into Test Developer |
| LocalStackEmulator | AWS Engineer | Already owns LocalStack config |

### Tenured Team Updates

- **Test Developer**: Merged TestArchitect's PyTorch ML testing expertise (`torch.testing`, `gradcheck`, shape validation, numerical stability)
- **Chief Fullstack Architect**: Updated with ML pipeline team, prompt-templates mapping, and prompting-guide integration
