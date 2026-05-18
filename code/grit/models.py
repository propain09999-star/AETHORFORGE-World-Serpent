import os, json, subprocess

GROQ_URL = "https://api.groq.com/openai/v1/chat/completions"

def _groq_call(prompt, model="llama-3.1-8b-instant"):
    key = os.environ.get("GROQ_API_KEY", "")
    if not key:
        return f"[Grit fallback] {prompt[:60]}..."
    payload = json.dumps({
        "model": model,
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": 512
    })
    try:
        result = subprocess.run([
            "curl", "-s",
            "https://api.groq.com/openai/v1/chat/completions",
            "-H", f"Authorization: Bearer {key}",
            "-H", "Content-Type: application/json",
            "-d", payload
        ], capture_output=True, text=True, timeout=30)
        return json.loads(result.stdout)["choices"][0]["message"]["content"]
    except Exception as e:
        return f"[Grit error] {e}"

class NanoModel:
    name = "Nano"
    def __init__(self): print("  ✓ Nano loaded")
    def process(self, task): return _groq_call(task)

class QuarkModel:
    name = "Quark"
    def process(self, task): return _groq_call(f"One sentence: {task}")

class ScoutAnt:
    name = "ScoutAnt"
    def process(self, task): return _groq_call(f"OSINT recon: {task}")

class SquireModel:
    name = "Squire"
    def __init__(self): print("  ✓ Squire loaded")
    def validate(self, output): return _groq_call(f"Validate and improve: {output}", "llama-3.3-70b-versatile")
    def process(self, task): return self.validate(task)

def get_model(tier="grit", size="nano"):
    if tier == "squire": return SquireModel()
    if size == "quark":  return QuarkModel()
    if size == "scout":  return ScoutAnt()
    return NanoModel()

