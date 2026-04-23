from groq import Groq
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Initialize Groq client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# Model to use (free + ultra fast)
MODEL = "llama-3.3-70b-versatile"


# ------------------------
# System Prompt
# ------------------------

SYSTEM_PROMPT = """
You are an expert DevOps engineer and log analysis assistant.
You are given a set of raw log chunks retrieved from a production system.

Your job is to:
1. Identify errors, warnings, or anomalies
2. Explain what likely went wrong
3. Suggest actionable fixes or next steps

Be concise, technical, and precise. Format your response clearly.
"""


# ------------------------
# Analyze Logs via Groq
# ------------------------

def analyze_logs(context: str) -> str:
    """
    Send retrieved log context to Groq LLM for analysis.

    Args:
        context: Concatenated log chunks from FAISS search

    Returns:
        LLM-generated analysis as a string
    """
    try:
        response = client.chat.completions.create(
            model=MODEL,
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": f"""--- LOG CONTEXT ---
{context}
-------------------

Analyze the above logs and provide:
- Root cause (if identifiable)
- Severity level (INFO / WARNING / CRITICAL)
- Recommended fix or next steps
"""}
            ],
            temperature=0.3,
            max_tokens=1024,
        )
        return response.choices[0].message.content

    except Exception as e:
        return f"LLM analysis failed: {str(e)}"


# ------------------------
# Optional: Test
# ------------------------
