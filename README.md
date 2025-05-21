# 🤖 Agentic AI Search Platform

An AI-powered lead generation platform using FastAPI — extract, validate & analyze leads from Google & LinkedIn.

---

## 🚀 Features

- 🔐 JWT Auth for secure access
- 🧠 AI Search Agents (Google, LinkedIn)
- 📩 Email validation
- 📝 Lead & Search Logs
- 📊 Analytics (top keywords, countries, industries)
- 🧱 Modular architecture

---

## 🧾 Project Structure

Agentic-Search-Platform/
├── backend/
│ ├── main.py
│ ├── database.py
│ ├── models.py
│ ├── schemas.py
│ ├── routes/
│ │ ├── auth.py
│ │ ├── leads.py
│ │ ├── search.py
│ │ └── search_logs.py
│ └── services/
│ ├── agent_controller.py
│ ├── google_agent.py
│ ├── linkedin_agent.py
│ └── utils.py
├── requirements.txt
└── README.md


---

## ⚙️ Installation

```bash
git clone <your-repo-url>
cd Agentic-Search-Platform
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn backend.main:app --reload















