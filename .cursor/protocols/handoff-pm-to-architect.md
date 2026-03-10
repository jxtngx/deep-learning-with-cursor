# Handoff Protocol: Product Manager to Chief Architect

This document defines the handoff protocol when Product Manager completes product discovery and needs Chief Architect validation.

## When to Initiate Handoff

After:
1. Product discovery questionnaire completed
2. Technical requirements document generated
3. User has reviewed and approved requirements
4. GitHub issue script configured

## Handoff Checklist

Before handing off to Chief Architect, ensure:

- [ ] Technical requirements document created in `.cursor/plans/project-init/`
- [ ] Document includes all required sections
- [ ] Technology stack clearly documented (defaults or customized)
- [ ] AWS services identified and justified
- [ ] Architecture diagram included
- [ ] Scale and performance requirements realistic
- [ ] GitHub repository configured in create-github-issue.sh
- [ ] Sprint plan file name determined
- [ ] User has approved the requirements
- [ ] Research reports incorporated (if applicable)
- [ ] System architecture diagrams included (Figma exports or Mermaid)
- [ ] UI wireframes included (if applicable)
- [ ] Design specifications documented (if applicable)

## Handoff Message Template

Use this template when notifying Chief Architect:

```markdown
@chief-architect

Product discovery completed for: **[Product Name]**

## Technical Requirements Document

File: `.cursor/plans/project-init/[filename].plan.md`

## Review Requests

Please validate the following:

### 1. Technical Feasibility
- [ ] Proposed architecture is buildable with current stack
- [ ] Technology choices are appropriate for scale requirements
- [ ] AWS services are justified and cost-effective
- [ ] Database choice matches data requirements
- [ ] Performance targets are achievable

### 2. Technology Stack Compatibility
- [ ] Frontend and backend integration approach
- [ ] Database compatibility with backend framework
- [ ] AI/ML framework integration (HuggingFace/LangChain/Bedrock)
- [ ] Observability tools (SigNoz/Phoenix) properly configured
- [ ] Docker and infrastructure setup

### 3. Architecture Patterns
- [ ] Recommend specific patterns for this product type
- [ ] Identify reusable components from template
- [ ] Define API structure and data flow
- [ ] Authentication and authorization approach
- [ ] Error handling and logging strategy

### 4. Risk Assessment
- [ ] Technical risks and mitigation strategies
- [ ] Third-party service dependencies
- [ ] Scalability bottlenecks
- [ ] Security considerations
- [ ] Performance concerns

## Key Details

- **Uses Template Defaults**: [Yes/No]
- **Target Users**: [User types]
- **Expected Scale**: [Scale tier]
- **AWS Services**: [List]
- **MCP Integrations**: [Enabled/Disabled]

## Research and Design Outputs

### Scientific Research
- **Engaged**: [Yes/No]
- **Mode**: [MCP/Collaboration/N/A]
- **Domain**: [Domain]
- **Key Findings**: [Summary]
- **MCP Research Report**: [Path]

### Business Research
- **Engaged**: [Yes/No]
- **Mode**: [MCP/Collaboration/N/A]
- **Vertical**: [Vertical]
- **Key Findings**: [Summary]
- **Compliance Requirements**: [List]
- **MCP Research Report**: [Path]

### Design Outputs
- **System Diagrams**: [Figma links and export paths or Mermaid code locations]
- **UI Wireframes**: [Figma links or text descriptions] (if created)
- **Design Specs**: [Document path] (if created)
- **Designer Mode**: [MCP/Collaboration]

### Designer Collaboration Status
**Note**: System diagrams have already been reviewed and approved by Chief Architect during the design phase. This handoff includes the final validated diagrams.

## Next Steps

After your validation:
1. Update agent files with project-specific context
2. Define architecture patterns and conventions
3. Identify team member assignments
4. Notify Product Manager of completion
5. Product Manager will then hand off to Scrum Master for sprint planning
```

## Expected Chief Architect Actions

Chief Architect should:

### 1. Review Technical Requirements

Read the technical requirements document thoroughly and validate:
- Feasibility of proposed features
- Appropriateness of technology choices
- Scalability of architecture
- Security considerations
- Cost implications of AWS services

### 2. Validate or Challenge

For each aspect, either:
- **Approve**: Confirm it's feasible and well-designed
- **Suggest Improvements**: Recommend better approaches
- **Raise Concerns**: Identify risks that need mitigation
- **Reject**: If fundamentally infeasible, explain why

### 3. Define Architecture Patterns

Document specific patterns for this product:

**API Structure**:
```python
# Example: RESTful endpoint pattern
@app.get("/api/v1/resources/{resource_id}")
async def get_resource(resource_id: str):
    ...
```

**Data Models**:
```python
# Example: SQLAlchemy model pattern
class Resource(Base):
    __tablename__ = "resources"
    id = Column(UUID, primary_key=True)
    ...
```

**Frontend Components**:
```typescript
// Example: Component pattern
export function ResourceCard({ resource }: ResourceCardProps) {
  ...
}
```

### 4. Update Agent Files

Add project-specific context to relevant agent files:

**Backend Engineer** (`.cursor/agents/backend-engineer.md`):
- Add project-specific API patterns
- Document database schema approach
- Define business logic organization

**Frontend Engineer** (`.cursor/agents/frontend-engineer.md`):
- Add UI component guidelines
- Document state management approach
- Define routing structure

**AWS Engineer** (`.cursor/agents/aws-engineer.md`):
- List required AWS services
- Define infrastructure as code approach
- Document LocalStack configuration

**Test Developer** (`.cursor/agents/test-developer.md`):
- Define testing strategy
- Specify coverage requirements
- List critical test scenarios

### 5. Notify Product Manager

After validation, respond with:

```markdown
@product-manager

Technical requirements validated for: **[Product Name]**

## Validation Results

✅ **Approved**: Technical requirements are feasible and well-designed

[OR]

⚠️ **Approved with Recommendations**: See suggestions below

[OR]

❌ **Concerns Raised**: See critical issues below

## Architecture Decisions

[Document key architecture patterns and decisions]

## Team Assignments (Preliminary)

- **Backend Engineer**: [Key responsibilities]
- **Frontend Engineer**: [Key responsibilities]
- **AWS Engineer**: [Key responsibilities]
- **Test Developer**: [Coverage requirements]
- **Notion/Linear/Discord Engineers**: [If MCP enabled]

## Agent Files Updated

- [ ] backend-engineer.md
- [ ] frontend-engineer.md
- [ ] aws-engineer.md
- [ ] test-developer.md

## Ready for Sprint Planning

Technical requirements are validated. Please proceed with Scrum Master handoff for sprint plan creation.

## Notes

[Any additional context or recommendations]
```

## Validation Criteria

### Technical Feasibility Checklist

- [ ] All core features can be implemented with chosen stack
- [ ] API endpoints are RESTful and well-structured
- [ ] Database schema can support required queries
- [ ] Authentication method is secure and scalable
- [ ] File storage approach is cost-effective
- [ ] AI/ML integration is properly architected
- [ ] Observability covers critical paths

### Technology Stack Compatibility

- [ ] Frontend can communicate with backend API
- [ ] Backend framework supports required database
- [ ] AI/ML frameworks integrate smoothly
- [ ] Docker configuration supports all services
- [ ] AWS services work together coherently
- [ ] LocalStack can emulate required AWS services

### Architecture Pattern Validation

- [ ] Follows single responsibility principle
- [ ] Separation of concerns (controller/service/repository)
- [ ] Error handling is centralized
- [ ] Logging strategy is consistent
- [ ] Configuration management is secure
- [ ] API versioning strategy defined

### Risk Assessment

Common risks to evaluate:

**Scalability Risks**:
- Database query performance at scale
- API rate limiting approach
- Caching strategy
- CDN for static assets

**Security Risks**:
- Authentication vulnerabilities
- Authorization bypass potential
- SQL injection prevention
- XSS protection
- API key management

**Dependency Risks**:
- Third-party service availability
- API rate limits
- Cost overruns on cloud services
- Framework version compatibility

**Performance Risks**:
- N+1 query problems
- Large payload handling
- Real-time requirements
- Cold start latency (Lambda)

## Edge Cases

### Template Defaults with Custom Features

If using template defaults but features require additional services:
- Evaluate if defaults still appropriate
- Consider hybrid approach
- Document deviations and reasons

### Large Scale with Minimal AWS

If large scale expected but minimal AWS services:
- Challenge the scale estimates
- Recommend additional services
- Explain cost/benefit tradeoffs

### Complex AI/ML Without Bedrock

If heavy AI/ML requirements but no Bedrock:
- Evaluate HuggingFace/LangChain limitations
- Consider self-hosted vs. managed trade-offs
- Estimate compute requirements

## Post-Validation Actions

After Chief Architect completes validation:

1. **Product Manager** receives notification
2. **Product Manager** reviews any recommendations or concerns
3. If concerns raised: **Product Manager** discusses with user and updates requirements
4. Once fully validated: **Product Manager** proceeds to Scrum Master handoff
5. **Chief Architect** may join sprint planning for architectural guidance

## Collaboration During Sprint

Chief Architect remains available during sprint for:
- Architecture questions from engineers
- Technical blocker resolution
- Code review of critical components
- Performance optimization guidance
- Security review

## Documentation

All architecture decisions should be documented in:
- Technical requirements document (updated with Chief Architect notes)
- Agent files (project-specific context)
- Architecture decision records (ADRs) if needed for complex decisions
