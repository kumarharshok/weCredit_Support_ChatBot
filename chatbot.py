from flask import Flask, request, jsonify, render_template
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=API_KEY)

app = Flask(__name__)

def chatbot_response(prompt):
    model = genai.GenerativeModel("gemini-pro")

    # Instruction to Gemini to check if the question is finance-related
    filter_prompt = (
        f"Determine if the following question is related to finance, banking, investments, "
        f"loans, credit, or money management. "
        f"Answer only 'YES' if it's finance-related, otherwise answer 'NO'.\n\n"
        f"Question: {prompt}"
    )

    filter_response = model.generate_content(filter_prompt).text.strip().upper()

    if filter_response == "YES":
        short_prompt = f"Question: {prompt}\nAnswer (max 15 words):"
        response = model.generate_content(short_prompt, generation_config={
            "max_output_tokens": 25,
            "temperature": 0,
        })
        return response.text.strip()
    else:
        return "I'm a financial support chatbot. Please ask finance-related questions."

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json()
    user_question = data.get("question", "")

    if not user_question:
        return jsonify({"error": "Please provide a valid question"}), 400

    answer = chatbot_response(user_question)
    return jsonify({"answer": answer})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

