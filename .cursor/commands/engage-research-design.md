# Engage Research and Design

This command assesses which specialist agents to engage based on product characteristics from the discovery phase.

## Purpose

After product discovery is complete, determine:
1. Should Scientific Researcher be engaged?
2. Should Business Researcher be engaged?
3. What scope should Designer have (system diagrams only vs. full UI)?

## Trigger Logic

### Scientific Researcher

Engage when ANY of these indicators are present:

**AI/ML Indicators**:
- Core features mention: AI, ML, machine learning, models, neural networks
- Algorithms: NLP, computer vision, recommendation systems, prediction
- Technology stack includes: HuggingFace, LangChain, AWS Bedrock, SageMaker
- Training, inference, or model deployment mentioned

**Bioinformatics Indicators**:
- Domain mentions: genomics, proteomics, sequence analysis, bioinformatics
- Biological data, DNA/RNA, proteins, molecular
- Clinical or research applications

**Complex Technical Domains**:
- Physics simulations, chemistry applications, mathematical modeling
- Scientific computing, signal processing
- Research-grade data analysis
- Complex algorithms or computational methods

**Explicit Request**:
- User explicitly asks for scientific research or domain validation

### Business Researcher

Engage when ANY of these indicators are present:

**Regulated Industries**:
- Healthcare (HIPAA, medical data, patient information, telemedicine)
- Finance (payments, transactions, PCI-DSS, banking, fintech)
- Legal (attorney-client, legal documents, compliance)
- Insurance (underwriting, claims, policy management)
- Education (FERPA, student data, COPPA)
- Government (FedRAMP, public sector, compliance)

**Business Verticals**:
- E-commerce (shopping cart, payments, product catalog, checkout)
- SaaS (subscriptions, multi-tenant, billing, accounts)
- Marketplace (multi-sided platform, vendors, buyers, escrow)
- Fintech (money movement, wallets, transactions, KYC/AML)
- Edtech (learning management, student records, assessments)
- Healthtech (EHR integration, health data, telehealth)

**Complex Business Models**:
- Multi-tenant architecture explicitly mentioned
- Complex billing or subscription models
- Regulatory compliance requirements mentioned
- Cross-border or data sovereignty concerns

**Explicit Request**:
- User explicitly asks for market research or business validation

### Designer Scope

**System Diagrams** (Always):
- ALWAYS engage Designer for system architecture diagrams
- Collaborates with Chief Architect
- Creates visual representations of technical requirements

**UI Wireframes** (Conditional):
Engage for wireframes when ANY of these are true:
- Dashboard application
- Complex forms or multi-step flows
- Consumer-facing B2C application
- Rich interactive UI explicitly mentioned
- Admin panels, data visualization, or reporting interfaces
- User explicitly requests UI design

## Assessment Process

### Step 1: Analyze Discovery Responses

Review the completed technical requirements for:
- Product description and problem statement
- Core features and functionality
- Technology stack choices
- Target users and use cases

### Step 2: Check Automatic Triggers

Run through trigger logic above to identify:
- Scientific Researcher needed? (Yes/No)
- Business Researcher needed? (Yes/No)
- Designer scope: System diagrams only or + UI wireframes?

### Step 3: Ask If Unclear

If triggers are not clearly met, ask the user:

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

### Step 4: Check MCP Availability

For each engaged agent, detect operational mode:

**Claude MCP** (for researchers):
```bash
if [ -f ".cursor/mcp/claude-research-server.json" ] && [ ! -z "$ANTHROPIC_API_KEY" ]; then
  MODE="mcp"  # Deep research via Claude API
else
  MODE="collaboration"  # Lightweight guidance via Cursor AI
fi
```

**Figma MCP** (for designer):
```bash
if [ -f ".cursor/mcp/figma-design-server.json" ] && [ ! -z "$FIGMA_ACCESS_TOKEN" ]; then
  MODE="mcp"  # Professional diagrams via Figma API
else
  MODE="collaboration"  # Text-based Mermaid diagrams
fi
```

### Step 5: Inform User of Mode

Communicate which mode will be used:

**MCP Mode Available**:
```
Scientific Researcher will use Claude MCP for deep domain research.
- Research depth: Comprehensive, literature-backed
- Credit usage: External Anthropic API credits
- Output: Detailed research report with citations
```

**Collaboration Mode**:
```
Scientific Researcher will provide lightweight domain guidance.
- Research depth: General knowledge, high-level
- Credit usage: Cursor AI credits
- Output: Concise guidance document
```

### Step 6: Generate Engagement Plan

Create structured engagement plan:

```yaml
specialist_engagement:
  scientific_researcher:
    engaged: [true | false]
    mode: [mcp | collaboration | not_engaged]
    rationale: [Why engaged or not]
    scope: [What will be researched]
  
  business_researcher:
    engaged: [true | false]
    mode: [mcp | collaboration | not_engaged]
    rationale: [Why engaged or not]
    scope: [What will be researched]
  
  designer:
    system_diagrams: true  # Always
    ui_wireframes: [true | false]
    mode: [mcp | collaboration]
    rationale: [Why wireframes are/aren't needed]
    scope: [What will be designed]
```

## Engagement Plan Output

Document the plan in technical requirements frontmatter:

```yaml
specialist_agents:
  scientific_researcher:
    engaged: true
    mode: mcp
    domain: "Machine Learning for Recommendation Systems"
  business_researcher:
    engaged: true
    mode: collaboration
    vertical: "E-commerce"
  designer:
    system_diagrams: true
    ui_wireframes: true
    mode: mcp
```

## Next Steps After Assessment

### If Researchers Engaged

1. Hand off technical requirements to Scientific Researcher (if engaged)
2. Hand off technical requirements to Business Researcher (if engaged)
3. Researchers work in parallel
4. Wait for research reports
5. Product Manager consolidates findings into enhanced requirements
6. Proceed to Designer engagement

### Designer Engagement (Always)

1. Hand off (enhanced) requirements to Designer
2. Designer creates system diagrams (always)
3. Chief Architect reviews and provides feedback
4. Designer iterates on diagrams
5. Designer creates UI wireframes (if scope includes it)
6. Product Manager reviews wireframes for feature alignment
7. Final design outputs added to technical requirements

### Handoff to Chief Architect

1. Complete technical requirements with:
   - Research reports (if researchers engaged)
   - System diagrams (always)
   - UI wireframes (if created)
   - Design specifications (if created, MCP mode)
2. Chief Architect validates complete package
3. Proceed to Scrum Master for sprint planning

## Examples

### Example 1: AI-Powered Healthcare App

**Product**: AI diagnostic assistant for radiologists

**Triggers**:
- AI/ML: Neural networks for image classification
- Healthcare: Medical imaging, patient data, HIPAA

**Assessment**:
- Scientific Researcher: YES (AI/ML domain)
- Business Researcher: YES (Healthcare vertical)
- Designer Wireframes: YES (Dashboard for radiologists)

**Engagement Plan**:
```yaml
scientific_researcher:
  engaged: true
  mode: mcp
  domain: "Medical Image Analysis with Deep Learning"
business_researcher:
  engaged: true
  mode: mcp
  vertical: "Healthcare - HIPAA Compliance"
designer:
  system_diagrams: true
  ui_wireframes: true
```

### Example 2: Simple Task Management App

**Product**: Team task tracker with boards and lists

**Triggers**:
- No AI/ML, no complex domain
- No regulated industry
- Standard SaaS application

**Assessment**:
- Scientific Researcher: NO (no complex domain)
- Business Researcher: NO (standard SaaS, no specific vertical)
- Designer Wireframes: YES (UI-heavy dashboard)

**Engagement Plan**:
```yaml
scientific_researcher:
  engaged: false
business_researcher:
  engaged: false
designer:
  system_diagrams: true
  ui_wireframes: true
  mode: collaboration  # Text-based is sufficient
```

### Example 3: Fintech Payment Platform

**Product**: P2P payment platform with instant transfers

**Triggers**:
- Fintech: Money movement, transactions
- Regulated: Financial services, compliance

**Assessment**:
- Scientific Researcher: NO (no complex technical domain)
- Business Researcher: YES (Fintech vertical, regulations)
- Designer Wireframes: YES (Consumer-facing B2C app)

**Engagement Plan**:
```yaml
scientific_researcher:
  engaged: false
business_researcher:
  engaged: true
  mode: mcp
  vertical: "Fintech - Money Transmission and KYC/AML"
designer:
  system_diagrams: true
  ui_wireframes: true
```

## Integration with Product Development

1. Product Manager completes discovery → Technical requirements draft
2. **This Command** → Assess specialist needs
3. Engage specialists based on assessment
4. Consolidate findings into enhanced requirements
5. Handoff to Chief Architect for validation
6. Chief Architect collaborates with Designer on diagrams
7. Proceed to Scrum Master for sprint planning

## Related Documentation

- [Scientific Researcher Agent](.cursor/agents/scientific-researcher.md)
- [Business Researcher Agent](.cursor/agents/business-researcher.md)
- [Designer Agent](.cursor/agents/designer.md)
- [Researcher Collaboration Protocol](.cursor/protocols/researcher-collaboration.md)
- [Designer Collaboration Protocol](.cursor/protocols/designer-collaboration.md)
- [Claude MCP Setup](.cursor/docs/mcp-setup-claude.md)
- [Figma MCP Setup](.cursor/docs/mcp-setup-figma.md)

## Notes

- Assessment should be quick and decisive
- When in doubt, engage specialists (can always scope down)
- MCP mode detection is automatic at runtime
- Designer is ALWAYS engaged for system diagrams
- Communicate mode and credit implications to user
- Engagement plan becomes part of technical requirements metadata
