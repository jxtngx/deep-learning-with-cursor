<!-- Copyright 2025 jxtngx | Apache 2.0 License | https://github.com/jxtngx/claude-code-pytorch -->

# Named Entity Recognition

I need to implement a Named Entity Recognition system that can identify PER, ORG, LOC, and MISC entities using a transformer with token classification head. The system should use BIO or BILOU labeling schemes and process sentences in under 10ms. I need entity-level F1 above 0.9, with support for nested entities and cross-lingual capabilities. Please build the complete NER pipeline including CRF layer consideration, entity linking, active learning setup, and visualization tools for the extracted entities.

## Requirements

- Architecture: Token classification head on transformer
- Entity types: PER, ORG, LOC, MISC minimum
- Sequence labeling: BIO or BILOU scheme
- Inference speed: <10ms per sentence

## Success Criteria

- Entity-level F1 >0.9
- Nested entity support
- Cross-lingual capability
- Active learning setup

## Deliverables

- NER model with visualization
- Entity extraction pipeline
- Evaluation per entity type
- Integration with knowledge base
