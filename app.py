from flask import Flask, request, jsonify
from sentiment_analysis import analyze_sentiment

app = Flask(__name__)

@app.route('/')
def home():
    return "Sentiment Analyzer API is running!"

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.json
    text = data.get('text', '')
    if not text:
        return jsonify({"error": "No text provided"}), 400

    sentiment = analyze_sentiment(text)
    return jsonify({"text": text, "sentiment": sentiment})

if __name__ == "__main__":
    app.run(debug=True)
