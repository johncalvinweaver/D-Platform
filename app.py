from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "Welcome to D Platform: AI-Based Hiring Reimagined"

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    question = data.get("question", "")
    # Placeholder response
    return jsonify({
        "response": f"Agent received your question: '{question}' (AI logic will process this soon)."
    })

if __name__ == "__main__":
    app.run(debug=True)