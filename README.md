# 🤖 Agentic AI Search Platform

An AI-powered lead generation platform using **FastAPI** and **Streamlit** — extract, validate, search, and analyze leads from Google & LinkedIn with visual insights and downloadable reports.

---

## 🚀 Features

- 🔐 **Authentication** – Secure signup/login with JWT tokens  
- 🔍 **Agentic Search** – Autonomous agents for intelligent lead queries  
- 🌐 **Multi-platform Search** – Google + LinkedIn scraping  
- 📊 **Admin Dashboard** – Full user & search analytics (with delete + insights)  
- 📥 **Leads Table** – Sort + export collected leads with 1 click  
- 🧾 **Search Logs** – Timestamped user search history  
- 👨‍💼 **User Management** – Admin can view/delete users and track top performers  
- 🖼️ **Visual Insights** – Pie charts for industries, services, locations  
- 🖥️ **Streamlit UI** – Clean, responsive frontend with expanding sections  
- 🧠 **LLM Ready** – Google Gemini, OpenAI, LangChain integrated  
- 📎 **Export** – One-click CSV export for leads    
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

## 📊 Admin Dashboard Includes

📊 Admin Dashboard Includes

- 👤 Total Users
- 🧠 Total Searches
- 🧾 Total Leads
- 🏆 Top 10 Users (by search activity)
- 🏭 Top Industries (Pie chart)
- 🛠️ Top Services (Pie chart)
- 🌍 Top Locations (Pie chart)
- 🧹 Delete users + all their data
- 🔐 Admin-only access and controls



---

## 📸 Screenshots

### images Folder Path
## 📸 Screenshots

All screenshots used in this README are stored in the `assets/` folder.

- 🔐 [Login Page](assets/login_signup.png)  
- 📊 [Dashboard Overview](assets/Dashboard1.png)  
- 🧠 [Agentic Search Form](assets/Search.png)  
- 📥 [Leads Table with Sorting & Export](assets/Leads.png)  


---
## 📌 Future Enhancements

- Docker support
- OAuth (Google/LinkedIn login)
- Admin analytics PDF export
- Role-based permissions
- MongoDB / NoSQL support
- React frontend

---

## 🤝 Contributing

Pull requests are welcome. Open an issue first to discuss what you’d like to change.

---

## 📄 License

Licensed under the **MIT License**.  
See [LICENSE](LICENSE) for more details.
