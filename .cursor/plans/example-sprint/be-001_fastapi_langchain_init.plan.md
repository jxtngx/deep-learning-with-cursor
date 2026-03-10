---
ticket: BE-001
title: Initialize FastAPI with LangChain
owner: Backend Engineer
points: 3
dependencies: [INFRA-002]
phase: Backend AI Services
---

# BE-001: Initialize FastAPI with LangChain

## Description

Create the FastAPI application structure with LangChain dependencies. Set up basic routing, health check endpoint, and project organization for AI services.

## Acceptance Criteria

- [ ] FastAPI app initialized with proper structure
- [ ] LangChain and related dependencies installed
- [ ] Health check endpoint responds correctly
- [ ] CORS configured for frontend integration
- [ ] Dev server runs without errors

## Technical Details

### Project Structure

```
backend/
├── main.py
├── core/
│   ├── __init__.py
│   ├── config.py
│   └── aws_client.py
├── api/
│   ├── __init__.py
│   └── routes/
│       ├── __init__.py
│       ├── health.py
│       └── chat.py
├── services/
│   ├── __init__.py
│   └── ai/
│       ├── __init__.py
│       ├── bedrock_llm.py
│       ├── agent.py
│       └── tools.py
└── tests/
    ├── unit/
    └── integration/
```

### Dependencies

Update `backend/pyproject.toml`:

```toml
[project]
dependencies = [
    "fastapi>=0.109.0",
    "uvicorn[standard]>=0.27.0",
    "langchain>=0.1.0",
    "langchain-community>=0.0.20",
    "boto3>=1.34.0",
    "pydantic>=2.6.0",
    "pydantic-settings>=2.1.0",
    "python-dotenv>=1.0.0",
]
```

### FastAPI Application

Create `backend/main.py`:

```python
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.routes import health, chat

app = FastAPI(
    title="AI Chat Assistant",
    description="Agentic AI chat using LangChain and AWS Bedrock",
    version="1.0.0"
)

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routes
app.include_router(health.router, prefix="/api", tags=["health"])
app.include_router(chat.router, prefix="/api", tags=["chat"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

### Health Check Endpoint

Create `backend/api/routes/health.py`:

```python
from fastapi import APIRouter

router = APIRouter()

@router.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "service": "ai-chat-backend",
        "version": "1.0.0"
    }
```

## Files to Create/Modify

- `backend/main.py` - FastAPI application
- `backend/pyproject.toml` - Add dependencies
- `backend/api/routes/health.py` - Health check
- `backend/api/routes/chat.py` - Chat endpoint stub
- `backend/services/ai/__init__.py` - AI services package

## Testing

1. Install dependencies: `cd backend && pip install -e .`
2. Run dev server: `uvicorn main:app --reload`
3. Test health endpoint: `curl http://localhost:8000/api/health`
4. Verify response: `{"status":"healthy","service":"ai-chat-backend","version":"1.0.0"}`

## Development Commands

Add to `backend/Makefile`:

```makefile
.PHONY: install dev test

install:
	pip install -e .

dev:
	uvicorn main:app --reload --host 0.0.0.0 --port 8000

test:
	pytest tests/
```

## Definition of Done

- [ ] FastAPI app runs without errors
- [ ] Health check endpoint returns 200 OK
- [ ] LangChain imports successfully
- [ ] CORS configured for frontend
- [ ] Code reviewed and approved
- [ ] Documentation updated
