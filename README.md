
# 🌿 Mental Health Chatbot

A full-stack, interactive, LLM-powered mental health chatbot built with **Python, Django, HTMX, Tailwind CSS**, and **OpenAI GPT-4**, supporting **Hindi / Hinglish / English**.

## 💡 Features

- ✔ Interactive and animated chat UI with smooth animations  
- ✔ Friendly, compassionate, NLP-powered mental health assistant  
- ✔ Supports Hindi, Hinglish, and English  
- ✔ User authentication (JWT based)  
- ✔ Fully Dockerized and production-ready  
- ✔ Easy deployment on any Docker-compatible server  
- ✔ Lightweight frontend (HTMX + Tailwind CSS)  

---

## ⚙ Project structure

```
mental_health_bot_project/
├── backend/
│   ├── chatbot/            # Chat app with LLM + language detection
│   ├── users/              # Auth system with JWT
│   ├── mental_health_bot/  # Django project core
│   ├── Dockerfile
│   ├── .env.example
│   └── requirements.txt
├── frontend/
│   └── templates/
│       └── chat.html
└── docker-compose.yml
```

---

## 🔧 Local Setup (without Docker)

### Clone the repository
```bash
git clone https://github.com/your-username/mental_health_bot_project.git
cd mental_health_bot_project/backend
```

### Setup virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### Install dependencies
```bash
pip install -r requirements.txt
```

### Create `.env` file
```bash
cp .env.example .env
# Edit .env and add your OpenAI API Key and Django secret key
```

### Run migrations
```bash
python manage.py migrate
```

### Run Django server
```bash
python manage.py runserver
```

### Access the app

- Go to `http://127.0.0.1:8000`  
- Register a user via API at `/api/auth/register/`  
- Login at `/api/auth/login/` to get JWT token  
- Use token in `chat.html` in the frontend manually (replace `'YOUR_JWT_TOKEN'`)  

---

## 🔧 Dockerized Setup (Recommended for Production)

### Clone the repo
```bash
git clone https://github.com/your-username/mental_health_bot_project.git
cd mental_health_bot_project
```

### Copy `.env` and configure
```bash
cp backend/.env.example backend/.env
# Edit backend/.env and set your keys
```

### Build and run with Docker Compose
```bash
docker-compose up --build
```

### Visit
- App will be live at `http://localhost:8000`  
- Use the same register and login flow as above.  

---

## 🔑 Authentication Flow (JWT)

| Endpoint                | Method  | Description          |
|-------------------------|---------|----------------------|
| `/api/auth/register/`   | POST    | Register new user    |
| `/api/auth/login/`      | POST    | Obtain JWT token     |
| `/api/chat/chat/`       | POST    | Send message (JWT)   |

> Use JWT token in frontend manually (for now).

---

## 🧪 Tech stack used

| Layer        | Tech                                      |
|--------------|--------------------------------------------|
| Backend       | Django + Django REST + SimpleJWT          |
| NLP Engine    | OpenAI GPT-4 + langdetect (Hindi/English) |
| Frontend      | HTMX + Tailwind CSS + Vanilla JS          |
| Deployment    | Docker + Docker Compose + Gunicorn        |
