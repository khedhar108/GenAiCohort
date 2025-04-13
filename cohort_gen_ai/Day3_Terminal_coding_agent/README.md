# 🤖 Cody - AI Coding Terminal Agent

## Overview

Cody is an AI-powered terminal assistant that helps you build and modify software projects through natural language commands. Using OpenRouter's AI models, Cody can create files and directories, write code, run terminal commands, and more - all from a simple command-line interface.

## 🌟 Features

- 📁 **Create Directories**: Set up project structures and nested folders
- 📝 **Create/Update Files**: Generate or modify code files with specified content
- 📖 **Read Files**: View the contents of any file in your workspace
- 📋 **List Files**: See the structure of your project directories
- ⚡ **Execute Commands**: Run terminal commands like pip install, npm init, etc.

## 🚀 Getting Started

### Prerequisites

- Python 3.7+
- pip (Python package manager)

### Installation

1. Clone this repository or download the files
   ```bash
   git clone <repository-url>
   cd Day3_Terminal_coding_agent
   ```

2. Install required dependencies
   ```bash
   pip install openai python-dotenv
   ```

3. Create a `.env` file in the project directory with your OpenRouter API key:
   ```
   OPENROUTER_API_KEY=your_openrouter_api_key_here
   ```

4. Run the application:
   ```bash
   python main.py
   ```

## 💡 How to Use

### Basic Usage

Once you start the application, you'll see a welcome message and a prompt. Simply type your request in natural language:

```
🧑‍💻 > Create a simple Flask application
```

Cody will interpret your request, break it down into the necessary steps, and execute them using the available tools.

### Available Tools

Cody has the following capabilities:

1. **Create Directories**:
   ```
   🧑‍💻 > Create a directory called "my_project"
   ```

2. **Create or Update Files**:
   ```
   🧑‍💻 > Create a Python file called "app.py" with a Flask hello world app
   ```

3. **Read Files**:
   ```
   🧑‍💻 > Show me the contents of app.py
   ```

4. **List Files**:
   ```
   🧑‍💻 > List files in the my_project directory
   ```

5. **Run Terminal Commands**:
   ```
   🧑‍💻 > Install Flask using pip
   ```

### Example Project Scenarios

#### Creating a Basic Web Application

```
🧑‍💻 > Create a directory called "web_app"
🧑‍💻 > Inside web_app, create an HTML file called "index.html" with a basic template
🧑‍💻 > Add a CSS file called "styles.css" in the web_app directory
🧑‍💻 > Add a JavaScript file called "script.js" in the web_app directory
```

#### Setting Up a Flask Project

```
🧑‍💻 > Create a directory called "flask_app"
🧑‍💻 > Create a file called "app.py" in flask_app with a basic Flask application
🧑‍💻 > Create a requirements.txt file with Flask as a dependency
🧑‍💻 > Install the requirements
🧑‍💻 > Run the Flask application
```

#### Building a Node.js Application

```
🧑‍💻 > Create a directory called "node_project"
🧑‍💻 > Initialize a Node.js project in that directory
🧑‍💻 > Install Express as a dependency
🧑‍💻 > Create a server.js file with a basic Express server
```

## 🔍 Advanced Usage

### Multi-File Projects

Cody can handle multi-file projects. Simply describe what you want to create:

```
🧑‍💻 > Create a React component structure with components for Header, Footer, and Main
```

### Code Modifications

Cody can modify existing code:

```
🧑‍💻 > Add a new route to the Flask app to handle POST requests
```

### Combining Multiple Operations

Chain operations together for complex tasks:

```
🧑‍💻 > Set up a Flask API with SQLite database connection and endpoints for user CRUD operations
```

## ⚙️ Configuration

The workspace directory is set to `workspace/` within the project folder. All files and directories are created relative to this path.

## 🔒 Security Notes

- Cody runs terminal commands in the workspace directory - be mindful of the commands you ask it to execute
- Do not use Cody to run sensitive commands or manage production systems
- API keys are stored in the .env file - make sure this file is not committed to public repositories

## 📚 Tips for Effective Use

1. **Be Specific**: Provide clear, detailed instructions
2. **Start Simple**: Begin with basic commands and increase complexity
3. **Check Results**: Use the list_files and read_file tools to verify changes
4. **Step by Step**: For complex projects, break down your requests into smaller steps
5. **Path Awareness**: Remember all paths are relative to the workspace directory

## 🤝 Contributing

Contributions are welcome! Feel free to submit issues or pull requests.


