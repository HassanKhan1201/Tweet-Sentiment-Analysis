from flask import Flask, render_template, request, jsonify
from utils.sentiment_analysis import analyze_sentiment

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.json
    tweet = data.get('tweet', '')
    sentiment = analyze_sentiment(tweet)
    return jsonify({'sentiment': sentiment})

if __name__ == '__main__':
    app.run(debug=True)
 