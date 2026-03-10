---
ticket: BE-002
title: Implement Bedrock LLM Wrapper
owner: Backend Engineer
points: 5
dependencies: [BE-001, INFRA-002]
phase: Backend AI Services
---

# BE-002: Implement Bedrock LLM Wrapper

## Description

Create a LangChain custom LLM class that wraps AWS Bedrock. Support both standard invocation and streaming responses. Handle authentication, rate limiting, and errors gracefully.

## Acceptance Criteria

- [ ] Custom LangChain LLM class for Bedrock
- [ ] Support for streaming responses
- [ ] Error handling for rate limits and timeouts
- [ ] Unit tests with mocked boto3 calls
- [ ] Integration tests with LocalStack

## Technical Details

### Bedrock LLM Implementation

Create `backend/services/ai/bedrock_llm.py`:

```python
from typing import Any, Iterator, Optional
from langchain_core.language_models.llms import LLM
from langchain_core.callbacks import CallbackManagerForLLMRun
import boto3
import json
from core.config import settings
from core.aws_client import get_bedrock_client

class BedrockLLM(LLM):
    """Custom LangChain LLM for AWS Bedrock fine-tuned models."""
    
    model_id: str = settings.bedrock_model_id
    max_tokens: int = 2048
    temperature: float = 0.7
    
    @property
    def _llm_type(self) -> str:
        return "bedrock"
    
    def _call(
        self,
        prompt: str,
        stop: Optional[list[str]] = None,
        run_manager: Optional[CallbackManagerForLLMRun] = None,
        **kwargs: Any,
    ) -> str:
        """Invoke Bedrock model and return response."""
        client = get_bedrock_client()
        
        body = json.dumps({
            "prompt": prompt,
            "max_tokens": self.max_tokens,
            "temperature": self.temperature,
            "stop_sequences": stop or [],
        })
        
        try:
            response = client.invoke_model(
                modelId=self.model_id,
                body=body,
                contentType="application/json",
                accept="application/json"
            )
            
            response_body = json.loads(response["body"].read())
            return response_body.get("completion", "")
            
        except client.exceptions.ThrottlingException:
            raise Exception("Rate limit exceeded. Please try again later.")
        except client.exceptions.ValidationException as e:
            raise ValueError(f"Invalid request: {str(e)}")
        except Exception as e:
            raise Exception(f"Bedrock invocation failed: {str(e)}")
    
    def _stream(
        self,
        prompt: str,
        stop: Optional[list[str]] = None,
        run_manager: Optional[CallbackManagerForLLMRun] = None,
        **kwargs: Any,
    ) -> Iterator[str]:
        """Stream Bedrock model responses token by token."""
        client = get_bedrock_client()
        
        body = json.dumps({
            "prompt": prompt,
            "max_tokens": self.max_tokens,
            "temperature": self.temperature,
            "stop_sequences": stop or [],
            "stream": True,
        })
        
        try:
            response = client.invoke_model_with_response_stream(
                modelId=self.model_id,
                body=body,
                contentType="application/json",
                accept="application/json"
            )
            
            for event in response["body"]:
                chunk = json.loads(event["chunk"]["bytes"])
                if token := chunk.get("token"):
                    if run_manager:
                        run_manager.on_llm_new_token(token)
                    yield token
                    
        except Exception as e:
            raise Exception(f"Streaming failed: {str(e)}")
```

### Unit Tests

Create `backend/tests/unit/test_bedrock_llm.py`:

```python
import pytest
from unittest.mock import Mock, patch
from services.ai.bedrock_llm import BedrockLLM

@pytest.fixture
def mock_bedrock_client():
    with patch("services.ai.bedrock_llm.get_bedrock_client") as mock:
        client = Mock()
        mock.return_value = client
        yield client

def test_bedrock_llm_call(mock_bedrock_client):
    """Test standard LLM invocation."""
    mock_bedrock_client.invoke_model.return_value = {
        "body": Mock(read=lambda: b'{"completion": "Test response"}')
    }
    
    llm = BedrockLLM()
    response = llm("Test prompt")
    
    assert response == "Test response"
    mock_bedrock_client.invoke_model.assert_called_once()

def test_bedrock_llm_handles_throttling(mock_bedrock_client):
    """Test rate limit error handling."""
    mock_bedrock_client.invoke_model.side_effect = \
        mock_bedrock_client.exceptions.ThrottlingException(
            {"Error": {"Code": "ThrottlingException"}}, "test"
        )
    
    llm = BedrockLLM()
    
    with pytest.raises(Exception, match="Rate limit exceeded"):
        llm("Test prompt")

def test_bedrock_llm_streaming(mock_bedrock_client):
    """Test streaming responses."""
    mock_bedrock_client.invoke_model_with_response_stream.return_value = {
        "body": [
            {"chunk": {"bytes": b'{"token": "Hello"}'}},
            {"chunk": {"bytes": b'{"token": " world"}'}},
        ]
    }
    
    llm = BedrockLLM()
    tokens = list(llm.stream("Test prompt"))
    
    assert tokens == ["Hello", " world"]
```

## Files to Create/Modify

- `backend/services/ai/bedrock_llm.py` - LLM implementation
- `backend/tests/unit/test_bedrock_llm.py` - Unit tests
- `backend/tests/integration/test_bedrock_integration.py` - LocalStack integration tests

## Testing

### Unit Tests
```bash
cd backend
pytest tests/unit/test_bedrock_llm.py -v
```

### Integration Test with LocalStack
```bash
# Start LocalStack
docker-compose up localstack

# Run integration tests
pytest tests/integration/test_bedrock_integration.py -v
```

## Definition of Done

- [ ] BedrockLLM class implements LangChain LLM interface
- [ ] Streaming functionality works correctly
- [ ] Error handling for throttling, validation, timeouts
- [ ] Unit tests achieve >80% coverage
- [ ] Integration tests pass with LocalStack
- [ ] Code reviewed and approved
- [ ] Documentation includes usage examples
