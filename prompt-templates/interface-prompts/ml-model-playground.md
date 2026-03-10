<!-- Copyright 2025 jxtngx | Apache 2.0 License | https://github.com/jxtngx/claude-code-pytorch -->

# ML Model Playground Interface

I need to create an interactive ML model playground interface with real-time parameter adjustment, live prediction visualization, and performance metrics display. The interface should handle model selection from a dropdown, hyperparameter sliders with instant updates, input data upload or manual entry, and animated visualizations of predictions. Please implement using the dark theme design system in apps/global.css with CSS custom properties, WebSocket connections for real-time updates, responsive layout for desktop and mobile using CSS Grid/Flexbox, keyboard shortcuts for power users (space for play/pause, arrow keys for parameter adjustment), and export functionality for results and configurations as JSON/CSV.

## Requirements

- Framework: Vanilla JavaScript with global.css CSS custom properties
- Real-time updates: <100ms latency via WebSocket
- Browser support: Chrome 88+, Firefox 85+, Safari 14+, Edge 88+
- Mobile responsive: 320px minimum width with touch-friendly controls
- Accessibility: WCAG 2.1 AA compliance with keyboard navigation

## Success Criteria

- Real-time parameter adjustment
- Live prediction visualization
- Performance metrics dashboard
- Export/import configurations

## Deliverables

- Interactive playground interface
- Real-time model experimentation
- Performance visualization
- Configuration management
