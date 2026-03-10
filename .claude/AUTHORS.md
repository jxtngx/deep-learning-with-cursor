# Authors

## Primary Author & Architect

**jxtngx** (https://github.com/jxtngx)

### Core Contributions

- **Agent Architecture Design**: Created the multi-agent system for collaborative ML development
- **Prompt Template Framework**: Designed comprehensive prompt templates for vision, NLP, multimodal, pre-training, and fine-tuning tasks
- **Modular PyTorch Architecture**: Established the non-package module structure for simplified deployment
- **AWS Integration Patterns**: Developed cloud-native patterns for EC2, S3, SageMaker, and Bedrock
- **LocalStack Integration**: Added local AWS emulation capabilities for cost-effective development
- **Test-Driven Development Workflow**: Implemented TDD principles with torch.testing preference

### Agent System Design

Designed and documented 15 specialized agents:
- DatasetCurator, DataEngineer, TransformSpecialist (Data Pipeline)
- ModelArchitect, NetworkArchitect (Model Architecture)
- TrainingOrchestrator, MetricsArchitect, RunnerOrchestrator (Training & Evaluation)
- CloudEngineer, ComputeOrchestrator, LocalStackEmulator (Infrastructure)
- TestArchitect, InterfaceDesigner (Quality & Interface)
- Supervisor, DomainExpert (Strategy)

## License

This project is licensed under the Apache License, Version 2.0.
Copyright 2025 jxtngx

## Contact

Repository: https://github.com/jxtngx/claude-code-pytorch
Issues: https://github.com/jxtngx/claude-code-pytorch/issues