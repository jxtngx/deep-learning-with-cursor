---
ticket: FE-002
title: Implement Streaming Response
owner: Frontend Engineer
points: 3
dependencies: [FE-001, BE-002]
phase: Frontend Chat Interface
---

# FE-002: Implement Streaming Response

## Description

Implement real-time streaming of AI responses using Server-Sent Events (SSE) or fetch streams. Update the UI token-by-token as the backend generates responses.

## Acceptance Criteria

- [ ] SSE or fetch stream client for real-time updates
- [ ] Messages appear token-by-token
- [ ] Handle connection errors gracefully
- [ ] Loading indicator during streaming
- [ ] Reconnection logic for dropped connections

## Technical Details

### Streaming Client

Create `frontend/lib/stream-client.ts`:

```typescript
export interface StreamOptions {
  onToken: (token: string) => void
  onComplete: () => void
  onError: (error: Error) => void
}

export async function streamChat(
  message: string,
  options: StreamOptions
): Promise<void> {
  const { onToken, onComplete, onError } = options
  
  try {
    const response = await fetch("http://localhost:8000/api/chat", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        message,
        stream: true,
      }),
    })

    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`)
    }

    const reader = response.body?.getReader()
    if (!reader) {
      throw new Error("Response body is not readable")
    }

    const decoder = new TextDecoder()

    while (true) {
      const { done, value } = await reader.read()
      
      if (done) {
        onComplete()
        break
      }

      const chunk = decoder.decode(value, { stream: true })
      const lines = chunk.split("\n").filter(line => line.trim())

      for (const line of lines) {
        try {
          const data = JSON.parse(line)
          if (data.token) {
            onToken(data.token)
          }
        } catch (e) {
          console.error("Failed to parse chunk:", line)
        }
      }
    }
  } catch (error) {
    onError(error instanceof Error ? error : new Error(String(error)))
  }
}
```

### Custom Hook for Chat Streaming

Create `frontend/hooks/use-chat-stream.ts`:

```typescript
import { useState, useCallback } from "react"
import { streamChat } from "@/lib/stream-client"
import { Message } from "@/components/chat/ChatInterface"

export function useChatStream() {
  const [messages, setMessages] = useState<Message[]>([])
  const [isStreaming, setIsStreaming] = useState(false)
  const [error, setError] = useState<string | null>(null)

  const sendMessage = useCallback(async (content: string) => {
    // Add user message
    const userMessage: Message = {
      id: crypto.randomUUID(),
      role: "user",
      content,
      timestamp: new Date(),
    }
    setMessages(prev => [...prev, userMessage])
    
    // Create placeholder for assistant message
    const assistantMessageId = crypto.randomUUID()
    const assistantMessage: Message = {
      id: assistantMessageId,
      role: "assistant",
      content: "",
      timestamp: new Date(),
    }
    setMessages(prev => [...prev, assistantMessage])
    
    setIsStreaming(true)
    setError(null)

    await streamChat(content, {
      onToken: (token: string) => {
        setMessages(prev => 
          prev.map(msg => 
            msg.id === assistantMessageId
              ? { ...msg, content: msg.content + token }
              : msg
          )
        )
      },
      onComplete: () => {
        setIsStreaming(false)
      },
      onError: (err: Error) => {
        setError(err.message)
        setIsStreaming(false)
        // Remove incomplete assistant message on error
        setMessages(prev => prev.filter(msg => msg.id !== assistantMessageId))
      },
    })
  }, [])

  const clearMessages = useCallback(() => {
    setMessages([])
    setError(null)
  }, [])

  return {
    messages,
    isStreaming,
    error,
    sendMessage,
    clearMessages,
  }
}
```

### Updated Chat Interface

Update `frontend/components/chat/ChatInterface.tsx`:

```tsx
"use client"

import { ChatMessages } from "./ChatMessages"
import { ChatInput } from "./ChatInput"
import { useChatStream } from "@/hooks/use-chat-stream"
import { Alert, AlertDescription } from "@/components/ui/alert"
import { AlertCircle } from "lucide-react"

export function ChatInterface() {
  const { messages, isStreaming, error, sendMessage, clearMessages } = useChatStream()

  return (
    <div className="flex flex-col h-screen max-w-4xl mx-auto">
      <header className="p-4 border-b">
        <h1 className="text-2xl font-bold">AI Chat Assistant</h1>
        <p className="text-sm text-muted-foreground">
          Powered by LangChain and AWS Bedrock
        </p>
      </header>
      
      {error && (
        <Alert variant="destructive" className="m-4">
          <AlertCircle className="h-4 w-4" />
          <AlertDescription>{error}</AlertDescription>
        </Alert>
      )}
      
      <ChatMessages messages={messages} isLoading={isStreaming} />
      <ChatInput onSend={sendMessage} disabled={isStreaming} />
    </div>
  )
}
```

### Environment Configuration

Update `frontend/.env.local`:

```bash
NEXT_PUBLIC_API_URL=http://localhost:8000
```

Update stream client to use env var:

```typescript
const API_URL = process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000"

export async function streamChat(message: string, options: StreamOptions) {
  const response = await fetch(`${API_URL}/api/chat`, {
    // ... rest of implementation
  })
}
```

## Files to Create/Modify

- `frontend/lib/stream-client.ts` - Streaming fetch implementation
- `frontend/hooks/use-chat-stream.ts` - Custom hook for chat state
- `frontend/components/chat/ChatInterface.tsx` - Update to use streaming
- `frontend/.env.local` - API endpoint configuration

## Testing

### Manual Testing

1. Start backend: `cd backend && uvicorn main:app --reload`
2. Start frontend: `cd frontend && npm run dev`
3. Navigate to `http://localhost:3000/chat`
4. Send message: "What is 10 + 5?"
5. Verify response streams token-by-token
6. Test error handling: stop backend and try sending message
7. Test reconnection: restart backend and send another message

### Test Scenarios

- [ ] Normal streaming response works
- [ ] Long responses stream smoothly
- [ ] Error displays when backend is down
- [ ] Connection timeout handled gracefully
- [ ] Multiple rapid messages queued correctly
- [ ] Auto-scroll works during streaming
- [ ] Cancel/interrupt streaming (optional)

## Error Handling

Add retry logic for transient failures:

```typescript
async function streamChatWithRetry(
  message: string,
  options: StreamOptions,
  maxRetries = 3
) {
  for (let i = 0; i < maxRetries; i++) {
    try {
      await streamChat(message, options)
      return
    } catch (error) {
      if (i === maxRetries - 1) {
        options.onError(error as Error)
      }
      // Wait before retry with exponential backoff
      await new Promise(resolve => setTimeout(resolve, 1000 * Math.pow(2, i)))
    }
  }
}
```

## Performance Considerations

- Use `requestAnimationFrame` for smooth UI updates during high-frequency token streaming
- Debounce rapid token updates if needed
- Consider virtualization for very long message lists

## Definition of Done

- [ ] Streaming works with backend API
- [ ] Messages appear token-by-token smoothly
- [ ] Error handling displays user-friendly messages
- [ ] Reconnection logic works after connection drop
- [ ] No memory leaks from unclosed streams
- [ ] Code reviewed and approved
- [ ] Manual testing completed
- [ ] Environment variables documented
