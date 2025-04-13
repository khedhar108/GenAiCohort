# GenAI Cohort Projects

This repository contains AI projects developed during the GenAI Cohort program, featuring multiple applications powered by Large Language Models.

## Projects

### 1. Python Persona Chatbot

A Python application that implements a chatbot with a specific persona, using the OpenAI API for generating responses.

### 2. Cody - AI Coding Terminal Agent

An AI-powered terminal assistant that helps build and modify software projects through natural language commands, using OpenRouter AI models.

## Description

This repository showcases various GenAI applications:

- **Python Persona Chatbot**: Demonstrates how to create a chatbot with a defined personality using OpenAI's API.
- **Cody (Terminal Coding Agent)**: Allows users to create projects, files, and run commands through natural language in a terminal interface.

Each project demonstrates different aspects of working with large language models and AI tools.

## Prerequisites

*   Python 3.8+
*   Git
*   An OpenAI API Key (for Persona Chatbot)
*   An OpenRouter API Key (for Cody Terminal Agent)

## Setup and Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/khedhar108/GenAiCohort.git
    ```
    ```bash
    cd GenAiCohort
    ```

2.  **Create and activate a virtual environment:**
    *   On macOS/Linux:
        ```bash
        python -m venv .venv
        ```
        ```bash
        source .venv/bin/activate
        ```
    *   On Windows:
        ```bash
        python -m venv .venv
        ```
        ```bash
        .venv\Scripts\activate
        ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure Environment Variables:**
    *   Create a file named `.env` in the project root directory.
    *   Add your API keys to this file:
        ```dotenv
        OPENAI_API_KEY='your_openai_api_key_here'
        OPENROUTER_API_KEY='your_openrouter_api_key_here'
        ```
    *   **Important:** Ensure the `.env` file is listed in your `.gitignore` file to avoid committing secrets.

## Project Usage

### Python Persona Chatbot

To start the chatbot application:

```bash
python src/python_persona_chatbot/main.py
```

### Cody - AI Coding Terminal Agent

To start the AI coding assistant:

```bash
python cohort_gen_ai/Day3_Terminal_coding_agent/main.py
```

Once Cody is running, you can interact with it through the terminal by typing natural language commands like:
- "Create a directory called my_project"
- "Create a Python file with Flask hello world code"
- "Run pip install flask"

## Project Structure

```
GenAiCohort/
├── .venv/
├── src/
│   └── python_persona_chatbot/
│       ├── __init__.py
│       ├── chatbot/
│       │   ├── __init__.py
│       │   └── core.py
│       ├── config.py
│       ├── utils/
│       │   └── __init__.py
│       └── main.py
├── cohort_gen_ai/
│   └── Day3_Terminal_coding_agent/
│       ├── main.py
│       ├── tools.py
│       └── workspace/
├── tests/
├── .env             # <-- Make sure this is in .gitignore
├── .gitignore
├── README.md
└── requirements.txt
```

## Features

### Python Persona Chatbot
- Custom persona configuration
- Conversation history management
- OpenAI API integration

### Cody - AI Coding Terminal Agent
- 📁 Create directories and project structures
- 📝 Create and update files with code or content
- 📖 Read file contents
- 📋 List files and directory structures
- ⚡ Execute terminal commands

## Running Tests (Optional)

*(Add instructions here if you implement tests, e.g., using pytest)*

```bash
pytest
```

## Contributing

Contributions to enhance these projects are welcome. Please feel free to submit issues or pull requests.
