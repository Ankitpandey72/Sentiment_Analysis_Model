# Sentiment_Analysis_Model
This is Sentiment Analysis Model Project Which Predict the review of Movies is positive or negative using Pyhton integrated with React and Node.

# Sentiment Analysis Model

## Overview
A sentiment analysis model built with Python and Flask, integrated with a React.js frontend and Node.js backend. The model analyzes input text and returns a positive or negative sentiment.

## Tech Stack
- **Model**: Python, Flask
- **Backend**: Node.js, Express.js
- **Frontend**: React.js

## Architecture
1. **Python Model (Flask)**: Analyzes sentiment of input text
2. **Node.js Backend**: Acts as a bridge between Flask API and React frontend
3. **React.js Frontend**: Takes user input and displays sentiment result

## API Endpoints
- `POST /api/analyze` (Node.js): Forwards request to Flask API
- `POST /analyze` (Flask): Analyzes sentiment of input text
  - Request Body: `{ text: string }`
  - Response: `{ sentiment: 'positive' | 'negative' }`

## Setup
1. Clone the repo
2. run sentiment.py
2. **Flask Model**:
   - `pip install -r requirements.txt`
   - `python app.py`
3. **Node.js Backend**:
   - `cd mern-sentiment`
   - `npm install`
   - `node server.js` or `npm run dev`
4. **React.js Frontend**:
   - `cd client`  `note:- if you are in mern-sentiment then cd ..`
   - `npm install`
   - `npm start`

## Usage
1. Open the app in your browser
2. Enter text in the input field
3. Click "Analyze" to see the sentiment result (positive or negative)
