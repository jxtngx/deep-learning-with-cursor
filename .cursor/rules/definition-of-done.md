# Definition of Done

Checklist that every story must satisfy before being marked complete.

## Code Complete

- [ ] Implementation matches acceptance criteria
- [ ] Code follows project style guide
- [ ] No commented-out code or TODOs
- [ ] Logging added for key operations

## Testing

- [ ] Unit tests written and passing
- [ ] Integration tests written (if applicable)
- [ ] Test coverage meets project threshold
- [ ] Manual testing completed

## Code Review

- [ ] Pull request created
- [ ] Chief Fullstack Architect or peer review approved
- [ ] All review comments addressed
- [ ] CI/CD pipeline passes

## Documentation

- [ ] Docstrings added to public functions
- [ ] README updated (if user-facing change)
- [ ] Architecture docs updated (if design change)
- [ ] API docs updated (if interface change)

## Integration

- [ ] Merged to main branch
- [ ] No merge conflicts
- [ ] No breaking changes (or migration path provided)
- [ ] Deployed to staging environment

## Story-Specific

Additional criteria based on story type:

| Type | Additional Requirements |
|------|-------------------------|
| New Feature | User acceptance demo, feature flag |
| Bug Fix | Regression test, root cause documented |
| Refactoring | Performance benchmarks unchanged |
| API Change | Backward compatibility or deprecation notice |

## Verification

Before marking done, ask:
1. Would this pass a code review?
2. Can another developer understand this?
3. Is this production-ready?
4. Does this add technical debt?
