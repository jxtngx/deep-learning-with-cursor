# Git Commit Standards

## Prohibited Patterns

Never add tool attribution trailers to commits:

```bash
# DO NOT USE
git commit --trailer "Made-with: Cursor"
git commit --trailer "Made-with: <any-tool>"
```

## Rationale

Commits should reflect the work done, not the tools used. Tool metadata clutters commit history and provides no value for code review or history tracking.
