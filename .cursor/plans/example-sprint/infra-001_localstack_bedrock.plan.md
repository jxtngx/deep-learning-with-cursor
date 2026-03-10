---
ticket: INFRA-001
title: Setup LocalStack with Bedrock
owner: AWS Engineer
points: 3
dependencies: []
phase: Infrastructure & Setup
---

# INFRA-001: Setup LocalStack with Bedrock

## Description

Configure LocalStack to emulate AWS Bedrock services for local development. This enables developers to test the AI chat application without requiring real AWS credentials or incurring cloud costs.

## Acceptance Criteria

- [ ] LocalStack service added to docker-compose.yml
- [ ] Bedrock service enabled in LocalStack configuration
- [ ] Init script creates mock fine-tuned model endpoint
- [ ] Documentation for starting LocalStack locally
- [ ] Can successfully connect to LocalStack Bedrock endpoint

## Technical Details

### Docker Compose Configuration

Add LocalStack service to `docker-compose.yml`:

```yaml
services:
  localstack:
    image: localstack/localstack:latest
    container_name: localstack
    ports:
      - "4566:4566"
      - "4571:4571"
    environment:
      - SERVICES=bedrock,secretsmanager,s3
      - DEBUG=1
      - DOCKER_HOST=unix:///var/run/docker.sock
      - AWS_DEFAULT_REGION=us-east-1
    volumes:
      - "./infrastructure/localstack/init:/etc/localstack/init/ready.d"
      - "/var/run/docker.sock:/var/run/docker.sock"
```

### Init Script

Create `infrastructure/localstack/init/bedrock-init.sh`:

```bash
#!/bin/bash
echo "Initializing Bedrock mock models..."

# Create mock fine-tuned model
awslocal bedrock put-model-invocation-logging-configuration \
  --logging-config '{"cloudWatchConfig":{"logGroupName":"/aws/bedrock/model-invocations"}}'

echo "Bedrock initialization complete"
```

## Files to Create/Modify

- `docker-compose.yml` - Add LocalStack service
- `infrastructure/localstack/init/bedrock-init.sh` - Bedrock initialization
- `README.md` - Add LocalStack setup instructions
- `.env.example` - Add LocalStack environment variables

## Testing

1. Run `docker-compose up localstack`
2. Verify service is running: `curl http://localhost:4566/_localstack/health`
3. Check Bedrock service is available in health check response

## Documentation Updates

Add to README.md:

```markdown
## Local Development with LocalStack

Start LocalStack services:
```bash
docker-compose up localstack
```

Verify services are running:
```bash
curl http://localhost:4566/_localstack/health
```
```

## Definition of Done

- [ ] Code reviewed and approved
- [ ] LocalStack starts without errors
- [ ] Health check shows Bedrock service available
- [ ] Documentation updated in README
- [ ] Team can run LocalStack locally
