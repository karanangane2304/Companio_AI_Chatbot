# AI Chatbot

A Gradio chatbot using Groq with current-date and calculator tools.

## Local setup

1. Create and activate a virtual environment.
2. Install dependencies:

   ```powershell
   python -m pip install -r requirements.txt
   ```

3. Create a local environment file:

   ```powershell
   Copy-Item .env.example .env
   ```

4. Open `.env` and replace `your_groq_api_key_here` with your Groq API key.
5. Start the app:

   ```powershell
   python Chatbot.py
   ```

Open the local URL printed by Gradio, usually `http://127.0.0.1:7860`.

## Git and secrets

`.env` is ignored by Git and must never be committed. Only `.env.example` should be uploaded; it contains a placeholder and no secret.

Before the first commit, check that the key is not staged:

```powershell
git status --short
git diff --cached
git grep -n "gsk_" -- . ':!.venv' ':!.venv-1'
```

For a deployed app, add `GROQ_API_KEY` in the hosting provider's secret or environment-variable settings instead of committing it.
