# Run Ticket Plan

Select the next available ticket, validate dependencies, create feature branch, and direct the user to the ticket's plan file for implementation.

## Usage

```
@run-ticket-plan
```

No ticket ID required - the command automatically determines the next ticket to work on.

## Purpose

This command does NOT implement code. It:
1. Selects the optimal next ticket using agent consultation
2. Validates git state and dependencies
3. Creates the feature branch
4. Directs you to the ticket plan file to begin implementation

**You implement from the ticket plan file directly.**

## Workflow

```mermaid
graph TD
    A[Invoke Command] --> B[Consult Agents]
    B --> C[Select Next Ticket]
    C --> D[Validate Git State]
    D --> E[Check Dependencies]
    E --> F[Create Feature Branch]
    F --> G[Display Plan Path]
    G --> H[User Implements]
    
    B --> B1[Scrum Master]
    B --> B2[Chief Fullstack Architect]
    B1 --> B3[Sprint Status]
    B2 --> B4[Technical Readiness]
    B3 --> C
    B4 --> C
    
    D --> D1{On main?}
    D1 -->|No| D2[Fail: Switch to main]
    D1 -->|Yes| D3{Clean state?}
    D3 -->|No| D4[Fail: Commit changes]
    D3 -->|Yes| E
    
    E --> E1[Load Sprint Plan]
    E1 --> E2[Extract Dependencies]
    E2 --> E3[Load Ticket Plan]
    E3 --> E4[Check Each Dependency]
    E4 --> E5{All merged?}
    E5 -->|No| E6[Fail: List pending PRs]
    E5 -->|Yes| F
```

## Steps

### 0. Ticket Selection (Automated)

Consult agents to determine next ticket:

**Scrum Master Assessment** (`.cursor/agents/scrum-master.md`):
- Review sprint plan progress
- Identify completed tickets from git history
- Calculate sprint velocity and capacity
- Filter to tickets with satisfied dependencies
- Prioritize by phase and critical path

**Chief Fullstack Architect Assessment** (`.cursor/agents/chief-architect.md`):
- Evaluate technical readiness
- Check for architectural blockers
- Verify prerequisite knowledge available
- Assess risk and complexity
- Recommend optimal ticket for current context

**Selection Criteria**:
1. All dependencies merged to main
2. Highest priority in current phase
3. Matches team member specialization (if agent context available)
4. Technically ready (no architectural blockers)
5. Fits within remaining sprint capacity

**Output**: Selected ticket ID (e.g., `FE-002`)

### 1. Git State Validation

Verify repository state before starting work:

- Current branch is `main`
- Working directory is clean
- Local main is up to date with remote

### 2. Dependency Resolution

Check ticket dependencies are satisfied:

- Parse sprint plan table for ticket's "Depends On" column
- Parse ticket plan file for dependency mentions
- Verify each dependency ticket has merged PR in git history
- Report any unmerged dependencies with commit search

### 3. Branch Creation

Create feature branch following convention:

- Pattern: `feature/TICKET-ID-short-description`
- Example: `feature/FE-002-dashboard-component`
- Branch from current main

### 4. Display Plan Path

Provide clear instruction to user:

- Display full path to ticket plan file
- Highlight the plan file for the user to reference
- Summarize key deliverables from plan
- Confirm branch is ready for work

**The user implements from the plan file - the command does NOT auto-implement.**

## Pre-flight Checks

Before executing, validate:

| Check | Command | Expected |
|-------|---------|----------|
| Sprint plan exists | Read `.cursor/plans/sprint_*.plan.md` | File found |
| Agents available | Read `.cursor/agents/scrum-master.md` | File found |
| Agents available | Read `.cursor/agents/chief-architect.md` | File found |
| Current branch | `git branch --show-current` | `main` |
| Clean state | `git status --porcelain` | Empty output |
| Up to date | `git fetch && git status` | No "behind" message |
| Dependencies | `git log --all --grep="[TICKET]"` | Commit exists for each |

## Ticket Selection Process

### Step 1: Gather Sprint Context

Parse sprint plan table to extract:
- All ticket IDs and their status
- Dependency relationships
- Phase groupings
- Current week/phase

Search git history for completed tickets:
```bash
git log --all --oneline | grep -E '\[(FE|BE|INFRA|TEST|DOC)-[0-9]+\]'
```

### Step 2: Consult Scrum Master

Invoke scrum-master agent with context:
- Sprint plan file path
- Completed tickets list
- Current phase

Ask scrum-master to:
1. Identify tickets ready to start (dependencies satisfied)
2. Prioritize by sprint goals and critical path
3. Consider sprint velocity and capacity
4. Return top 3 candidate tickets

### Step 3: Consult Chief Fullstack Architect

Invoke chief-architect agent with:
- Top 3 candidate tickets from scrum-master
- Current codebase state
- Recent changes or context

Ask chief-architect to:
1. Assess technical readiness for each candidate
2. Identify any architectural blockers
3. Recommend single ticket to work on next
4. Provide technical context for implementation

### Step 4: Final Selection

Select the ticket recommended by chief-architect and proceed with validation and branch creation.

## Dependency Validation

For ticket with dependencies `FE-002, BE-003`:

1. Search git history: `git log --all --grep="\[FE-002\]" --oneline`
2. Verify commit exists on main branch
3. Check commit is merged (not on abandoned branch)
4. Repeat for each dependency

If dependency missing:

- Report unmerged dependency ticket
- List expected commit message pattern: `[TICKET-ID]`
- Block execution until dependencies satisfied

## Branch Naming

Extract short description from ticket plan file:

- Read plan name field
- Convert to kebab-case
- Limit to 50 chars total
- Format: `feature/TICKET-ID-description`

Examples:

- `feature/FE-002-dashboard-component`
- `feature/BE-001-auth-endpoint`
- `feature/INFRA-003-docker-compose`

## Error Handling

| Error | Message | Resolution |
|-------|---------|------------|
| Sprint plan not found | `No sprint plan found in .cursor/plans/. Create sprint plan first.` | Create sprint plan file |
| Agent not found | `Agent {name} not found at {path}. Check agent files.` | Verify agent file exists |
| No available tickets | `No tickets ready to start. All available tickets have unmet dependencies.` | Complete dependency tickets first |
| Not on main | `Current branch is {branch}. Switch to main first.` | `git checkout main` |
| Dirty working tree | `Uncommitted changes detected. Commit or stash.` | `git status` |
| Missing dependency | `Dependency {TICKET} not merged. Required PRs: {list}` | Wait for PR merge |
| Plan file not found | `No plan file for {TICKET}. Create plan first.` | Create plan file |
| Branch exists | `Branch feature/{TICKET} exists. Delete or reuse?` | `git branch -D feature/{TICKET}` |
| Agent disagreement | `Scrum master and architect disagree on ticket priority. Manual selection required.` | Provide ticket ID manually |

## Implementation Flow

After successful ticket selection and validation:

1. Display selected ticket ID and rationale
2. Show agent recommendations and context
3. Create feature branch
4. Display ticket plan file path
5. Summarize key deliverables
6. User implements by referencing the plan file directly

**IMPORTANT**: This command only prepares the environment. The user always implements from the ticket plan file (e.g., `@.cursor/plans/fe-001_component_setup_fac33c9f.plan.md`).

## Agent Coordination

```mermaid
sequenceDiagram
    participant C as Command
    participant SM as Scrum Master
    participant CA as Chief Architect
    participant G as Git
    
    C->>C: Load Sprint Plan
    C->>G: Get Completed Tickets
    C->>SM: Assess Sprint Status
    SM-->>C: Top 3 Candidates
    C->>CA: Evaluate Technical Readiness
    CA-->>C: Recommended Ticket + Context
    C->>C: Validate Dependencies
    C->>G: Create Feature Branch
    C->>C: Display Plan
```

## Example Output

```
[TICKET SELECTION]
Scrum Master recommends: FE-002, BE-003, INFRA-001
  - FE-002: Highest priority, critical path
  - BE-003: Parallel work opportunity
  - INFRA-001: Independent, can start anytime

Chief Fullstack Architect recommends: FE-002
  - Technical readiness: HIGH
  - Dependencies satisfied: FE-001 merged in commit abc123
  - Context: Component structure ready, API integration straightforward
  - Risk: LOW - isolated to component directory

[SELECTED TICKET]
FE-002: Implement Dashboard Component

[GIT VALIDATION]
✓ On main branch
✓ Working directory clean
✓ Up to date with origin/main
✓ Dependency FE-001 merged

[BRANCH CREATION]
Creating branch: feature/FE-002-dashboard-component
Branch created successfully

[READY FOR IMPLEMENTATION]
Plan file: @.cursor/plans/fe-002_dashboard_component_614da315.plan.md

Use the plan file above to implement this ticket.

Key deliverables:
- Implement Dashboard component with Shadcn UI
- Add data fetching with API client
- Implement responsive layout with Tailwind
- Add component tests

The feature branch is ready. Begin implementation from the plan file.
```
