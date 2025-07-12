# ✈️ RAG Chatbot for Airline FAQs

This project is a **Retrieval-Augmented Generation (RAG) based chatbot** designed to answer Frequently Asked Questions (FAQs) related to airlines. It uses **FastAPI** for the backend and **React** for the frontend. The system retrieves relevant questions from a dataset, embeds them, and serves accurate responses via a chatbot interface.

---

## 📁 Project Structure

- `FQAs.csv` / `FQAs_cleaned.csv` – Original and cleaned airline FAQ dataset.
- `preprocessing.ipynb` – Preprocessing notebook to lowercase text and remove punctuation.
- `faq_data.npz` – Preprocessed data saved in `.npz` format for efficient loading.
- `embedding.py` – Script for converting questions into embeddings.
- `main.py` – FastAPI backend to serve the bot and answer user queries.
- `faq-bot-frontend/` – React frontend to interact with the FastAPI backend.
- `requirements.txt` – List of required Python packages.

---

## 🚀 How It Works

1. **Data Preparation**
   - Started with a dataset of 96 airline FAQs.
   - Preprocessed the text (lowercasing + punctuation removal).
   - Saved the processed data into `faq_data.npz` for easy loading.

2. **Embedding Script**
   - Used `embedding.py` to generate sentence embeddings for all FAQs.
   - These embeddings are used to find the most relevant question match.

3. **FastAPI Backend**
   - Built a RESTful API using FastAPI to:
     - Accept user queries.
     - Match the query with the most relevant FAQ.
     - Return the corresponding answer.

4. **React Frontend**
   - Created a simple React-based web interface to:
     - Allow users to type questions.
     - Display chatbot replies from the FastAPI backend.

---

## 🧰 Technologies Used

- **Python**, **NumPy**, **FastAPI**
- **Sentence Transformers / Embedding Models**
- **ReactJS**, **Axios**
- **VS Code**, **Git**, **GitHub**

---

## 📦 Installation

### Backend (FastAPI)
```bash
cd RAG-CHATBOT
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
```

### Frontend (React)
```bash
cd faq-bot-frontend
npm install
npm start
```
