# Architecture Decision Records

This directory contains Architecture Decision Records (ADRs) for the Claude Code PyTorch project.

## What is an ADR?

An Architecture Decision Record captures an important architectural decision made along with its context and consequences.

## ADR Index

| ADR | Title | Status | Date |
|-----|-------|--------|------|
| [ADR-001](001-agile-methodology.md) | Adopt Agile Methodology | Accepted | 2025-01-26 |

## Creating a New ADR

1. Copy `template.md` to a new file: `XXX-title-of-decision.md`
2. Fill in all sections
3. Update this index
4. Submit for review through standard PR process

## ADR Lifecycle

- **Proposed**: Under discussion
- **Accepted**: Decision ratified and in effect
- **Deprecated**: No longer relevant but kept for historical context
- **Superseded**: Replaced by another ADR (link to the new one)

## Integration with Agile Process

ADRs are reviewed during:
- Sprint planning (for proposed ADRs affecting upcoming work)
- Sprint retrospectives (for lessons learned)
- Architecture reviews (quarterly)