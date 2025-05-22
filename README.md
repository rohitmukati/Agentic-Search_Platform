# 🤖 Agentic AI Search Platform

An AI-powered lead generation platform using FastAPI — extract, validate & analyze leads from Google & LinkedIn.

---

## 🚀 Features

- 🔐 **Authentication** – Secure login and token-based access  
- 🔍 **Agentic Search** – Autonomous agents to perform contextual searches  
- 🧠 **Multi-platform Support** – Google & LinkedIn integration  
- 📊 **Search Logging** – Tracks and stores query logs  
- 📥 **Lead Management** – Capture and manage search results as leads  
- ✅ **Downloadable Leads** – Search results can be exported as CSV for further use  

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
# Clone the repository
git clone https://github.com/yourusername/Agentic-Search-Platform.git
cd Agentic-Search-Platform

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate       # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the FastAPI server
uvicorn backend.main:app --reload
```

---

## 🛠️ Tech Stack

- **Framework**: FastAPI  
- **Language**: Python 3.10+  
- **Database**: PostgreSQL / SQLite (configurable)  
- **ORM**: SQLAlchemy  
- **Agents**: Custom Python logic for Google & LinkedIn scraping/search  

---

## 🧪 Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/Agentic-Search-Platform.git
   cd Agentic-Search-Platform
   ```

2. Set up your environment and dependencies:
   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

3. Launch the development server:
   ```bash
   uvicorn backend.main:app --reload
   ```

4. Open your browser and go to:
   ```
   http://127.0.0.1:8000/docs
   ```

---


### Explanation of Environment Variables and How to Get Them:

- `DATABASE_URL`:  
  The connection string for your PostgreSQL database.  
  Format example:  
  `postgresql://username:password@localhost:5432/agentic_db`  
  Replace `username`, `password`, `host`, `port`, and `database_name` according to your database setup.

- `SECRET_KEY`:  
  A secret key used to sign JWT tokens securely.  
  Make sure to generate a strong, random key (e.g., using `openssl rand -hex 32`).

- `ALGORITHM`:  
  The algorithm used to sign JWT tokens. Usually `HS256`.

- `ACCESS_TOKEN_EXPIRE_MINUTES`:  
  The expiry time for access tokens in minutes.

- `SERPAPI_KEY`:  
  API key for accessing Google Search via [SerpAPI](https://serpapi.com/).  
  You can create a free or paid account on SerpAPI and get your API key from their dashboard.

- `MAILBOXLAYER_KEY`:  
  API key for email verification service via [MailboxLayer](https://mailboxlayer.com/).  
  Register on MailboxLayer and obtain your API key from their dashboard.

---

### Security Recommendations:

- Never commit your `.env` file to public repositories.  
- Add `.env` to your `.gitignore` file to avoid accidental commits.  
- Consider creating a `.env.example` file without real keys to share variable names with collaborators.



## ✅ API Documentation

FastAPI automatically generates Swagger UI:

- Interactive docs: `http://127.0.0.1:8000/docs`
- ReDoc docs: `http://127.0.0.1:8000/redoc`

---

## 📌 Future Enhancements

- [ ] Docker support  
- [ ] MongoDB integration  
- [ ] Frontend in React/Next.js  
- [ ] OAuth for LinkedIn login  
- [ ] Dashboard with charts for admin  

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

---

## 📄 License

This project is licensed under the **MIT License**.  
See the [LICENSE](LICENSE) file for more information.
