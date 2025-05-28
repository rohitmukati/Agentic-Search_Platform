# 🤖 Agentic AI Search Platform

An AI-powered lead generation platform using **FastAPI** and **Streamlit** — extract, validate, search, and analyze leads from Google & LinkedIn with visual insights and downloadable reports.

---

## 🚀 Features

- 🔐 **Authentication** – Secure signup/login with JWT tokens  
- 🔍 **Agentic Search** – Autonomous agents for intelligent lead queries  
- 🧠 **Multi-platform Search** – Google + LinkedIn scraping supported  
- 📊 **Interactive Dashboard** – Visualize top searches, services, industries, and more  
- 📥 **Leads Table** – Sortable leads view with CSV export  
- 📄 **Logs** – Track search queries with timestamps  
- 📎 **CSV Export** – Export search results instantly  
- 🖥️ **Frontend Interface** – Built with Streamlit for a minimal & responsive UI  

---

## 📁 Project Structure

```
Agentic-Search-Platform/
├── backend/
│   ├── main.py                 # FastAPI entry point
│   ├── database.py             # DB setup
│   ├── models.py               # SQLAlchemy models
│   ├── schemas.py              # Pydantic schemas
│   ├── routes/
│   │   ├── auth.py             # Auth APIs
│   │   ├── leads.py            # Lead endpoints
│   │   ├── search.py           # Search agents
│   │   └── search_logs.py      # Logs API
│   └── services/
│       ├── agent_controller.py # Orchestrates search logic
│       ├── google_agent.py     # Google search agent
│       ├── linkedin_agent.py   # LinkedIn search agent
│       └── utils.py            # Utilities
├── frontend/
│   ├── app.py                  # Streamlit app entry
│   ├── auth.py                 # Login/Signup handlers
│   ├── dashboard.py            # Dashboard with charts
│   ├── search.py               # Search form UI
│   ├── leads_table.py          # Leads view and export
│   ├── logs_table.py           # Logs viewer
│   ├── config.py               # API config
│   └── utils.py                # Helpers
├── requirements.txt            # All Python dependencies
└── README.md                   # You're here!
```

---

## ⚙️ Installation & Running the Platform

```bash
# Clone the repo
git clone https://github.com/yourusername/Agentic-Search-Platform.git
cd Agentic-Search-Platform

# Create and activate virtual environment
python -m venv venv
# On macOS/Linux
source venv/bin/activate
# On Windows
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run backend
uvicorn backend.main:app --reload

# In a separate terminal, run frontend
cd frontend
streamlit run app.py
```

---

## 🌍 Accessing the App

- FastAPI docs: http://127.0.0.1:8000/docs  
- Streamlit frontend: http://localhost:8501

---

## 🛠️ Tech Stack

- **Backend**: FastAPI, SQLAlchemy  
- **Frontend**: Streamlit  
- **Database**: SQLite / PostgreSQL  
- **Language**: Python 3.10+  
- **Agents**: Custom scraping for Google + LinkedIn  

---

## 🔐 Environment Variables

Create a `.env` file in the `backend/` directory with the following:

```
DATABASE_URL=postgresql://user:pass@localhost:5432/agentic_db
SECRET_KEY=your_jwt_secret
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
SERPAPI_KEY=your_serpapi_key
MAILBOXLAYER_KEY=your_mailboxlayer_key
```

---

## ✅ API Documentation

FastAPI generates docs automatically:

- Swagger UI: `http://127.0.0.1:8000/docs`  
- ReDoc: `http://127.0.0.1:8000/redoc`

---

## 📊 Dashboard Includes

- ✅ Total Searches  
- ✅ Total Leads  
- ✅ Top 10 Searched Keywords  
- ✅ Top 10 Services  
- ✅ Top 10 Industries  
- ✅ Top 10 Locations  
- ✅ Sortable views for Leads & Logs  

---
## 📸 Screenshots

### 🔐 Login Page
<img src="assets/login_signup.png" width="600"/>

### 📊 Dashboard Overview
<img src="assets/Dashboard1.png" width="600"/>

### 🧠 Agentic Search Form
<img src="assets/Search.png" width="600"/>

### 📥 Leads Table with Sorting & Export
<img src="assets/Leads.png" width="600"/>

---
## 📌 Future Enhancements

- [ ] Docker support  
- [ ] React-based frontend  
- [ ] OAuth for LinkedIn login  
- [ ] Admin analytics page  
- [ ] MongoDB support  

---

## 🤝 Contributing

Pull requests are welcome. Open an issue first to discuss what you’d like to change.

---

## 📄 License

Licensed under the **MIT License**.  
See [LICENSE](LICENSE) for more details.
