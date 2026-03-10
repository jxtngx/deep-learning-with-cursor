# Product Discovery Command

Guide users through structured product idea formation using conditional questionnaires.

## Implementation Steps

### 1. Initialize Session

Read README.md to load opinionated technology stack defaults:
- Python + TypeScript
- Next.js + Shadcn UI
- FastAPI
- PostgreSQL or Cassandra
- HuggingFace + LangChain
- Docker + Make
- AWS + LocalStack
- SigNoz + Phoenix
- MCP Integrations (Notion, Linear, Discord)

### 2. Question Sequence

#### Q1: Technology Stack Decision

Use AskQuestion tool:

```json
{
  "title": "Product Discovery - Technology Stack",
  "questions": [
    {
      "id": "use-defaults",
      "prompt": "This template uses an opinionated tech stack: Python/TypeScript, Next.js, FastAPI, AWS, HuggingFace, LangChain, Docker, SigNoz. Would you like to use these defaults?",
      "options": [
        {"id": "yes-defaults", "label": "Yes - Use template defaults (recommended for faster setup)"},
        {"id": "customize", "label": "No - I want to customize the technology stack"}
      ],
      "allow_multiple": false
    }
  ]
}
```

Store response as `uses_template_defaults`.

#### Q2: Customization (Conditional)

If user selected "customize", ask:

```json
{
  "title": "Technology Stack Customization",
  "questions": [
    {
      "id": "frontend",
      "prompt": "Frontend Framework?",
      "options": [
        {"id": "nextjs", "label": "Next.js (default)"},
        {"id": "react", "label": "React (vanilla)"},
        {"id": "vue", "label": "Vue.js"},
        {"id": "other-frontend", "label": "Other"}
      ],
      "allow_multiple": false
    },
    {
      "id": "backend",
      "prompt": "Backend Framework?",
      "options": [
        {"id": "fastapi", "label": "FastAPI (default)"},
        {"id": "express", "label": "Express.js"},
        {"id": "django", "label": "Django"},
        {"id": "other-backend", "label": "Other"}
      ],
      "allow_multiple": false
    },
    {
      "id": "database",
      "prompt": "Database?",
      "options": [
        {"id": "postgresql", "label": "PostgreSQL (default for relational)"},
        {"id": "cassandra", "label": "Cassandra (default for time-series/high-volume)"},
        {"id": "mongodb", "label": "MongoDB"},
        {"id": "other-db", "label": "Other"}
      ],
      "allow_multiple": false
    }
  ]
}
```

#### Q3: Target Users

```json
{
  "title": "Product Discovery - Target Users",
  "questions": [
    {
      "id": "target-users",
      "prompt": "Who are the primary users of this product?",
      "options": [
        {"id": "developers", "label": "Individual developers"},
        {"id": "small-teams", "label": "Small teams (2-10 people)"},
        {"id": "enterprises", "label": "Enterprise organizations"},
        {"id": "consumers", "label": "End consumers (B2C)"},
        {"id": "mixed", "label": "Mixed user base"}
      ],
      "allow_multiple": true
    }
  ]
}
```

#### Q4: Product Name and Overview

**First, provide examples to help the user:**

**One-sentence Description Examples:**
- "A mobile-first meal planning app that uses AI to generate personalized weekly menus based on dietary preferences and pantry inventory"
- "A real-time collaboration platform for remote teams to brainstorm ideas using visual boards and AI-powered suggestion features"
- "A consumer health tracking app that integrates wearable data with AI coaching to provide personalized wellness recommendations"

**Problem Statement Examples:**
- "Consumers waste time and money on meal planning because they lack personalized recipe suggestions that match their dietary needs and available ingredients"
- "Remote teams struggle with creative collaboration due to fragmented tools and lack of real-time ideation features, leading to slower project timelines"
- "Health-conscious consumers find it difficult to make sense of their fitness data and lack actionable insights to improve their wellness journey"

**Then ask for product name using AskQuestion:**

```json
{
  "title": "Product Discovery - Product Name",
  "questions": [
    {
      "id": "product-name-choice",
      "prompt": "What would you like to name your product? Choose from suggestions or provide your own name",
      "options": [
        {"id": "suggestion-1", "label": "MealMind - AI-powered meal planning assistant"},
        {"id": "suggestion-2", "label": "CollabCanvas - Visual collaboration workspace"},
        {"id": "custom-name", "label": "I have my own product name (please provide it in chat after selecting)"}
      ],
      "allow_multiple": false
    }
  ]
}
```

If user selects "custom-name", ask them to provide their product name in the conversation.

**Then gather description and problem statement conversationally:**
- Ask: "Please provide a one-sentence description of your product (see examples above for reference)"
- Ask: "Please describe the problem your product solves (see examples above for reference)"

#### Q5: Core Features

Ask user to describe 3-5 core features via conversation. For each feature, follow up with priority:

```json
{
  "title": "Feature Priority",
  "questions": [
    {
      "id": "feature-1-priority",
      "prompt": "Priority for [Feature Name]?",
      "options": [
        {"id": "must-have", "label": "Must-have (MVP requirement)"},
        {"id": "nice-to-have", "label": "Nice-to-have (post-MVP)"}
      ],
      "allow_multiple": false
    }
  ]
}
```

Repeat for each feature.

#### Q6: Data Requirements

```json
{
  "title": "Data Requirements",
  "questions": [
    {
      "id": "data-needs",
      "prompt": "What type of data storage do you need?",
      "options": [
        {"id": "none", "label": "No database needed (static/serverless)"},
        {"id": "relational", "label": "Relational data (PostgreSQL recommended)"},
        {"id": "timeseries", "label": "Time-series or high-volume data (Cassandra recommended)"},
        {"id": "document", "label": "Document store (MongoDB)"},
        {"id": "mixed-data", "label": "Multiple database types"}
      ],
      "allow_multiple": true
    }
  ]
}
```

#### Q7: AWS Services

```json
{
  "title": "AWS Services Selection",
  "questions": [
    {
      "id": "aws-compute",
      "prompt": "What compute services do you need?",
      "options": [
        {"id": "ec2", "label": "EC2 (virtual machines for model training)"},
        {"id": "ecs", "label": "ECS (container orchestration)"},
        {"id": "lambda", "label": "Lambda (serverless functions)"},
        {"id": "no-compute", "label": "None / local only"}
      ],
      "allow_multiple": true
    },
    {
      "id": "aws-storage",
      "prompt": "What storage services do you need?",
      "options": [
        {"id": "s3", "label": "S3 (object storage)"},
        {"id": "rds", "label": "RDS (managed database)"},
        {"id": "no-storage", "label": "None / local only"}
      ],
      "allow_multiple": true
    },
    {
      "id": "aws-ai",
      "prompt": "What AI/ML services do you need?",
      "options": [
        {"id": "bedrock", "label": "Bedrock (model hosting)"},
        {"id": "sagemaker", "label": "SageMaker (training/inference)"},
        {"id": "no-ai", "label": "None / using HuggingFace only"}
      ],
      "allow_multiple": true
    }
  ]
}
```

Note: LocalStack is automatically enabled for local AWS emulation.

#### Q8: External Integrations

```json
{
  "title": "External Integrations",
  "questions": [
    {
      "id": "auth-provider",
      "prompt": "Authentication method?",
      "options": [
        {"id": "custom-auth", "label": "Custom authentication (build in-house)"},
        {"id": "auth0", "label": "Auth0"},
        {"id": "clerk", "label": "Clerk"},
        {"id": "cognito", "label": "AWS Cognito"},
        {"id": "no-auth", "label": "No authentication needed"}
      ],
      "allow_multiple": false
    },
    {
      "id": "payment",
      "prompt": "Payment processing?",
      "options": [
        {"id": "stripe", "label": "Stripe"},
        {"id": "paypal", "label": "PayPal"},
        {"id": "no-payment", "label": "No payment processing"}
      ],
      "allow_multiple": false
    },
    {
      "id": "other-integrations",
      "prompt": "Other third-party services?",
      "options": [
        {"id": "email", "label": "Email service (SendGrid, SES)"},
        {"id": "sms", "label": "SMS (Twilio)"},
        {"id": "analytics", "label": "Analytics (Segment, Mixpanel)"},
        {"id": "none-other", "label": "None"}
      ],
      "allow_multiple": true
    }
  ]
}
```

#### Q9: Scale Requirements

```json
{
  "title": "Scale & Performance",
  "questions": [
    {
      "id": "scale",
      "prompt": "Expected scale at launch?",
      "options": [
        {"id": "prototype", "label": "Prototype (< 100 users) - LocalStack + SigNoz"},
        {"id": "small", "label": "Small scale (100-1K users) - AWS Free Tier"},
        {"id": "medium", "label": "Medium scale (1K-100K users) - AWS paid"},
        {"id": "large", "label": "Large scale (100K+ users) - AWS enterprise"}
      ],
      "allow_multiple": false
    },
    {
      "id": "performance",
      "prompt": "Performance requirements?",
      "options": [
        {"id": "standard", "label": "Standard (< 1s response time)"},
        {"id": "fast", "label": "Fast (< 500ms response time)"},
        {"id": "realtime", "label": "Real-time (< 100ms response time)"}
      ],
      "allow_multiple": false
    }
  ]
}
```

#### Q10: UI/UX Preferences

```json
{
  "title": "UI/UX Preferences",
  "questions": [
    {
      "id": "design-style",
      "prompt": "Design style preference?",
      "options": [
        {"id": "minimalist", "label": "Minimalist"},
        {"id": "dashboard", "label": "Feature-rich dashboard"},
        {"id": "mobile-first", "label": "Mobile-first"},
        {"id": "standard", "label": "Standard web app"}
      ],
      "allow_multiple": true
    },
    {
      "id": "accessibility",
      "prompt": "Accessibility requirements?",
      "options": [
        {"id": "wcag-aa", "label": "WCAG 2.1 AA compliance"},
        {"id": "wcag-aaa", "label": "WCAG 2.1 AAA compliance"},
        {"id": "basic", "label": "Basic accessibility"},
        {"id": "standard-access", "label": "Standard (no special requirements)"}
      ],
      "allow_multiple": false
    },
    {
      "id": "dark-mode",
      "prompt": "Dark mode support?",
      "options": [
        {"id": "yes-dark", "label": "Yes (Shadcn UI supports by default)"},
        {"id": "no-dark", "label": "No"}
      ],
      "allow_multiple": false
    }
  ]
}
```

#### Q11: MCP Work Tracking

```json
{
  "title": "Work Tracking Integration",
  "questions": [
    {
      "id": "mcp-enabled",
      "prompt": "Enable MCP work tracking integrations (Notion, Linear, Discord)?",
      "options": [
        {"id": "yes-mcp", "label": "Yes - Enable all MCP integrations"},
        {"id": "partial-mcp", "label": "Partial - Enable specific integrations"},
        {"id": "no-mcp", "label": "No - Manual tracking only"}
      ],
      "allow_multiple": false
    }
  ]
}
```

If "partial-mcp" selected, follow up with:

```json
{
  "title": "Select MCP Integrations",
  "questions": [
    {
      "id": "mcp-services",
      "prompt": "Which integrations to enable?",
      "options": [
        {"id": "notion", "label": "Notion (documentation, sprint planning)"},
        {"id": "linear", "label": "Linear (issue tracking)"},
        {"id": "discord", "label": "Discord (team communication)"}
      ],
      "allow_multiple": true
    }
  ]
}
```

### 3. Repository Configuration

Ask user for:
- GitHub repository (format: owner/repo)
- Sprint plan file name (suggest: `[product-name]-sprint.plan.md`)

Use StrReplace to update `.cursor/scripts/create-github-issue.sh`:

Line 9: `_SPRINT_PLAN=.cursor/plans/project-init/[sprint-plan-name]`
Line 13: `GITHUB_REPO=[owner]/[repo]`

### 4. Generate Technical Requirements

Create file: `.cursor/plans/project-init/[product-name]-technical-requirements.plan.md`

Use all collected responses to populate:
- Frontmatter with metadata
- All content sections
- Mermaid architecture diagram based on tech stack

### 5. Review with User

Present generated technical requirements document to user for review.

Ask: "Would you like to proceed with these requirements, or would you like to make changes?"

If changes needed, allow iteration on specific sections.

### 6. Handoff to Chief Architect

Once approved, notify Chief Architect:

```
@chief-architect

I have completed product discovery for [Product Name].

Technical Requirements: .cursor/plans/project-init/[filename].plan.md

Please review and validate:
1. Technical feasibility
2. Technology stack compatibility
3. Architecture patterns
4. Risk assessment

After validation, please update agent files with project-specific context.
```

### 7. Assess Research and Design Needs

After initial technical requirements are approved, determine which specialist agents to engage.

Use `.cursor/commands/engage-research-design.md` logic to assess:

**Automatic Triggers**:

Check for **Scientific Researcher** engagement:
- AI/ML indicators (keywords: AI, ML, models, neural, algorithm)
- Bioinformatics (keywords: genomics, sequence, molecular, biological)
- Complex domains (physics, chemistry, scientific computing)
- AWS Bedrock or SageMaker in services
- HuggingFace/LangChain in tech stack

Check for **Business Researcher** engagement:
- Regulated industries (healthcare, finance, legal, insurance)
- Business verticals (e-commerce, SaaS, marketplace, fintech, edtech)
- Compliance keywords (HIPAA, PCI-DSS, GDPR, SOX)
- Complex business models

Check for **Designer wireframe** scope:
- UI-heavy products (dashboard, complex forms, multi-step flows)
- B2C applications
- Consumer-facing interfaces
- User explicitly wants UI design

**Note**: Designer is ALWAYS engaged for system diagrams, regardless of product type.

**If triggers are unclear**, ask the user:

```json
{
  "title": "Specialist Support Assessment",
  "questions": [
    {
      "id": "research-needed",
      "prompt": "Your product may benefit from specialist research. Would you like deep domain expertise?",
      "options": [
        {"id": "scientific", "label": "Yes - Scientific/technical domain research (uses Claude MCP if configured)"},
        {"id": "business", "label": "Yes - Business vertical/market research (uses Claude MCP if configured)"},
        {"id": "both-research", "label": "Yes - Both scientific and business research"},
        {"id": "no-research", "label": "No - Standard validation is sufficient"}
      ],
      "allow_multiple": false
    },
    {
      "id": "ui-design-needed",
      "prompt": "Should we create UI wireframes for your product?",
      "options": [
        {"id": "yes-wireframes", "label": "Yes - Create wireframes for key user flows (uses Figma MCP if configured)"},
        {"id": "no-wireframes", "label": "No - System diagrams only (always included)"}
      ],
      "allow_multiple": false
    }
  ]
}
```

**Document engagement in technical requirements frontmatter**:

```yaml
specialist_agents:
  scientific_researcher:
    engaged: [true | false]
    mode: [mcp | collaboration | not_engaged]
    domain: "[Domain]"
  business_researcher:
    engaged: [true | false]
    mode: [mcp | collaboration | not_engaged]
    vertical: "[Vertical]"
  designer:
    system_diagrams: true
    ui_wireframes: [true | false]
    mode: [mcp | collaboration]
```

**If specialists engaged**:
1. Hand off technical requirements to researchers (if engaged)
2. Wait for research reports
3. Hand off to Designer (always)
4. Wait for system diagrams (Chief Architect reviews)
5. Wait for UI wireframes (if created, Product Manager reviews)
6. Consolidate findings into enhanced technical requirements
7. Update technical requirements document with:
   - Research findings sections
   - System architecture diagrams
   - UI wireframes (if created)
   - Design specifications (if created)

### 8. Handoff to Scrum Master

After Chief Architect validation and all specialist work complete:

```
@scrum-master

Technical requirements for [Product Name] have been validated.

Requirements File: .cursor/plans/project-init/[filename].plan.md

[If research conducted]:
Research reports:
- Scientific: [Path to report]
- Business: [Path to report]

[If design outputs]:
Design outputs:
- System diagrams: [Paths or Figma links]
- UI wireframes: [Paths or Figma links] (if created)

Please create sprint plan following sprint-plan-example.plan.md with:
- Ticket naming: FEAT-###, API-###, UI-###, DB-###, TEST-###, DOC-###, INFRA-###
- Table format from table-header.md
- Phases: Week 1 (Foundation), Week 2 (Core), Week 3+ (Features)
- Todos with ticket IDs
- Mermaid dependency graphs
- Review checkpoints

Please switch to Plan mode for sprint planning.
```

## Conditional Logic

- If `uses_template_defaults` = true → Skip Q2 (customization)
- If `data-needs` includes databases → Emphasize relevant options
- If AI features in core features → Highlight Bedrock/SageMaker options
- If scale = prototype → Recommend LocalStack only
- If scale = large → Recommend comprehensive AWS services

## Response Storage

Store all responses in session memory with keys:
- `uses_template_defaults`: boolean
- `tech_stack`: object with custom choices (if applicable)
- `target_users`: array
- `product_name`: string
- `product_overview`: string
- `problem_statement`: string
- `core_features`: array of {name, description, priority}
- `data_requirements`: array
- `aws_services`: object {compute, storage, ai}
- `external_integrations`: object {auth, payment, other}
- `scale`: string
- `performance`: string
- `ui_ux`: object {style, accessibility, dark_mode}
- `mcp_enabled`: boolean
- `mcp_services`: array (if partial)
- `github_repo`: string
- `sprint_plan_file`: string

## Error Handling

- If user provides unclear answers, ask clarifying questions
- If conflicting requirements detected, point out conflicts and ask for resolution
- If infeasible requirements (e.g., large scale with no cloud), explain constraints
- Always validate GitHub repo format before configuring scripts

## Output

Generate comprehensive technical requirements document and configure repository for sprint planning and issue tracking.
