import json
import os
from dotenv import load_dotenv
from openai import OpenAI
import tools

# Load environment variables
load_dotenv()

# Get the OpenRouter API key
openrouter_api_key = os.getenv("OPENROUTER_API_KEY")
if not openrouter_api_key:
    raise ValueError("OPENROUTER_API_KEY not found in .env file")

# Initialize the client for OpenRouter
client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key=openrouter_api_key,
)

# Define available tools
available_tools = {
    "create_directory": {
        "fn": tools.create_directory,
        "description": "Creates a directory (and any parent directories) at the specified path within the workspace.",
        "parameters": {
            "type": "object",
            "properties": {
                "path": {"type": "string", "description": "The relative path for the directory to create (e.g., 'my_project/src')."}
            },
            "required": ["path"]
        }
    },
    "create_or_update_file": {
        "fn": tools.create_or_update_file,
        "description": "Creates a new file or completely overwrites an existing file with the given content at the specified path within the workspace.",
        "parameters": {
            "type": "object",
            "properties": {
                "path": {"type": "string", "description": "The relative path for the file (e.g., 'my_project/main.py')."},
                "content": {"type": "string", "description": "The full content to write into the file."}
            },
            "required": ["path", "content"]
        }
    },
    "read_file": {
        "fn": tools.read_file,
        "description": "Reads the entire content of a file at the specified path within the workspace.",
        "parameters": {
            "type": "object",
            "properties": {
                "path": {"type": "string", "description": "The relative path of the file to read (e.g., 'my_project/main.py')."}
            },
            "required": ["path"]
        }
    },
    "list_files": {
        "fn": tools.list_files,
        "description": "Lists all files and directories within a specified path in the workspace.",
        "parameters": {
            "type": "object",
            "properties": {
                "path": {"type": "string", "description": "The relative path within the workspace to list files from (e.g., 'my_project/src'). Defaults to '.' (workspace root)."}
            },
            "required": []
        }
    },
    "run_terminal_command": {
        "fn": tools.run_terminal_command,
        "description": "Executes a shell command within the workspace directory and returns its output.",
        "parameters": {
            "type": "object",
            "properties": {
                "command": {"type": "string", "description": "The shell command to execute (e.g., 'pip install flask')."}
            },
            "required": ["command"]
        }
    }
}

# Function to get emoji based on tool type
def get_tool_emoji(tool_name):
    emoji_map = {
        "create_directory": "📁",
        "create_or_update_file": "📝",
        "read_file": "📖",
        "list_files": "📋",
        "run_terminal_command": "⚡"
    }
    return emoji_map.get(tool_name, "🔧")

# Function to convert our tools into the format expected by the API
def get_tool_definitions():
    tools_list = []
    for name, tool_info in available_tools.items():
        tools_list.append({
            "type": "function",
            "function": {
                "name": name,
                "description": tool_info["description"],
                "parameters": tool_info["parameters"]
            }
        })
    return tools_list

# System message to instruct the AI on its role and capabilities
system_prompt = f"""
You are Cody, an AI coding assistant that helps users create and modify software projects.
You have access to the following tools that allow you to interact with the file system:
- create_directory: Create a new directory
- create_or_update_file: Create a new file or update an existing one
- read_file: Read the contents of a file
- list_files: List files in a directory
- run_terminal_command: Execute shell commands

All paths are relative to the workspace directory: {tools.WORKSPACE_DIR}
"""

# Initialize conversation with system message
messages = [
    {"role": "system", "content": system_prompt}
]

# Welcome message with better formatting and emojis
print("\n" + "=" * 60)
print("✨ 🤖 Welcome to Cody - Your AI Coding Assistant! ✨")
print("=" * 60 + "\n")
print("🏠 Working directory: " + tools.WORKSPACE_DIR + "\n")
print("💡 Type your coding requests or 'exit' to quit\n")

# Main interaction loop
while True:
    user_input = input("🧑‍💻 > ")
    if user_input.lower() in ['exit', 'quit']:
        print("\n👋 Goodbye! Happy coding!\n")
        break
    
    # Add user message to conversation history
    messages.append({"role": "user", "content": user_input})
    
    # Show thinking indicator
    print("\n🔍 Thinking...\n")
    
    try:
        # Send conversation to OpenAI API
        response = client.chat.completions.create(
            model="gpt-3.5-turbo-0125", # Use a model that supports function calling
            messages=messages,
            tools=get_tool_definitions(),
            tool_choice="auto" # Let the model decide whether to use tools
        )
        
        # Extract the assistant's message
        assistant_message = response.choices[0].message
        messages.append(assistant_message) # Add to conversation history
        
        # Check if the assistant wants to use tools
        if hasattr(assistant_message, 'tool_calls') and assistant_message.tool_calls:
            print("\n✨ Planning and executing your request... ✨")            
            # Process each tool call
            for tool_call in assistant_message.tool_calls:
                function_name = tool_call.function.name
                if function_name in available_tools:
                    # Parse the function arguments
                    function_args = json.loads(tool_call.function.arguments)
                    
                    # Get appropriate emoji for this tool
                    tool_emoji = get_tool_emoji(function_name)
                    
                    # Format args for display
                    formatted_args = json.dumps(function_args, indent=2)
                    
                    # Get the function to call
                    function_to_call = available_tools[function_name]["fn"]
                    
                    # Call the function with the provided arguments
                    print(f"{tool_emoji} Using tool: {function_name}")
                    print(f"   with parameters: {formatted_args}\n")
                    result = function_to_call(**function_args)
                    
                    # Add the result to conversation history
                    messages.append({
                        "tool_call_id": tool_call.id,
                        "role": "tool",
                        "name": function_name,
                        "content": result
                    })
                    
                    # Show result (with formatting)
                    print(f"🔹 Result: {result}\n")
            
            # Get the final response after tool use
            print("🧩 Finalizing response...\n")
            final_response = client.chat.completions.create(
                model="gpt-3.5-turbo-0125",
                messages=messages
            )
            assistant_response = final_response.choices[0].message.content
        else:
            # If no tools were used, just get the content
            assistant_response = assistant_message.content
        
        # Display the assistant's response with nice formatting
        print("\n" + "=" * 60)
        print("🤖 Cody says:")
        print("=" * 60 + "\n")
        
        # Format the response content with proper spacing
        formatted_response = "\n".join([f"  {line}" for line in assistant_response.split('\n')])
        print(formatted_response)
        print("\n" + "-" * 60 + "\n")
        
    except Exception as e:
        print(f"\n❌ Error: {str(e)}\n")
        print("Please try again or check your connection.\n")
