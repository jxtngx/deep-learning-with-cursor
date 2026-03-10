---
name: ""
overview: ""
todos: []
isProject: false
---

# TEST-002: E2E Chat Flow Test

## Description

Create end-to-end tests using Playwright to test the complete chat interaction flow from frontend to backend with LocalStack.

## Acceptance Criteria

- Playwright test for complete chat interaction
- Tests run against LocalStack environment
- Verify message sending and receiving
- Test streaming responses in UI
- Screenshots on test failure
- Tests run in CI/CD

## Technical Details

### Test Setup

Create `e2e/tests/chat.spec.ts`:

```typescript
import { test, expect } from '@playwright/test'

test.describe('Chat Interface', () => {
  test.beforeEach(async ({ page }) => {
    await page.goto('http://localhost:3000/chat')
  })

  test('should display chat interface', async ({ page }) => {
    await expect(page.locator('h1')).toContainText('AI Chat Assistant')
    await expect(page.locator('textarea')).toBeVisible()
    await expect(page.locator('button[type="submit"]')).toBeVisible()
  })

  test('should send message and receive response', async ({ page }) => {
    // Type message
    await page.locator('textarea').fill('What is 10 + 5?')
    
    // Send message
    await page.locator('button').filter({ hasText: 'Send' }).click()
    
    // Verify user message appears
    await expect(page.locator('text=What is 10 + 5?')).toBeVisible()
    
    // Wait for loading indicator
    await expect(page.locator('text=Thinking...')).toBeVisible()
    
    // Wait for response (with generous timeout for agent processing)
    await expect(page.locator('text=/15|fifteen/i')).toBeVisible({
      timeout: 30000
    })
  })

  test('should handle streaming responses', async ({ page }) => {
    await page.locator('textarea').fill('Tell me about your tech stack')
    await page.locator('button').filter({ hasText: 'Send' }).click()
    
    // Verify user message
    await expect(page.locator('text=Tell me about your tech stack')).toBeVisible()
    
    // Wait for first token (indicates streaming started)
    await page.waitForTimeout(2000)
    
    // Verify response contains expected content
    await expect(page.locator('text=/Next.js|FastAPI|LangChain/i')).toBeVisible({
      timeout: 30000
    })
  })

  test('should handle multiple messages', async ({ page }) => {
    // First message
    await page.locator('textarea').fill('What is 2 + 2?')
    await page.locator('button').filter({ hasText: 'Send' }).click()
    await expect(page.locator('text=/4|four/i')).toBeVisible({ timeout: 30000 })
    
    // Second message
    await page.locator('textarea').fill('What time is it?')
    await page.locator('button').filter({ hasText: 'Send' }).click()
    await expect(page.locator('text=/20\\d{2}/')) // Year
      .toBeVisible({ timeout: 30000 })
    
    // Verify both messages are in history
    const messages = page.locator('[data-testid="message"]')
    await expect(messages).toHaveCount(4) // 2 user + 2 assistant
  })

  test('should auto-scroll to latest message', async ({ page }) => {
    // Send multiple messages to trigger scroll
    for (let i = 0; i < 5; i++) {
      await page.locator('textarea').fill(`Message ${i}`)
      await page.locator('button').filter({ hasText: 'Send' }).click()
      await page.waitForTimeout(1000)
    }
    
    // Check if last message is visible (should be scrolled into view)
    await expect(page.locator('text=Message 4')).toBeVisible()
  })

  test('should disable input during response generation', async ({ page }) => {
    await page.locator('textarea').fill('Test message')
    await page.locator('button').filter({ hasText: 'Send' }).click()
    
    // Input should be disabled while loading
    await expect(page.locator('textarea')).toBeDisabled()
    await expect(page.locator('button').filter({ hasText: 'Send' }))
      .toBeDisabled()
    
    // Wait for response to complete
    await page.waitForSelector('text=Thinking...', { state: 'hidden' })
    
    // Input should be enabled again
    await expect(page.locator('textarea')).toBeEnabled()
  })

  test('should handle Enter key to send', async ({ page }) => {
    await page.locator('textarea').fill('Test enter key')
    await page.locator('textarea').press('Enter')
    
    await expect(page.locator('text=Test enter key')).toBeVisible()
  })

  test('should handle Shift+Enter for new line', async ({ page }) => {
    await page.locator('textarea').fill('Line 1')
    await page.keyboard.down('Shift')
    await page.locator('textarea').press('Enter')
    await page.keyboard.up('Shift')
    await page.locator('textarea').type('Line 2')
    
    const textareaValue = await page.locator('textarea').inputValue()
    expect(textareaValue).toContain('\n')
  })

  test('should display error on backend failure', async ({ page }) => {
    // Stop backend to simulate failure (or mock network error)
    await page.route('**/api/chat', route => route.abort())
    
    await page.locator('textarea').fill('This will fail')
    await page.locator('button').filter({ hasText: 'Send' }).click()
    
    // Should show error message
    await expect(page.locator('text=/error|failed/i')).toBeVisible({
      timeout: 10000
    })
  })
})

test.describe('Chat Accessibility', () => {
  test('should be keyboard navigable', async ({ page }) => {
    await page.goto('http://localhost:3000/chat')
    
    // Tab to textarea
    await page.keyboard.press('Tab')
    await expect(page.locator('textarea')).toBeFocused()
    
    // Type message
    await page.keyboard.type('Accessibility test')
    
    // Tab to send button
    await page.keyboard.press('Tab')
    await expect(page.locator('button').filter({ hasText: 'Send' }))
      .toBeFocused()
    
    // Press Enter to send
    await page.keyboard.press('Enter')
    
    await expect(page.locator('text=Accessibility test')).toBeVisible()
  })

  test('should have proper ARIA labels', async ({ page }) => {
    await page.goto('http://localhost:3000/chat')
    
    // Check for ARIA labels
    const textarea = page.locator('textarea')
    await expect(textarea).toHaveAttribute('aria-label', /.+/)
  })
})
```

### Playwright Configuration

Create `e2e/playwright.config.ts`:

```typescript
import { defineConfig, devices } from '@playwright/test'

export default defineConfig({
  testDir: './tests',
  fullyParallel: true,
  forbidOnly: !!process.env.CI,
  retries: process.env.CI ? 2 : 0,
  workers: process.env.CI ? 1 : undefined,
  reporter: 'html',
  
  use: {
    baseURL: 'http://localhost:3000',
    trace: 'on-first-retry',
    screenshot: 'only-on-failure',
  },

  projects: [
    {
      name: 'chromium',
      use: { ...devices['Desktop Chrome'] },
    },
    {
      name: 'firefox',
      use: { ...devices['Desktop Firefox'] },
    },
    {
      name: 'webkit',
      use: { ...devices['Desktop Safari'] },
    },
    {
      name: 'Mobile Chrome',
      use: { ...devices['Pixel 5'] },
    },
  ],

  webServer: [
    {
      command: 'cd ../backend && uvicorn main:app',
      url: 'http://localhost:8000/api/health',
      reuseExistingServer: !process.env.CI,
      timeout: 120 * 1000,
    },
    {
      command: 'cd ../frontend && npm run dev',
      url: 'http://localhost:3000',
      reuseExistingServer: !process.env.CI,
      timeout: 120 * 1000,
    },
  ],
})
```

### Setup Script

Create `e2e/setup.sh`:

```bash
#!/bin/bash

echo "Setting up E2E test environment..."

# Start LocalStack
docker-compose up -d localstack

# Wait for LocalStack to be ready
echo "Waiting for LocalStack..."
until curl -s http://localhost:4566/_localstack/health | grep -q '"bedrock": "available"'; do
  sleep 2
done

echo "LocalStack is ready"

# Install E2E dependencies
npm install

echo "E2E setup complete"
```

## Files to Create

- `e2e/tests/chat.spec.ts` - E2E tests
- `e2e/playwright.config.ts` - Playwright configuration
- `e2e/package.json` - E2E dependencies
- `e2e/setup.sh` - Setup script for E2E environment

### E2E Package.json

Create `e2e/package.json`:

```json
{
  "name": "e2e-tests",
  "version": "1.0.0",
  "scripts": {
    "test": "playwright test",
    "test:ui": "playwright test --ui",
    "test:debug": "playwright test --debug",
    "report": "playwright show-report"
  },
  "devDependencies": {
    "@playwright/test": "^1.40.0"
  }
}
```

## Running Tests

### Local Testing

```bash
cd e2e
chmod +x setup.sh
./setup.sh
npm test
```

### With UI Mode

```bash
npm run test:ui
```

### Specific Test

```bash
npx playwright test chat.spec.ts
```

### Debug Mode

```bash
npm run test:debug
```

## CI/CD Integration

Add to `.github/workflows/e2e.yml`:

```yaml
name: E2E Tests

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
      
      - name: Setup Node.js
        uses: actions/setup-node@v3
        with:
          node-version: '18'
      
      - name: Setup Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'
      
      - name: Install backend dependencies
        run: |
          cd backend
          pip install -e .
      
      - name: Install frontend dependencies
        run: |
          cd frontend
          npm install
      
      - name: Install Playwright
        run: |
          cd e2e
          npm install
          npx playwright install --with-deps
      
      - name: Run E2E tests
        run: |
          cd e2e
          npm test
      
      - name: Upload test results
        if: always()
        uses: actions/upload-artifact@v3
        with:
          name: playwright-report
          path: e2e/playwright-report/
```

## Definition of Done

- E2E tests cover complete chat flow
- Tests pass with LocalStack backend
- Streaming responses verified
- Multiple messages tested
- Error scenarios covered
- Accessibility tests included
- Screenshots captured on failure
- Tests run in CI/CD pipeline
- Code reviewed and approved
- Documentation includes running tests

