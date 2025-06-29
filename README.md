# AI Calendar Booking Assistant

 This is a conversational AI agent that helps users schedule meetings by chatting naturally. It understands messages like "Book a meeting tomorrow at 2pm" or "Any free time next Friday?" and books time on your Google Calendar.

---

## 🚀 Features

- ✨ Natural language understanding for time and dates
- 📆 Google Calendar integration
- 🧠 AI logic using LangGraph for intelligent flow
- 💬 Chat UI built with Streamlit
- 🔒 Secure via Google service account

---

## 🛠 Tech Stack

- **Backend**: FastAPI (API server)
- **Agent Logic**: LangGraph (LangChain + Graph-based logic)
- **Frontend**: Streamlit (chat interface)
- **Calendar**: Google Calendar API
- **Time Parsing**: `parsedatetime`

---

## 📁 Project Structure

```
TailorTalk/
├── app.py                  # Streamlit chat frontend
├── main.py                 # FastAPI backend
├── langgraph_workflow.py   # Agent logic using LangGraph
├── calendar_service.py     # Google Calendar integration
├── parse_utils.py          # Natural language date parsing
├── credentials.json        # Google service account key (DO NOT SHARE)
└── requirements.txt        # Python dependencies
```

---

## ✅ Setup Instructions

### 1. Clone or Download the Project

Unzip or clone:
```bash
git clone <repo-url>
cd TailorTalk
```

### 2. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Requirements

```bash
pip install -r requirements.txt
```

### 4. Set Up Google Calendar API

- Go to https://console.cloud.google.com/
- Create a project → Enable **Google Calendar API**
- Create a **Service Account** → Add key as JSON
- Save the file as `credentials.json` in the project root
- In your **Google Calendar settings**, share your calendar with the service account email:
  ```
  hello-631@your-project.iam.gserviceaccount.com
  ```
  With **Make changes to events** permission.

### 5. Run the Backend (FastAPI)

```bash
uvicorn main:app --reload
```

### 6. Run the Frontend (Streamlit)

In a new terminal:
```bash
streamlit run app.py
```

App will open at:
```
http://localhost:8501
```

---

## 💬 Example Conversations

- "Book a meeting for tomorrow at 3pm"
- "Do you have free time this Friday?"
- "Book a call between 4–5 PM next week"
- "Schedule a meeting next Monday afternoon"

---

## 📄 License

This project is for educational/demo use only.
