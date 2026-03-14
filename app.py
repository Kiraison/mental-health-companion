from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json["message"]

    if "sad" in user_message.lower():
        response = "I'm sorry you're feeling sad. Try taking a deep breath and talking to someone you trust."
    else:
        response = "I'm here to listen. Tell me more."

    return jsonify({"reply": response})

if __name__ == "__main__":
    app.run(debug=True)
    