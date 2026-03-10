# Configure GitHub Issue Script

Helper command to configure `.cursor/scripts/create-github-issue.sh` with project-specific settings.

## Purpose

After product discovery, the Product Manager needs to configure the repository for automated GitHub issue creation from sprint plan tickets.

## Configuration Variables

The script requires two variables to be set:

1. **_SPRINT_PLAN** (line 9): Path to the sprint plan file
2. **GITHUB_REPO** (line 13): GitHub repository in format `owner/repo`

## Implementation Steps

### 1. Gather Information

Ask user for:

**GitHub Repository**:
- Format: `owner/repo-name`
- Example: `jxtngx/cursor-fullstack-template`
- Validation: Must match pattern `^[a-zA-Z0-9-]+/[a-zA-Z0-9-_]+$`

**Sprint Plan File Name**:
- Suggest: `[product-name]-sprint.plan.md`
- Example: `task-management-app-sprint.plan.md`
- Location: `.cursor/plans/project-init/`
- Full path will be: `.cursor/plans/project-init/[filename]`

### 2. Validate Inputs

Check:
- GitHub repo format is correct
- Sprint plan file name ends with `.plan.md`
- No spaces in file name (use kebab-case)

### 3. Update create-github-issue.sh

Use `StrReplace` tool twice:

**First replacement (line 9)**:

```
old_string: _SPRINT_PLAN={{ THE-SPRINT-PLAN-FILE }}
new_string: _SPRINT_PLAN=.cursor/plans/project-init/[sprint-plan-filename]
```

**Second replacement (line 13)**:

```
old_string: GITHUB_REPO={{ THE-GITHUB-REPO }}
new_string: GITHUB_REPO=[owner]/[repo]
```

### 4. Verify Configuration

After making changes:
1. Read the script to confirm changes
2. Show user the updated configuration
3. Explain how to use the script:
   ```bash
   .cursor/scripts/create-github-issue.sh TICKET-ID
   ```

## Example Usage

### User Inputs
- GitHub Repo: `acme-corp/task-manager`
- Product Name: `Task Management App`
- Sprint Plan: `task-management-app-sprint.plan.md`

### Configuration Commands

```bash
# Line 9 becomes:
_SPRINT_PLAN=.cursor/plans/project-init/task-management-app-sprint.plan.md

# Line 13 becomes:
GITHUB_REPO=acme-corp/task-manager
```

## Error Handling

### Invalid GitHub Repo Format

If user provides invalid format:
```
❌ Invalid: jxtngx cursor-fullstack-template
❌ Invalid: https://github.com/jxtngx/cursor-fullstack-template
❌ Invalid: jxtngx.github.io/repo

✅ Valid: jxtngx/cursor-fullstack-template
```

### Invalid Sprint Plan File Name

If user provides invalid format:
```
❌ Invalid: sprint plan.md (has space)
❌ Invalid: sprint_plan.txt (wrong extension)
❌ Invalid: SPRINT-PLAN.PLAN.MD (too many dots before extension)

✅ Valid: task-manager-sprint.plan.md
✅ Valid: my-app-sprint.plan.md
```

## Validation Function

Use this logic to validate inputs:

```python
def validate_github_repo(repo: str) -> bool:
    """Validate GitHub repo format: owner/repo"""
    import re
    pattern = r'^[a-zA-Z0-9-]+/[a-zA-Z0-9-_]+$'
    return bool(re.match(pattern, repo))

def validate_sprint_plan_name(filename: str) -> bool:
    """Validate sprint plan file name"""
    return (
        filename.endswith('.plan.md') and
        ' ' not in filename and
        filename.replace('-', '').replace('_', '').replace('.', '').isalnum()
    )
```

## Integration with Product Discovery

This configuration happens in product discovery flow:

1. User completes questionnaire
2. Product Manager generates technical requirements
3. **Product Manager configures GitHub issue script** ← This step
4. Product Manager hands off to Chief Architect
5. Chief Architect validates
6. Scrum Master creates sprint plan (file name matches what was configured)
7. Script is ready to create issues from tickets

## Post-Configuration

After configuration, the script can be used to create GitHub issues:

```bash
# Example: Create issue for ticket FEAT-001
.cursor/scripts/create-github-issue.sh FEAT-001

# The script will:
# 1. Read sprint plan from configured path
# 2. Extract ticket details for FEAT-001
# 3. Create GitHub issue in configured repo
# 4. Link to sprint epic
# 5. Apply appropriate labels
```

## Notes

- Configuration is project-specific
- Each new product needs reconfiguration
- Consider creating a backup before modifying
- If multiple products in same repo, script supports only one sprint plan at a time
- For multiple projects, consider separate branches or repositories

## Rollback

If configuration needs to be reset:

```bash
# Restore placeholders
_SPRINT_PLAN={{ THE-SPRINT-PLAN-FILE }}
GITHUB_REPO={{ THE-GITHUB-REPO }}
```

Use git to revert:
```bash
git checkout .cursor/scripts/create-github-issue.sh
```
