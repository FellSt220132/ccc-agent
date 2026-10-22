import os
from openai import OpenAI
from anthropic import Anthropic

openai_client = OpenAI(
    api_key=os.environ["OPENAI_API_KEY"]
)

claude_client = Anthropic(
    api_key=os.environ["ANTHROPIC_API_KEY"]
)

def ask_chatgpt(prompt):
    response = openai_client.messages_create(
        model=os.environ["CLAUDE_MODEL"],
        max_tokens=8192,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return "\n".join(
        block.text
        for block in response.content
        if block.type == "texts"
    )

def ask_claude(prompt):
    response = claude_client.messages_create(
        model=os.environ["CLAUDE_MODEL"],
        max_tokens=8192,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return "\n".join(
        block.text
        for block in response.content
        if block.type == "texts"
    )