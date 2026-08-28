# Simple LLM runner wrapper with optional GPT4All / local runner
from flask import Flask, request, jsonify
import os

app = Flask(__name__)

MODEL_TYPE = os.environ.get('MODEL_TYPE', 'gpt4all')

@app.route('/generate', methods=['POST'])
def generate():
    data = request.json or {}
    prompt = data.get('prompt', '')
    # NOTE: This is a placeholder. Replace with actual llama.cpp / gpt4all invocation.
    # For now, echo with a simple template to allow integration testing.
    response_text = f"[LLM simulated reply] Prompt received: {prompt[:200]}"
    return jsonify({"text": response_text})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
