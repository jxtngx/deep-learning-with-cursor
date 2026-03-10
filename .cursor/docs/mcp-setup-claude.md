# Claude MCP Setup Guide

This guide explains how to set up the Claude MCP server for the Scientific and Business Researcher agents.

## Overview

The Claude MCP server enables deep research capabilities by connecting to Anthropic's Claude API, allowing researchers to access comprehensive domain knowledge without consuming Cursor AI credits for research work.

## Prerequisites

- Node.js and npm installed
- Anthropic API account
- Command line access

## Step 1: Obtain Anthropic API Key

1. Go to [https://console.anthropic.com](https://console.anthropic.com)
2. Sign up or log in to your account
3. Navigate to API Keys section
4. Click "Create Key"
5. Name your key (e.g., "Cursor MCP Research")
6. Copy the API key (starts with `sk-ant-`)
7. Store it securely - you won't be able to see it again

## Step 2: Configure Environment Variable

Add your Anthropic API key to your environment:

### macOS/Linux

Add to your `~/.zshrc` or `~/.bashrc`:

```bash
export ANTHROPIC_API_KEY="sk-ant-your-key-here"
```

Then reload:

```bash
source ~/.zshrc  # or source ~/.bashrc
```

### Alternative: .env File

Create `.env` in your project root:

```bash
ANTHROPIC_API_KEY=sk-ant-your-key-here
```

Note: Ensure `.env` is in your `.gitignore`

## Step 3: Verify Configuration

The MCP configuration file is already created at:

`.cursor/mcp/claude-research-server.json`

Contents:

```json
{
  "mcpServers": {
    "claude-research": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-claude"],
      "env": {
        "ANTHROPIC_API_KEY": "${ANTHROPIC_API_KEY}"
      },
      "capabilities": {
        "resources": true,
        "tools": true,
        "prompts": true
      }
    }
  }
}
```

## Step 4: Test the Connection

Test that the MCP server can be accessed:

```bash
# Check if environment variable is set
echo $ANTHROPIC_API_KEY

# Should output your API key (starting with sk-ant-)
```

## Step 5: Using Claude MCP in Agents

### Mode Detection

Researcher agents automatically detect if Claude MCP is available:

```bash
# Check if both config file and API key exist
if [ -f ".cursor/mcp/claude-research-server.json" ] && [ ! -z "$ANTHROPIC_API_KEY" ]; then
  echo "MCP Mode - Claude API will be used"
else
  echo "Collaboration Mode - Cursor AI will be used"
fi
```

### Scientific Researcher Usage

When engaged, the Scientific Researcher will:
- Connect to Claude via MCP
- Perform deep domain research
- Access scientific literature and best practices
- Generate comprehensive research reports
- Return findings to Product Manager

### Business Researcher Usage

When engaged, the Business Researcher will:
- Connect to Claude via MCP
- Research industry and market data
- Identify regulatory requirements
- Validate business models
- Return market insights to Product Manager

## Credit Usage

With Claude MCP configured:
- **Anthropic API credits**: Used for research queries
- **Cursor AI credits**: Minimal (coordination only)

Without Claude MCP:
- **Cursor AI credits**: Higher (does all research work)
- **Anthropic API credits**: None

## Troubleshooting

### API Key Not Found

If researchers fall back to Collaboration Mode:

1. Verify API key is set:
   ```bash
   echo $ANTHROPIC_API_KEY
   ```

2. Check config file exists:
   ```bash
   ls -la .cursor/mcp/claude-research-server.json
   ```

3. Restart your shell/terminal after setting environment variable

### Connection Errors

If you see MCP connection errors:

1. Verify your API key is valid (try it in Anthropic Console)
2. Check for network issues
3. Ensure npx can access @modelcontextprotocol packages
4. Review Cursor logs for specific error messages

### Cost Management

Monitor your Anthropic API usage:
- Visit [https://console.anthropic.com](https://console.anthropic.com)
- Check "Usage" section
- Set up billing alerts if desired
- Research queries typically use Claude 3 models

## Best Practices

1. **Secure Your Key**: Never commit API keys to git
2. **Use .env**: Keep keys in environment variables or .env files
3. **Monitor Usage**: Check your Anthropic dashboard regularly
4. **Budget Alerts**: Set up spending alerts in Anthropic Console
5. **Fallback Mode**: Researchers work in Collaboration Mode without MCP

## Related Documentation

- [Figma MCP Setup](.cursor/docs/mcp-setup-figma.md)
- [Scientific Researcher Agent](.cursor/agents/scientific-researcher.md)
- [Business Researcher Agent](.cursor/agents/business-researcher.md)
- [Researcher Collaboration Protocol](.cursor/protocols/researcher-collaboration.md)

## Support

- **Anthropic API Issues**: [https://support.anthropic.com](https://support.anthropic.com)
- **MCP Protocol**: [https://modelcontextprotocol.io](https://modelcontextprotocol.io)
- **Cursor Support**: Check Cursor documentation
