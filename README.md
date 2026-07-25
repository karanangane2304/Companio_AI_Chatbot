# 🤖 Companio - Your AI Companion

Companio is an AI-powered conversational assistant built using **Python**, **Gradio**, and the **Groq API**. It provides a clean chat interface with conversation memory and supports tool calling to perform utility tasks such as retrieving the current date and performing mathematical calculations.

Designed as a Tier-2 LLM application, the chatbot demonstrates the use of **conversation memory**, **function/tool calling**, and a modern web-based interface.

---

## ✨ Features

- 💬 Natural conversational AI powered by Groq LLMs
- 🧠 Conversation memory for context-aware responses
- 📅 Current Date Tool
- 🧮 Calculator Tool
- ⚡ Fast inference using the Groq API
- 🌐 Interactive Gradio web interface
- 🔧 Function (Tool) Calling support
- 🖥️ Easy local setup

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Backend Logic |
| Gradio | Web Interface |
| Groq API | LLM Inference |
| Llama 3.x (Groq) | Language Model |
| Python Functions | Tool Calling |
| dotenv | Environment Variable Management |

---

## 📂 Project Structure

```
Companio-Chatbot/
│
├── Chatbot.py
├── requirements.txt
├── .env.example
├── README.md
└── .gitignore
```

---

## 🚀 Local Setup

### 1. Clone the Repository

```bash
git clone https://github.com/karanangane2304/Companio_AI_Chatbot.git
cd Companio-Chatbot
```

---

### 2. Create a Virtual Environment

Windows (PowerShell)

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

---

### 3. Install Dependencies

```powershell
python -m pip install -r requirements.txt
```

---

### 4. Configure Environment Variables

Create a local environment file.

```powershell
Copy-Item .env.example .env
```

Open the `.env` file and replace:

```
your_groq_api_key_here
```

with your own Groq API Key.

Example:

```
GROQ_API_KEY=gsk_xxxxxxxxxxxxxxxxxxxxxxxxx
```

---

### 5. Run the Application

```powershell
python Chatbot.py
```

Gradio will launch a local server.

Open the URL displayed in the terminal (usually):

```
http://127.0.0.1:7860
```

---

## 💬 Example Conversation

**User:**

```
Hello!
```

**Bot:**

```
Hi! How can I assist you today?
```

---

**User:**

```
My name is Karan.
```

**Bot:**

```
Nice to meet you, Karan!
```

---

**User:**

```
What's my name?
```

**Bot:**

```
Your name is Karan.
```

---

**User:**

```
What's today's date?
```

**Bot:**

```
Today's date is July 24, 2026.
```

---

**User:**

```
What is 145 × 23?
```

**Bot:**

```
145 × 23 = 3335
```

---

## 🧠 Built-in Tools

### 📅 Current Date Tool

Returns the current system date.

Example:

```
What is today's date?
```

---

### 🧮 Calculator Tool

Performs basic arithmetic operations.

Example:

```
Calculate (25 + 18) × 4
```

---

## 🔒 Environment Variables

The application reads the following environment variable:

| Variable | Description |
|----------|-------------|
| `GROQ_API_KEY` | Your Groq API Key |

**Important:**

- Never commit your `.env` file.
- Only commit `.env.example`.
- Each user should use their own Groq API key.

---

## 🔐 Git & Secrets

Before pushing your project to GitHub, verify that your API key has not been staged.

```powershell
git status --short
git diff --cached
git grep -n "gsk_" -- . ':!.venv' ':!.venv-1'
```

For deployment, configure `GROQ_API_KEY` using your hosting provider's environment variable or secret management settings.

---

## 📌 Learning Outcomes

This project demonstrates:

- Large Language Model (LLM) Integration
- Conversation Memory
- Function (Tool) Calling
- Prompt Engineering
- API Integration
- Gradio Web Applications
- Environment Variable Management

---

## 👨‍💻 Author

**Karan Angane**

B.Tech CSE (AI & ML)

Vishwaniketan's Institute of Management Entrepreneurship and Engineering Technology

---

## 📄 License

This project is developed for educational and learning purposes. Feel free to modify and extend it for personal or academic use.

---

⭐ If you found this project useful, consider giving it a star on GitHub!
