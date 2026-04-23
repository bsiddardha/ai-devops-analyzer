# 🧠 AI DevOps Analyzer

AI-powered log analysis tool that helps identify failures, root causes, and fixes from production logs.

---

## 🚀 What This Project Does

* Upload application logs
* Ask questions about logs
* Get AI-based analysis:

  * Summary
  * Root cause
  * Severity
  * Fix suggestions

---

## 🏗️ Tech Stack

* **Backend:** FastAPI
* **LLM:** Groq (LLaMA 3)
* **Embeddings:** Sentence Transformers
* **Vector DB:** FAISS
* **Frontend:** Custom HTML + JavaScript

---

## 📁 Project Structure

```
ai-devops-analyzer/
├── app/               # Backend logic
├── frontend/          # UI
├── logs/              # Sample logs
├── .env               # Environment template
├── requirements.txt
├── README.md
```

---

## ⚙️ Setup Instructions (Step-by-Step)

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/ai-devops-analyzer.git
cd ai-devops-analyzer
```

---

### 2️⃣ Create Virtual Environment

#### 🖥️ Windows

```bash
python -m venv venv
venv\Scripts\activate
```

#### 🐧 Mac/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Setup Environment Variables

👉 Create a `.env` file in the root directory



```text
GROQ_API_KEY=your_api_key_here
```




### 5️⃣ Get API Key (Groq)

1. Go to: https://console.groq.com
2. Create an API key
3. Paste it into `.env`

---

### 6️⃣ Run the Application

```bash
uvicorn app.main:app --reload
```

---

### 7️⃣ Open in Browser

```text
http://127.0.0.1:8000
```

---

## 🧪 How to Use

### Step 1 — Upload Logs

Paste logs into the UI and click **Upload Logs**

---

### Step 2 — Ask Questions

Try:

```
why did the service fail?
what is the root cause?
how to fix this issue?
```

---

### Step 3 — Get AI Analysis

You’ll get:

* Summary
* Root Cause
* Severity
* Fix Suggestions

---

## 📄 Sample Logs (Try This)

```text
2026-04-23 10:02:49 ERROR [db] Connection timeout
2026-04-23 10:02:52 ERROR [db] Connection refused
2026-04-23 10:02:52 CRITICAL Service failed
2026-04-23 10:02:55 Pod restarting (CrashLoopBackOff)
```

---

## 🔐 Security

* `.env` is ignored via `.gitignore`
* API keys are NOT stored in code
* Use `.env.example` as template

---

## ⚠️ Common Issues

### ❌ GROQ_API_KEY not found

Fix:

* Ensure `.env` is in root folder
* Restart server

---

### ❌ First run slow

Reason:

* Model download (one-time)

---

## 🚀 Future Improvements

* Docker support 🐳
* Kubernetes deployment ☸️
* CI/CD pipeline 🔄
* Real-time log streaming

---

## 🤝 Contributing

Feel free to fork and improve!

---

## 👨‍💻 Author

B Siddardha
