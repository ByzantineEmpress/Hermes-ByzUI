# Hermes Command Center

A custom, high-performance dashboard for the Hermes Agent infrastructure.

## Features
- **Smart Model Routing:** Automatically switches between `chat`, `coder`, `reasoning`, and `deep-logic` models based on task intent.
- **System Health:** Real-time status of `litellm`, `firecrawl`, and local inference engines.
- **Terminal UI:** A dedicated workspace for agentic interactions and code execution.
- **Customization:** Full support for custom CSS themes and widget layouts.

## Setup
1. Ensure `litellm` and `firecrawl` containers are running.
2. Open `index.html` in your browser.
3. Access the local dashboard at `http://127.0.0.1:9119` for backend management.

## Tech Stack
- **Frontend:** HTML5, Tailwind CSS, Vanilla JS.
- **Backend:** Hermes Agent (Local Inference + OpenRouter).
- **Orchestration:** LiteLLM.