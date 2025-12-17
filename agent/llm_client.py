#llm_client.py
import os
import re
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def call_llm(system_prompt: str, user_prompt: str) -> str:
    """
    Calls Groq LLM and returns raw text response.
    Cleans any markdown/code fences to ensure valid JSON.
    """
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        temperature=0.3,
        max_tokens=800
    )

    text = response.choices[0].message.content.strip()

    # Remove any Markdown code fences like ```json ... ```
    text = re.sub(r"^```json\s*", "", text)
    text = re.sub(r"\s*```$", "", text)

    return text
