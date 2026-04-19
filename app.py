from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)

# Load model and vectorizer
with open('sentiment_model.pkl', 'rb') as f:
    clf = pickle.load(f)
with open('vectorizer.pkl', 'rb') as f:
    vectorizer = pickle.load(f)

# Define endpoint
@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    text = data['text']
    vec = vectorizer.transform([text])
    pred = clf.predict(vec)
    sentiment = 'Positive' if pred[0] == 1 else 'Negative'
    return jsonify({ 'sentiment': sentiment })

# Run app
if __name__ == '__main__':
    app.run(port=5000)