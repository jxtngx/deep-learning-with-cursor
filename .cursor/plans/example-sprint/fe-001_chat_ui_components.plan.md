---
ticket: FE-001
title: Create Chat UI Components
owner: Frontend Engineer
points: 5
dependencies: []
phase: Frontend Chat Interface
---

# FE-001: Create Chat UI Components

## Description

Build chat interface components using Shadcn UI: message list with auto-scroll, input field, message bubbles with user/assistant styling, and loading states.

## Acceptance Criteria

- [ ] Chat message list with auto-scroll to bottom
- [ ] Message input with send button
- [ ] Message bubbles with distinct user/assistant styling
- [ ] Loading state during response generation
- [ ] Responsive design with Tailwind CSS
- [ ] Accessible keyboard navigation

## Technical Details

### Component Structure

```
frontend/
├── app/
│   └── chat/
│       └── page.tsx
└── components/
    └── chat/
        ├── ChatInterface.tsx
        ├── ChatMessages.tsx
        ├── ChatInput.tsx
        └── MessageBubble.tsx
```

### Main Chat Interface

Create `frontend/components/chat/ChatInterface.tsx`:

```tsx
"use client"

import { useState } from "react"
import { ChatMessages } from "./ChatMessages"
import { ChatInput } from "./ChatInput"

export interface Message {
  id: string
  role: "user" | "assistant"
  content: string
  timestamp: Date
}

export function ChatInterface() {
  const [messages, setMessages] = useState<Message[]>([])
  const [isLoading, setIsLoading] = useState(false)

  const handleSend = async (content: string) => {
    const userMessage: Message = {
      id: crypto.randomUUID(),
      role: "user",
      content,
      timestamp: new Date(),
    }
    
    setMessages(prev => [...prev, userMessage])
    setIsLoading(true)
    
    // TODO: Replace with actual API call in FE-002
    setTimeout(() => {
      const assistantMessage: Message = {
        id: crypto.randomUUID(),
        role: "assistant",
        content: "This is a placeholder response.",
        timestamp: new Date(),
      }
      setMessages(prev => [...prev, assistantMessage])
      setIsLoading(false)
    }, 1000)
  }

  return (
    <div className="flex flex-col h-screen max-w-4xl mx-auto">
      <header className="p-4 border-b">
        <h1 className="text-2xl font-bold">AI Chat Assistant</h1>
        <p className="text-sm text-muted-foreground">
          Powered by LangChain and AWS Bedrock
        </p>
      </header>
      
      <ChatMessages messages={messages} isLoading={isLoading} />
      <ChatInput onSend={handleSend} disabled={isLoading} />
    </div>
  )
}
```

### Message List Component

Create `frontend/components/chat/ChatMessages.tsx`:

```tsx
import { useEffect, useRef } from "react"
import { MessageBubble } from "./MessageBubble"
import { Message } from "./ChatInterface"
import { Loader2 } from "lucide-react"

interface ChatMessagesProps {
  messages: Message[]
  isLoading: boolean
}

export function ChatMessages({ messages, isLoading }: ChatMessagesProps) {
  const messagesEndRef = useRef<HTMLDivElement>(null)

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" })
  }

  useEffect(() => {
    scrollToBottom()
  }, [messages])

  return (
    <div className="flex-1 overflow-y-auto p-4 space-y-4">
      {messages.length === 0 && (
        <div className="flex items-center justify-center h-full text-muted-foreground">
          <div className="text-center">
            <p className="text-lg font-medium">Start a conversation</p>
            <p className="text-sm">Ask me anything!</p>
          </div>
        </div>
      )}
      
      {messages.map(message => (
        <MessageBubble key={message.id} message={message} />
      ))}
      
      {isLoading && (
        <div className="flex items-center gap-2 text-muted-foreground">
          <Loader2 className="w-4 h-4 animate-spin" />
          <span className="text-sm">Thinking...</span>
        </div>
      )}
      
      <div ref={messagesEndRef} />
    </div>
  )
}
```

### Message Bubble Component

Create `frontend/components/chat/MessageBubble.tsx`:

```tsx
import { Message } from "./ChatInterface"
import { cn } from "@/lib/utils"
import { Bot, User } from "lucide-react"

interface MessageBubbleProps {
  message: Message
}

export function MessageBubble({ message }: MessageBubbleProps) {
  const isUser = message.role === "user"
  
  return (
    <div className={cn(
      "flex gap-3",
      isUser ? "flex-row-reverse" : "flex-row"
    )}>
      <div className={cn(
        "flex items-center justify-center w-8 h-8 rounded-full shrink-0",
        isUser ? "bg-primary" : "bg-secondary"
      )}>
        {isUser ? (
          <User className="w-5 h-5 text-primary-foreground" />
        ) : (
          <Bot className="w-5 h-5 text-secondary-foreground" />
        )}
      </div>
      
      <div className={cn(
        "flex flex-col gap-1 max-w-[70%]",
        isUser ? "items-end" : "items-start"
      )}>
        <div className={cn(
          "px-4 py-2 rounded-lg",
          isUser 
            ? "bg-primary text-primary-foreground" 
            : "bg-secondary text-secondary-foreground"
        )}>
          <p className="text-sm whitespace-pre-wrap">{message.content}</p>
        </div>
        <span className="text-xs text-muted-foreground">
          {message.timestamp.toLocaleTimeString()}
        </span>
      </div>
    </div>
  )
}
```

### Input Component

Create `frontend/components/chat/ChatInput.tsx`:

```tsx
"use client"

import { useState, KeyboardEvent } from "react"
import { Button } from "@/components/ui/button"
import { Textarea } from "@/components/ui/textarea"
import { Send } from "lucide-react"

interface ChatInputProps {
  onSend: (message: string) => void
  disabled?: boolean
}

export function ChatInput({ onSend, disabled }: ChatInputProps) {
  const [input, setInput] = useState("")

  const handleSend = () => {
    if (input.trim() && !disabled) {
      onSend(input.trim())
      setInput("")
    }
  }

  const handleKeyDown = (e: KeyboardEvent<HTMLTextAreaElement>) => {
    if (e.key === "Enter" && !e.shiftKey) {
      e.preventDefault()
      handleSend()
    }
  }

  return (
    <div className="p-4 border-t">
      <div className="flex gap-2">
        <Textarea
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyDown={handleKeyDown}
          placeholder="Type your message... (Shift+Enter for new line)"
          disabled={disabled}
          className="resize-none"
          rows={2}
        />
        <Button 
          onClick={handleSend} 
          disabled={disabled || !input.trim()}
          size="icon"
        >
          <Send className="w-4 h-4" />
        </Button>
      </div>
    </div>
  )
}
```

### Chat Page

Create `frontend/app/chat/page.tsx`:

```tsx
import { ChatInterface } from "@/components/chat/ChatInterface"

export default function ChatPage() {
  return <ChatInterface />
}
```

## Files to Create/Modify

- `frontend/components/chat/ChatInterface.tsx` - Main chat container
- `frontend/components/chat/ChatMessages.tsx` - Message list with auto-scroll
- `frontend/components/chat/ChatInput.tsx` - Input field with send button
- `frontend/components/chat/MessageBubble.tsx` - Individual message display
- `frontend/app/chat/page.tsx` - Chat route page

## Testing

### Manual Testing Checklist

- [ ] Navigate to `/chat`
- [ ] Send a message
- [ ] Verify message appears in chat
- [ ] Verify auto-scroll to bottom
- [ ] Test Enter key to send
- [ ] Test Shift+Enter for new line
- [ ] Verify loading state appears
- [ ] Test responsive design on mobile
- [ ] Test keyboard navigation
- [ ] Verify accessibility with screen reader

## Definition of Done

- [ ] All components render without errors
- [ ] Auto-scroll works correctly
- [ ] Keyboard shortcuts functional (Enter to send)
- [ ] Loading state displays properly
- [ ] Responsive on mobile and desktop
- [ ] Accessible (keyboard nav, screen readers)
- [ ] Code reviewed and approved
- [ ] Matches design specifications
