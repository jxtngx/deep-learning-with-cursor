---
name: ""
overview: ""
todos: []
isProject: false
---

# INFRA-002: Configure AWS Bedrock Connection

## Description

Set up AWS SDK configuration and environment variables to connect to Bedrock (via LocalStack locally, real AWS in production). Configure IAM policies and authentication.

## Acceptance Criteria

- AWS SDK configured for both LocalStack and production
- Environment variables for Bedrock endpoint and credentials
- IAM policy JSON for Bedrock access
- Configuration module in backend supports environment switching
- Secrets stored in .env (not committed)

## Technical Details

### Environment Configuration

Create `.env.example`:

```bash
# AWS Configuration
AWS_REGION=us-east-1
AWS_ACCESS_KEY_ID=test
AWS_SECRET_ACCESS_KEY=test
BEDROCK_ENDPOINT_URL=http://localhost:4566

# Model Configuration
BEDROCK_MODEL_ID=custom-model-v1
BEDROCK_MODEL_ARN=arn:aws:bedrock:us-east-1:123456789012:model/custom-model-v1
```

### Backend Configuration Module

Create `backend/core/config.py`:

```python
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    aws_region: str = "us-east-1"
    aws_access_key_id: str
    aws_secret_access_key: str
    bedrock_endpoint_url: str | None = None
    bedrock_model_id: str
    
    class Config:
        env_file = ".env"

settings = Settings()
```

### IAM Policy

Create `infrastructure/aws/policies/bedrock-access.json`:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "bedrock:InvokeModel",
        "bedrock:InvokeModelWithResponseStream"
      ],
      "Resource": "arn:aws:bedrock:*:*:model/*"
    }
  ]
}
```

## Files to Create/Modify

- `.env.example` - Environment variable template
- `backend/core/config.py` - Configuration management
- `backend/core/aws_client.py` - AWS client factory
- `infrastructure/aws/policies/bedrock-access.json` - IAM policy
- `README.md` - Configuration instructions

## Testing

1. Copy `.env.example` to `.env`
2. Run backend with LocalStack endpoint
3. Verify AWS client connects to LocalStack
4. Test configuration with real AWS (staging)

## Environment Switching Logic

```python
# backend/core/aws_client.py
import boto3
from .config import settings

def get_bedrock_client():
    config = {
        "region_name": settings.aws_region,
        "aws_access_key_id": settings.aws_access_key_id,
        "aws_secret_access_key": settings.aws_secret_access_key,
    }
    
    # Use LocalStack endpoint if configured
    if settings.bedrock_endpoint_url:
        config["endpoint_url"] = settings.bedrock_endpoint_url
    
    return boto3.client("bedrock-runtime", **config)
```

## Definition of Done

- Configuration module loads environment variables
- AWS client connects to LocalStack in development
- IAM policy documented for production deployment
- README updated with configuration instructions
- No credentials committed to git
- Code reviewed and approved

