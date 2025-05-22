# 🧠 Agentic AI Lead Intelligence Platform

An intelligent AI-powered platform to **search, validate, analyze, and store leads** from public sources like Google and LinkedIn — with support for real-time search logging, user-level analytics, and modular agent plugins.

---

## 🚀 Key Features

- 🔐 JWT-secured **User Authentication**
- 🤖 Modular Agent System – Google, LinkedIn (more coming)
- 📊 **Analytics** per user: keywords, industries, countries, services
- 📥 **Search & Lead Logging** in PostgreSQL
- ✅ **Email Validation** for verifying real lead quality
- 🧠 **Agent Controller** to easily add sources like Apollo, Crunchbase
- 💡 Scalable and production-ready FastAPI backend

---

## 🧱 Tech Stack

| Layer         | Tech                          |
|---------------|-------------------------------|
| Backend       | FastAPI, Python               |
| Database      | PostgreSQL, SQLAlchemy ORM    |
| Auth          | JWT, python-jose, passlib     |
| Agents        | Google & LinkedIn via SerpAPI |
| Validation    | email-validator               |
| Export        | pandas, openpyxl              |
| Logging       | Custom search/lead logs       |

---

## 📁 Project Structure

Agentic-Search-Platform/
│
├── backend/
│ ├── main.py # FastAPI entry point
│ ├── database.py # DB connection
│ ├── models.py # SQLAlchemy models
│ ├── schemas.py # Pydantic schemas
│ ├── routes/
│ │ ├── auth.py # Login/signup
│ │ ├── leads.py # Leads
│ │ ├── search_logs.py # Logs & analytics
│ │ └── search.py # Agent controller
│ ├── services/
│ │ ├── utils.py
│ │ ├── agent_controller.py
│ │ ├── google_agent.py
│ │ └── linkedin_agent.py
│
├── .env # Environment variables
├── requirements.txt # Python dependencies
└── README.md # This file


---

## ⚙️ Installation & Setup

```bash
# 1️⃣ Clone
git clone https://github.com/yourusername/agentic-platform.git
cd agentic-platform

# 2️⃣ Virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 3️⃣ Install dependencies
pip install -r requirements.txt

# 4️⃣ Configure .env
cp .env.example .env

# 5️⃣ Run
uvicorn backend.main:app --reload



