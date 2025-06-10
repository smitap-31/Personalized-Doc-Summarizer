import subprocess


def query_ollama(prompt: str, model: str = "mistral") -> str:
    """Queries the Ollama model with a given prompt."""
    result = subprocess.run(
        ["ollama", "run", model],
        input=prompt.encode(),
        capture_output=True,
    )
    return result.stdout.decode()
