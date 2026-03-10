---
ticket: TEST-001
title: Integration Tests for Agent
owner: Test Developer
points: 3
dependencies: [BE-003]
phase: Testing & Polish
---

# TEST-001: Integration Tests for Agent

## Description

Write comprehensive integration tests for the LangChain agent with mocked Bedrock responses. Test tool selection, multi-step reasoning, and error handling.

## Acceptance Criteria

- [ ] Integration tests for all agent tools
- [ ] Multi-step reasoning scenarios tested
- [ ] Error handling tests (invalid inputs, timeouts)
- [ ] Mock Bedrock responses using LocalStack or fixtures
- [ ] Test coverage >80% for agent module
- [ ] Tests run in CI/CD pipeline

## Technical Details

### Test Structure

```
backend/tests/integration/
├── conftest.py
├── test_agent.py
├── test_agent_tools.py
└── fixtures/
    └── bedrock_responses.json
```

### Fixtures Setup

Create `backend/tests/integration/conftest.py`:

```python
import pytest
from unittest.mock import Mock, patch
from services.ai.agent import create_chat_agent

@pytest.fixture
def mock_bedrock_responses():
    """Mock Bedrock responses for agent testing."""
    return {
        "calculator": {
            "output": "The answer is 100",
            "thought": "I need to use the Calculator tool"
        },
        "datetime": {
            "output": "The current time is 2024-03-15 14:30:00",
            "thought": "I need to use the CurrentDateTime tool"
        },
        "knowledge": {
            "output": "We use Next.js, FastAPI, LangChain, and AWS Bedrock",
            "thought": "I need to use the KnowledgeBase tool"
        }
    }

@pytest.fixture
def agent_with_mocked_llm(mock_bedrock_responses):
    """Create agent with mocked LLM responses."""
    with patch("services.ai.bedrock_llm.BedrockLLM._call") as mock_call:
        # Configure mock to return appropriate responses
        mock_call.side_effect = lambda prompt, **kwargs: \
            mock_bedrock_responses.get("calculator", {}).get("output", "")
        
        agent = create_chat_agent()
        yield agent, mock_call
```

### Agent Integration Tests

Create `backend/tests/integration/test_agent.py`:

```python
import pytest
from services.ai.agent import create_chat_agent

@pytest.mark.integration
def test_agent_calculator_tool():
    """Test agent correctly uses calculator for math questions."""
    agent = create_chat_agent()
    
    response = agent.invoke({
        "input": "What is 25 multiplied by 4?"
    })
    
    assert response is not None
    assert "100" in response["output"]
    # Verify calculator tool was used
    assert any("Calculator" in str(step) for step in response.get("intermediate_steps", []))

@pytest.mark.integration
def test_agent_datetime_tool():
    """Test agent uses datetime tool for time questions."""
    agent = create_chat_agent()
    
    response = agent.invoke({
        "input": "What is the current date and time?"
    })
    
    assert response is not None
    # Should contain year in format YYYY
    assert any(str(year) in response["output"] for year in range(2024, 2030))

@pytest.mark.integration
def test_agent_knowledge_tool():
    """Test agent uses knowledge base for company questions."""
    agent = create_chat_agent()
    
    response = agent.invoke({
        "input": "What technologies does the company use?"
    })
    
    assert response is not None
    assert any(tech in response["output"] for tech in ["Next.js", "FastAPI", "LangChain"])

@pytest.mark.integration
def test_agent_multi_step_reasoning():
    """Test agent can chain multiple tools in sequence."""
    agent = create_chat_agent()
    
    response = agent.invoke({
        "input": "Calculate 15 + 25, then tell me what time it is"
    })
    
    assert response is not None
    # Should use both calculator and datetime
    steps = response.get("intermediate_steps", [])
    tools_used = [str(step) for step in steps]
    assert any("Calculator" in tool for tool in tools_used)
    assert any("CurrentDateTime" in tool for tool in tools_used)

@pytest.mark.integration
def test_agent_handles_invalid_input():
    """Test agent handles invalid calculator input gracefully."""
    agent = create_chat_agent()
    
    response = agent.invoke({
        "input": "Calculate the square root of negative one million"
    })
    
    assert response is not None
    # Should still provide a response, not crash
    assert len(response["output"]) > 0

@pytest.mark.integration
def test_agent_max_iterations():
    """Test agent respects max iterations limit."""
    agent = create_chat_agent()
    
    # Query that might cause infinite loop without limit
    response = agent.invoke({
        "input": "Keep calculating numbers forever"
    })
    
    assert response is not None
    # Should have stopped at max_iterations
    assert len(response.get("intermediate_steps", [])) <= 5

@pytest.mark.integration
def test_agent_unknown_question():
    """Test agent handles questions outside tool capabilities."""
    agent = create_chat_agent()
    
    response = agent.invoke({
        "input": "What is the weather like today?"
    })
    
    assert response is not None
    # Should indicate it doesn't have that capability
    assert any(word in response["output"].lower() 
              for word in ["don't", "cannot", "unable", "not", "sorry"])
```

### Tool-Specific Tests

Create `backend/tests/integration/test_agent_tools.py`:

```python
import pytest
from services.ai.tools import calculator, get_current_datetime, knowledge_base_search

def test_calculator_basic_operations():
    """Test calculator with basic math operations."""
    assert "4" in calculator("2 + 2")
    assert "10" in calculator("5 * 2")
    assert "3" in calculator("9 / 3")
    assert "5" in calculator("10 - 5")

def test_calculator_complex_expression():
    """Test calculator with complex expressions."""
    result = calculator("(10 + 5) * 2")
    assert "30" in result

def test_calculator_error_handling():
    """Test calculator handles invalid expressions."""
    result = calculator("invalid expression")
    assert "Error" in result

def test_datetime_returns_valid_format():
    """Test datetime tool returns properly formatted date."""
    result = get_current_datetime("")
    # Should match YYYY-MM-DD HH:MM:SS format
    assert len(result.split("-")) == 3
    assert len(result.split(":")) == 3

def test_knowledge_base_search():
    """Test knowledge base returns relevant information."""
    result = knowledge_base_search("company")
    assert "AI" in result or "startup" in result
    
    result = knowledge_base_search("products")
    assert "chat" in result.lower()
    
    result = knowledge_base_search("tech stack")
    assert "Next.js" in result or "FastAPI" in result

def test_knowledge_base_unknown_query():
    """Test knowledge base handles unknown queries."""
    result = knowledge_base_search("random unknown topic")
    assert "don't have information" in result.lower()
```

## Files to Create

- `backend/tests/integration/conftest.py` - Test fixtures
- `backend/tests/integration/test_agent.py` - Agent integration tests
- `backend/tests/integration/test_agent_tools.py` - Tool-specific tests
- `backend/pytest.ini` - pytest configuration with markers

### pytest Configuration

Create `backend/pytest.ini`:

```ini
[pytest]
markers =
    integration: marks tests as integration tests (deselect with '-m "not integration"')
    slow: marks tests as slow (deselect with '-m "not slow"')

testpaths = tests
python_files = test_*.py
python_classes = Test*
python_functions = test_*
```

## Running Tests

### All Tests
```bash
cd backend
pytest tests/integration/ -v
```

### Specific Test File
```bash
pytest tests/integration/test_agent.py -v
```

### With Coverage
```bash
pytest tests/integration/ --cov=services.ai --cov-report=html
```

### Skip Slow Tests
```bash
pytest tests/integration/ -m "not slow" -v
```

## CI/CD Integration

Add to `.github/workflows/test.yml`:

```yaml
name: Integration Tests

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    
    services:
      localstack:
        image: localstack/localstack
        env:
          SERVICES: bedrock
        ports:
          - 4566:4566
    
    steps:
      - uses: actions/checkout@v3
      
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'
      
      - name: Install dependencies
        run: |
          cd backend
          pip install -e .
          pip install pytest pytest-cov
      
      - name: Run integration tests
        run: |
          cd backend
          pytest tests/integration/ --cov=services.ai --cov-report=xml
      
      - name: Upload coverage
        uses: codecov/codecov-action@v3
```

## Definition of Done

- [ ] All agent tools have integration tests
- [ ] Multi-step reasoning tested
- [ ] Error handling scenarios covered
- [ ] Test coverage >80% for agent module
- [ ] Tests pass in CI/CD pipeline
- [ ] Mocked Bedrock responses work correctly
- [ ] Code reviewed and approved
- [ ] Documentation includes running tests
