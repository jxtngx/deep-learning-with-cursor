---
name: Bug report
about: Report a defect
title: ''
labels: 'bug'
assignees: ''

---

<!-- Copyright 2025 jxtngx | Apache 2.0 License | https://github.com/jxtngx/claude-code-pytorch -->

## User Story

**As a** [role: researcher/developer/user]
**I want to** [fix the specific defect]
**So that** [benefit/value delivered]

**Examples:**

1. As a model developer
   I want to fix the DataLoader memory leak during multi-GPU training
   So that I can train models without OOM errors on long-running jobs

2. As a cloud engineer
   I want to fix the model checkpoint corruption when saving to S3
   So that I can reliably resume training from any checkpoint

3. As a training engineer
   I want to fix gradient accumulation producing incorrect gradient values
   So that I can train large models with small batch sizes accurately

4. As a network architect
   I want to fix the custom attention layer causing NaN loss values
   So that I can train transformer models to convergence

5. As a developer using LocalStack
   I want to fix the LocalStackEmulator failing to mock SageMaker endpoints
   So that I can test deployment workflows locally before using AWS

## Acceptance Criteria
- [ ] [Specific, testable criteria for bug fix validation]
- [ ] [Another measurable criteria]
- [ ] [Performance/behavior requirement after fix]

## Definition of Done
- [ ] Bug reproduced and root cause identified
- [ ] Fix implemented and unit tests written
- [ ] All existing tests pass
- [ ] Code reviewed by appropriate agent/team member
- [ ] Documentation updated if needed
- [ ] No regression in related functionality
- [ ] Performance impact assessed

## Severity
- [ ] **Critical** - Production down, data loss, security vulnerability
- [ ] **High** - Major functionality broken, no workaround
- [ ] **Medium** - Functionality impaired, workaround available
- [ ] **Low** - Minor issue, cosmetic, edge case

## Estimated Effort
- [ ] **Small** (1-3 story points) - Few hours
- [ ] **Medium** (5-8 story points) - 1-2 days
- [ ] **Large** (13+ story points) - 3+ days

---

### Additional Context

**Error Messages/Stack Traces:**
```
[Paste complete error output here]
```

**Environment:**
- PyTorch version:
- Python version:
- OS:
- GPU/CUDA version (if applicable):

**Steps to Reproduce:**
1. [First step]
2. [Second step]
3. [...]

**Expected Behavior:**
[What should happen]

**Actual Behavior:**
[What actually happens]

**Screenshots/Logs:**
[If applicable, add visual evidence]

**Related Issues:**
[Link to related issues if any]
