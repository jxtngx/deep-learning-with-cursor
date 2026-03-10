# Figma MCP Setup Guide

This guide explains how to set up the Figma MCP server for the Designer agent.

## Overview

The Figma MCP server enables professional diagram creation and UI design by connecting to Figma's API, allowing the designer to create high-fidelity system architecture diagrams and wireframes without consuming Cursor AI credits for design work.

## Prerequisites

- Node.js and npm installed
- Figma account (free tier works)
- Command line access

## Step 1: Obtain Figma Access Token

1. Go to [https://www.figma.com](https://www.figma.com)
2. Sign up or log in to your account
3. Click on your profile icon (top right)
4. Select "Settings"
5. Scroll down to "Personal Access Tokens"
6. Click "Generate new token"
7. Name your token (e.g., "Cursor MCP Designer")
8. Copy the token (starts with `figd_`)
9. Store it securely - you won't be able to see it again

## Step 2: Create or Identify Figma Project

1. In Figma, create a new project or select an existing one
2. Create a new file for your product's designs
3. Copy the file key from the URL:
   - URL format: `https://www.figma.com/file/FILE_KEY/File-Name`
   - Extract the `FILE_KEY` portion

Example:
- URL: `https://www.figma.com/file/abc123xyz789/Product-Designs`
- File Key: `abc123xyz789`

## Step 3: Configure Environment Variables

Add your Figma credentials to your environment:

### macOS/Linux

Add to your `~/.zshrc` or `~/.bashrc`:

```bash
export FIGMA_ACCESS_TOKEN="figd_your-token-here"
export FIGMA_FILE_KEY="your-file-key-here"
```

Then reload:

```bash
source ~/.zshrc  # or source ~/.bashrc
```

### Alternative: .env File

Create or update `.env` in your project root:

```bash
FIGMA_ACCESS_TOKEN=figd_your-token-here
FIGMA_FILE_KEY=your-file-key-here
```

Note: Ensure `.env` is in your `.gitignore`

## Step 4: Verify Configuration

The MCP configuration file is already created at:

`.cursor/mcp/figma-design-server.json`

Contents:

```json
{
  "mcpServers": {
    "figma-design": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-figma"],
      "env": {
        "FIGMA_ACCESS_TOKEN": "${FIGMA_ACCESS_TOKEN}",
        "FIGMA_FILE_KEY": "${FIGMA_FILE_KEY}"
      },
      "capabilities": {
        "resources": true,
        "tools": true
      }
    }
  }
}
```

## Step 5: Test the Connection

Test that the MCP server can be accessed:

```bash
# Check if environment variables are set
echo $FIGMA_ACCESS_TOKEN
echo $FIGMA_FILE_KEY

# Both should output your values
```

## Step 6: Using Figma MCP in Designer Agent

### Mode Detection

Designer agent automatically detects if Figma MCP is available:

```bash
# Check if both config file and credentials exist
if [ -f ".cursor/mcp/figma-design-server.json" ] && [ ! -z "$FIGMA_ACCESS_TOKEN" ]; then
  echo "MCP Mode - Figma API will be used"
else
  echo "Collaboration Mode - Text diagrams will be used"
fi
```

### Designer Usage (MCP Mode)

When Figma MCP is configured, the Designer will:
- Connect to Figma via MCP
- Create professional system architecture diagrams
- Generate UI wireframes for key flows (conditional)
- Export diagrams as PNG/SVG
- Provide Figma links for editing
- Collaborate with Chief Architect on diagram refinement

### Designer Usage (Collaboration Mode)

Without Figma MCP, the Designer will:
- Create text-based diagrams using mermaid syntax
- Provide ASCII diagrams for simple flows
- Give textual descriptions of wireframes
- Work with Chief Architect to refine descriptions

## Credit Usage

With Figma MCP configured:
- **Figma API**: Used for diagram creation
- **Cursor AI credits**: Minimal (coordination only)

Without Figma MCP:
- **Cursor AI credits**: Higher (creates text diagrams)
- **Figma API**: None

## Figma Project Setup Best Practices

### Recommended Structure

Organize your Figma file with pages:

1. **System Diagrams**
   - High-Level Architecture
   - Data Flow Diagrams
   - Component Diagrams
   - Deployment Diagrams

2. **Wireframes** (if UI-heavy product)
   - User Flow 1
   - User Flow 2
   - Component Library

3. **Design System** (if created)
   - Colors
   - Typography
   - Spacing
   - Components

### Figma Templates

Consider using or creating templates for:
- System architecture diagram layouts
- Wireframe component libraries
- Design system documentation

## Exporting Designs

The Designer agent will:
1. Create diagrams in Figma via MCP
2. Export as PNG or SVG to local project
3. Add exports to `.cursor/plans/project-init/diagrams/`
4. Include Figma links in technical requirements

Typical export paths:
```
.cursor/plans/project-init/diagrams/
├── system-architecture.png
├── data-flow.png
├── component-diagram.png
└── wireframes/
    ├── user-flow-1.png
    └── user-flow-2.png
```

## Troubleshooting

### Access Token Not Found

If designer falls back to Collaboration Mode:

1. Verify token is set:
   ```bash
   echo $FIGMA_ACCESS_TOKEN
   ```

2. Check config file exists:
   ```bash
   ls -la .cursor/mcp/figma-design-server.json
   ```

3. Restart your shell/terminal after setting environment variable

### File Key Issues

If you see file access errors:

1. Verify file key is correct (check Figma URL)
2. Ensure your token has access to the file
3. Check file permissions in Figma (must have edit access)

### Connection Errors

If you see MCP connection errors:

1. Verify your access token is valid (try it in Figma API)
2. Check for network issues
3. Ensure npx can access @modelcontextprotocol packages
4. Review Cursor logs for specific error messages

### Rate Limiting

Figma API has rate limits:
- Check [Figma API documentation](https://www.figma.com/developers/api) for current limits
- Designer agent will handle rate limits gracefully
- Consider spacing out design generation if hitting limits

## Best Practices

1. **Secure Your Token**: Never commit access tokens to git
2. **Use .env**: Keep tokens in environment variables or .env files
3. **File Organization**: Use clear page/frame names in Figma
4. **Version Control**: Use Figma's version history for diagram iterations
5. **Collaboration**: Share Figma file with team for review
6. **Fallback Mode**: Designer works in Collaboration Mode without MCP

## Figma Free Tier Limits

Figma's free tier includes:
- Unlimited personal files
- 3 projects
- 30 days version history
- Export capabilities

This is sufficient for most product development needs.

## Related Documentation

- [Claude MCP Setup](.cursor/docs/mcp-setup-claude.md)
- [Designer Agent](.cursor/agents/designer.md)
- [Designer Collaboration Protocol](.cursor/protocols/designer-collaboration.md)
- [Chief Architect Agent](.cursor/agents/chief-architect.md)

## Support

- **Figma API Issues**: [https://help.figma.com](https://help.figma.com)
- **MCP Protocol**: [https://modelcontextprotocol.io](https://modelcontextprotocol.io)
- **Cursor Support**: Check Cursor documentation
