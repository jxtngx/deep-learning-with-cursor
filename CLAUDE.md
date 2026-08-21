<!--
Copyright 2025 jxtngx
Licensed under Apache 2.0
-->

# Agent Router

Route ML/DL work to the four specialists in `.cursor/agents/`.

## Team

| Agent | Owns |
|-------|------|
| [chief-architect](.cursor/agents/chief-architect.md) | Pipeline topology, tech approval, routing, TDD gate |
| [research-scientist](.cursor/agents/research-scientist.md) | Methods, baselines, evaluation criteria |
| [data-engineer](.cursor/agents/data-engineer.md) | `src/data.py` |
| [ml-engineer](.cursor/agents/ml-engineer.md) | `src/network.py`, `src/trainer.py`, `src/runner.py`, `src/compute.py` |

## Routing

- Architecture or unclear scope: chief-architect
- Method, baseline, or metric choice: research-scientist
- Datasets, loaders, transforms: data-engineer
- Models, training, metrics implementation, runner, GPU: ml-engineer

Use `@agent-chief-architect`, `@agent-research-scientist`, `@agent-data-engineer`, or `@agent-ml-engineer`.

## Directives

### Penalties

- including code examples in agent files
- using emojis
- ignoring TDD
- verbose explanations
- code that does not follow the [PyTorch contributing guide](https://github.com/pytorch/pytorch/wiki/The-Ultimate-Guide-to-PyTorch-Contributions) and [design philosophy](https://docs.pytorch.org/docs/stable/community/design.html)
- adding AWS services outside of EC2, S3, SageMaker, and Bedrock without Chief Architect or user approval
- ignoring cost, security, maintainability, performance, testability, or documentation

### Rewards

- high code quality (ruff, black, mypy)
- concise docs
- test-first ML/DL changes
- cost-aware AWS use on the approved services
