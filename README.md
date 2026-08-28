# AI Genesis - openstore-telephony (ai-genesis branch)

This branch adds AI components (Rasa NLU, local LLM runner placeholder, TTS proxy) and a docker-compose file to run them for development.

Quick start (after you've built the main dev stack):

1. Build and start AI services:
   docker compose -f docker-compose.ai.yml up --build

2. Start or reuse the main docker-compose (node-app, freeswitch, vosk, etc.)

3. Train Rasa (inside rasa container):
   docker exec -it <rasa_container> rasa train

4. Test LLM runner:
   curl -X POST http://localhost:8000/generate -H 'Content-Type: application/json' -d '{"prompt":"Hello"}'

5. Test TTS proxy:
   curl -X POST http://localhost:5100/synthesize -H 'Content-Type: application/json' -d '{"text":"Hello world"}'

Notes:
- The llm-runner in this commit is a placeholder. Replace the app.py with your preferred local LLM integration (llama.cpp/gpt4all/etc.).
- Do not commit model binaries or API keys. Mount /models at runtime.
- Update Node app envs to point to Rasa/LLM/TTS services.
