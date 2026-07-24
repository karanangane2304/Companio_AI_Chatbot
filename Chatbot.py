import os
import json
from datetime import datetime

from groq import Groq
import gradio as gr
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
client = Groq(api_key=GROQ_API_KEY) if GROQ_API_KEY else None

messages = []

def get_current_date():
    """Returns today's current date."""

    return str(datetime.now().date())

def calculator(expression: str):
    """Evaluates a mathematical expression and returns the result."""
    try:
        return str(eval(expression))
    except Exception as e:
        return f"Error evaluating expression: {e}"

tools = [
    {
        "type": "function",
        "function": {
            "name": "get_current_date",
            "description": "Returns today's date.",
            "parameters": {
                "type": "object",
                "properties": {},
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "calculator",
            "description": "Evaluates a mathematical expression and returns the result.",
            "parameters": {
                "type": "object",
                "properties": {
                    "expression": {
                        "type": "string",
                        "description": "The mathematical expression to evaluate."
                    }
                },
                "required": ["expression"]
            },
        },
    }
]

def call_function(name, arguments):

    if name == "get_current_date":
        return get_current_date()
    elif name == "calculator":
        return calculator(expression=arguments.get("expression"))

    return "Tool not found."

def chatbot(message, history):

    global messages

    if client is None:
        return "GROQ_API_KEY is not configured. Set it before sending a message."

    # Save user message
    messages.append(
        {
            "role": "user",
            "content": message
        }
    )

    # First API Call
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=messages,
        tools=tools,
        tool_choice="auto"
    )

    assistant_message = response.choices[0].message

    # Check if tool is requested
    if assistant_message.tool_calls:

        tool_call = assistant_message.tool_calls[0]

        function_name = tool_call.function.name

        arguments = {}

        if tool_call.function.arguments:
            arguments = json.loads(tool_call.function.arguments)

        result = call_function(function_name, arguments)

        # Save assistant tool request
        messages.append(assistant_message.model_dump(exclude_none=True))

        # Send tool result
        messages.append(
            {
                "role": "tool",
                "tool_call_id": tool_call.id,
                "content": result
            }
        )

        # Second API Call
        second_response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=messages
        )

        final_answer = second_response.choices[0].message.content

        messages.append(
            {
                "role": "assistant",
                "content": final_answer
            }
        )

        return final_answer

    # Normal conversation
    else:

        final_answer = assistant_message.content

        messages.append(
            {
                "role": "assistant",
                "content": final_answer
            }
        )

        return final_answer

demo = gr.ChatInterface(
    fn=chatbot,
    title="AIVA - AI Virtual Assistant",
    description="Memory + Current Date Tool"
)

demo.launch()