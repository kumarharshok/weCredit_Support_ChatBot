
# WeCredit Support Chatbot  

## 📌 Project Overview  
The **WeCredit Support Chatbot** is a finance-related chatbot built using **Flask** and **Google Gemini AI**. It helps users with finance-related queries, such as banking, loans, investments, and credit. The chatbot strictly answers only finance-related questions.  

🔗 **Live URL:** [WeCredit Chatbot](https://wecredit-support-chatbot.onrender.com)  

---

## 🛠️ Technologies Used  

### Frontend  
- **HTML, CSS, JavaScript** → To create the chatbot UI.  
- **Fetch API** → To send user queries to the backend.  

### Backend  
- **Python (Flask)** → To create a web server.  
- **Google Gemini AI** → To generate intelligent chatbot responses.  
- **Render** → For deployment.  

---

## 🚀 Features  
✔️ **Finance-Specific Responses:** Only answers finance-related queries.  
✔️ **AI-Powered Chatbot:** Uses **Google Gemini AI** for generating responses.  
✔️ **Interactive UI:** A simple and responsive chatbot interface.  
✔️ **Real-Time Communication:** Users can chat, and responses appear instantly.  

---

## 🔧 How to Run Locally  

### 1️⃣ Clone the Repository  
```bash
git clone https://github.com/your-repo/wecredit-chatbot.git
cd wecredit-chatbot
```

### 2️⃣ Install Dependencies  
```bash
pip install -r requirements.txt
```

### 3️⃣ Set Up API Key  
Create a `.env` file and add:  
```
API_KEY=your_google_gemini_api_key
```

### 4️⃣ Run the Flask App  
```bash
python chatbot.py
```
The chatbot will be available at:  
🔗 **http://127.0.0.1:5000/**  

---

## 📄 API Endpoints  

| Method | Endpoint  | Description |
|--------|----------|-------------|
| GET    | `/`      | Loads the chatbot UI |
| POST   | `/ask`   | Sends user query to the AI model and returns a response |

---

## 🏗️ Deployment  
The chatbot is deployed on **Render**.  
- **Hosting:** Flask app hosted on **Render**.  
- **Frontend & Backend:** Integrated in a single Flask project.  

---

## 📢 Future Improvements  
- Support for more finance-related topics.  
- Improve UI with better animations.  
- Allow users to view chat history.  

---

Let me know if you need any modifications! 🚀
