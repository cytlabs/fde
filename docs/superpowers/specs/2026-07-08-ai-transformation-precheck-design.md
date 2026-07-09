# AI Transformation Precheck Skill Design

## Objective

Create a standalone customer-facing skill that helps enterprise users prepare for conversations with FDEs, AI consultants, or implementation teams. The skill should guide users through business self-diagnosis, workflow inventory, AI opportunity identification, prioritization, and preparation of a structured pre-consultation brief.

## Scope

The skill is a pre-consultation assistant. It does not replace FDE discovery, make final implementation promises, or jump directly to tool or architecture recommendations.

## Structure

- `skills/ai-transformation-precheck/SKILL.md`: core trigger description, modes, workflow, judging rules, output requirements, and quality checklist.
- `skills/ai-transformation-precheck/references/diagnosis-framework.md`: customer-side diagnosis questions and opportunity criteria.
- `skills/ai-transformation-precheck/references/output-formats.md`: fixed output templates for each mode.
- `skills/ai-transformation-precheck/references/examples.md`: representative examples across sales, customer service, finance, HR, and delivery.
- `skills/ai-transformation-precheck/agents/openai.yaml`: UI metadata and default prompt.

## Modes

- Enterprise self-diagnosis
- Business workflow inventory
- Single-scenario deep dive
- AI opportunity prioritization
- FDE pre-consultation brief generation

## Relationship To Existing Skill

`ai-transformation-precheck` is used by enterprise customers before speaking with an FDE. `fde-customer-discovery` is used by FDEs after receiving customer context to conduct deeper discovery, validate pain points, and scope MVPs.

## Success Criteria

- A customer with vague AI transformation intent can produce a clearer pre-consultation brief.
- The output distinguishes business goals, current workflows, pain points, data/tool readiness, candidate AI opportunities, and risks.
- The skill avoids premature technical promises.
- FDEs can use the resulting material as input for deeper discovery.
