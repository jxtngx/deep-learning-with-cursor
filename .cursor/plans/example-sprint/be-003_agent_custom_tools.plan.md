---
ticket: BE-003
title: Create Agent with Custom Tools
owner: Backend Engineer
points: 5
dependencies: [BE-002]
phase: Backend AI Services
---

# BE-003: Create Agent with Custom Tools

## Description

Build a LangChain agent using the ReAct pattern with 2-3 custom tools (calculator, knowledge base search). The agent should intelligently select tools based on user queries.

## Acceptance Criteria

- [ ] LangChain agent using ReAct pattern
- [ ] 2-3 custom tools implemented (calculator, knowledge base, datetime)
- [ ] Agent selects appropriate tool based on query
- [ ] FastAPI endpoint for chat interactions
- [ ] Integration tests demonstrating multi-step reasoning

## Technical Details

### Custom Tools Implementation

Create `backend/services/ai/tools.py`:

```python
from langchain.tools import Tool
from datetime import datetime
import operator

def calculator(expression: str) -> str:
    """
    Evaluate mathematical expressions.
    Example: "2 + 2" returns "4"
    """
    try:
        # Simple safe eval for basic math
        allowed = {
            "abs": abs, "round": round,
            **{op: getattr(operator, op) for op in ["add", "sub", "mul", "truediv"]}
        }
        result = eval(expression, {"__builtins__": {}}, allowed)
        return str(result)
    except Exception as e:
        return f"Error: {str(e)}"

def get_current_datetime(query: str) -> str:
    """
    Get current date and time.
    Example: "what time is it?" returns current datetime
    """
    now = datetime.now()
    return now.strftime("%Y-%m-%d %H:%M:%S")

def knowledge_base_search(query: str) -> str:
    """
    Search knowledge base for domain-specific information.
    This is a mock implementation - replace with real vector DB.
    """
    knowledge = {
        "company": "We are an AI startup building intelligent assistants.",
        "products": "Our main product is an AI chat assistant powered by LangChain.",
        "tech stack": "We use Next.js, FastAPI, LangChain, and AWS Bedrock.",
    }
    
    query_lower = query.lower()
    for key, value in knowledge.items():
        if key in query_lower:
            return value
    
    return "I don't have information about that in my knowledge base."

# Create LangChain Tool objects
calculator_tool = Tool(
    name="Calculator",
    func=calculator,
    description="Useful for performing mathematical calculations. Input should be a valid math expression like '2 + 2' or '10 * 5'."
)

datetime_tool = Tool(
    name="CurrentDateTime",
    func=get_current_datetime,
    description="Get the current date and time. Use this when user asks about the current time or date."
)

knowledge_tool = Tool(
    name="KnowledgeBase",
    func=knowledge_base_search,
    description="Search the knowledge base for company information, products, or technical details. Input should be a search query."
)
```

### Agent Implementation

Create `backend/services/ai/agent.py`:

```python
from langchain.agents import create_react_agent, AgentExecutor
from langchain.prompts import PromptTemplate
from .bedrock_llm import BedrockLLM
from .tools import calculator_tool, datetime_tool, knowledge_tool

AGENT_PROMPT = """You are a helpful AI assistant. Use the available tools to answer questions accurately.

You have access to the following tools:

{tools}

Use the following format:

Question: the input question you must answer
Thought: you should always think about what to do
Action: the action to take, should be one of [{tool_names}]
Action Input: the input to the action
Observation: the result of the action
... (this Thought/Action/Action Input/Observation can repeat N times)
Thought: I now know the final answer
Final Answer: the final answer to the original input question

Begin!

Question: {input}
Thought:{agent_scratchpad}
"""

def create_chat_agent() -> AgentExecutor:
    """Create a ReAct agent with custom tools."""
    llm = BedrockLLM()
    
    tools = [calculator_tool, datetime_tool, knowledge_tool]
    
    prompt = PromptTemplate.from_template(AGENT_PROMPT)
    
    agent = create_react_agent(
        llm=llm,
        tools=tools,
        prompt=prompt
    )
    
    agent_executor = AgentExecutor(
        agent=agent,
        tools=tools,
        verbose=True,
        max_iterations=5,
        handle_parsing_errors=True,
    )
    
    return agent_executor
```

### Chat API Endpoint

Create `backend/api/routes/chat.py`:

```python
from fastapi import APIRouter, HTTPException
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from services.ai.agent import create_chat_agent
import json

router = APIRouter()

class ChatRequest(BaseModel):
    message: str
    stream: bool = True

class ChatResponse(BaseModel):
    response: str
    steps: list[dict] = []

agent_executor = create_chat_agent()

@router.post("/chat")
async def chat(request: ChatRequest):
    """Handle chat requests with LangChain agent."""
    try:
        if request.stream:
            async def generate():
                response = agent_executor.invoke({"input": request.message})
                # Stream the response token by token
                for char in response["output"]:
                    yield json.dumps({"token": char}) + "\n"
            
            return StreamingResponse(
                generate(),
                media_type="application/x-ndjson"
            )
        else:
            response = agent_executor.invoke({"input": request.message})
            return ChatResponse(
                response=response["output"],
                steps=response.get("intermediate_steps", [])
            )
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
```

## Files to Create/Modify

- `backend/services/ai/tools.py` - Custom tool implementations
- `backend/services/ai/agent.py` - ReAct agent setup
- `backend/api/routes/chat.py` - Chat endpoint
- `backend/tests/integration/test_agent.py` - Agent integration tests

## Testing

### Integration Tests

Create `backend/tests/integration/test_agent.py`:

```python
import pytest
from services.ai.agent import create_chat_agent

@pytest.fixture
def agent():
    return create_chat_agent()

def test_agent_calculator_tool(agent):
    """Test agent uses calculator for math questions."""
    response = agent.invoke({"input": "What is 25 * 4?"})
    assert "100" in response["output"]

def test_agent_datetime_tool(agent):
    """Test agent uses datetime tool for time questions."""
    response = agent.invoke({"input": "What is the current date?"})
    assert response["output"]  # Should contain date

def test_agent_knowledge_tool(agent):
    """Test agent uses knowledge base for company questions."""
    response = agent.invoke({"input": "What is your tech stack?"})
    assert "Next.js" in response["output"] or "FastAPI" in response["output"]

def test_agent_multi_step_reasoning(agent):
    """Test agent can chain multiple tools."""
    response = agent.invoke({
        "input": "Calculate 10 + 5, then tell me what time it is"
    })
    assert response["output"]
    # Should use both calculator and datetime tools
```

### Manual Testing

```bash
# Start backend
cd backend && uvicorn main:app --reload

# Test endpoint
curl -X POST http://localhost:8000/api/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "What is 10 * 5?", "stream": false}'
```

## Definition of Done

- [ ] Agent successfully uses ReAct pattern
- [ ] All three tools implemented and functional
- [ ] Agent selects correct tool based on query
- [ ] Chat endpoint responds correctly
- [ ] Integration tests pass for all tools
- [ ] Multi-step reasoning demonstrated in tests
- [ ] Code reviewed and approved
- [ ] Logging added for agent decisions
