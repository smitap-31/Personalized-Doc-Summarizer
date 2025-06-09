def create_prompt(chunks, persona):
    context = "\n".join(chunks)
    return f"""
You are a helpful assistant generating summaries for {persona}s.

Context:
{context}

Summary for {persona}:
"""
