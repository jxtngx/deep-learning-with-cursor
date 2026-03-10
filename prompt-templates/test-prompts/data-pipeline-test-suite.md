<!-- Copyright 2025 jxtngx | Apache 2.0 License | https://github.com/jxtngx/claude-code-pytorch -->

# Data Pipeline Test Suite

@agent-TestArchitect I need comprehensive tests for a data pipeline that will handle image datasets with augmentations. The tests should verify DataLoader functionality, transformation pipelines, batch collation, and dataset iteration. Please write tests using torch.testing utilities that check tensor shapes after transforms, data type preservation, augmentation reproducibility with seeds, proper handling of edge cases (empty batches, single samples), and memory efficiency. Tests should fail initially and guide the implementation of create_dataloaders(), get_transforms(), and HFDatasetWrapper classes.

## Requirements

- Testing framework: torch.testing preferred
- Coverage target: >95% for data modules
- Test execution: <5 seconds for unit tests
- Memory limit: <1GB for test data

## Success Criteria

- Shape validation using torch.testing.assert_close()
- Deterministic testing with fixed seeds
- Edge case coverage
- Performance benchmarks included

## Deliverables

- Complete test suite before implementation
- All tests initially fail (red phase)
- Guide implementation to pass (green phase)
- Enable safe refactoring
