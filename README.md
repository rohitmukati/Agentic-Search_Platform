# 🤖 Agentic AI Search Platform

An AI-powered lead generation platform using FastAPI — extract, validate & analyze leads from Google & LinkedIn.

---

## 🚀 Features

- 🔐 **Authentication** – Secure login and token-based access
- 🔍 **Agentic Search** – Autonomous agents to perform contextual searches
- 🧠 **Multi-platform Support** – Google & LinkedIn integration
- 📊 **Search Logging** – Tracks and stores query logs
- 📥 **Lead Management** – Capture and manage search results as leads

---

## 📁 Project Structure

```
Agentic-Search-Platform/
├── backend/
│   ├── main.py                 # FastAPI entry point
│   ├── database.py             # Database configuration
│   ├── models.py               # SQLAlchemy models
│   ├── schemas.py              # Pydantic schemas
│   ├── routes/                 # API route handlers
│   │   ├── auth.py             # Authentication routes
│   │   ├── leads.py            # Lead management
│   │   ├── search.py           # Search operations
│   │   └── search_logs.py      # Logging user queries
│   └── services/               # Business logic and agents
│       ├── agent_controller.py # Manages multiple agents
│       ├── google_agent.py     # Google search automation
│       ├── linkedin_agent.py   # LinkedIn search automation
│       └── utils.py            # Helper functions
├── requirements.txt            # Python dependencies
└── README.md                   # Project documentation
```


---

## ⚙️ Installation

```bash
git clone <your-repo-url>
cd Agentic-Search-Platform
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn backend.main:app --reload


---

## 🛠️ Tech Stack

- **Framework**: FastAPI
- **ORM**: SQLAlchemy
- **Agents**: Custom logic for Google & LinkedIn scraping/search
- **Database**: PostgreSQL / SQLite (configurable)
- **Language**: Python 3.10+

---

## 🧪 Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/Agentic-Search-Platform.git
   cd Agentic-Search-Platform
















