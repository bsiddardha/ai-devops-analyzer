import re
from typing import List

# -----------------------------------
# Clean Logs
# -----------------------------------
def clean_log(log: str) -> str:
    """
    Normalize logs:
    - Remove extra spaces
    - Strip unwanted characters
    """
    log = log.strip()
    log = re.sub(r'\s+', ' ', log)
    return log


# -----------------------------------
# Detect Important Lines (Errors)
# -----------------------------------
def is_important(line: str) -> bool:
    keywords = ["ERROR", "CRITICAL", "FAIL", "EXCEPTION"]
    return any(keyword in line.upper() for keyword in keywords)


# -----------------------------------
# Smart Chunking (Production Style)
# -----------------------------------
def chunk_logs(log: str, max_length: int = 300) -> List[str]:
    """
    Intelligent chunking:
    - Groups related lines
    - Keeps error context together
    """
    lines = log.split("\n")

    chunks = []
    current_chunk = []

    for i, line in enumerate(lines):
        line = line.strip()
        if not line:
            continue

        current_chunk.append(line)

        # 🔥 If important line → include next 2 lines for context
        if is_important(line):
            for j in range(1, 3):
                if i + j < len(lines):
                    current_chunk.append(lines[i + j].strip())

        # If chunk too big → finalize it
        if sum(len(l) for l in current_chunk) > max_length:
            chunks.append(" ".join(current_chunk))
            current_chunk = []

    if current_chunk:
        chunks.append(" ".join(current_chunk))

    return chunks


# -----------------------------------
# Full Ingestion Pipeline
# -----------------------------------
def ingest(log: str) -> List[str]:
    cleaned = clean_log(log)
    chunks = chunk_logs(cleaned)
    return chunks