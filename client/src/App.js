import { useState } from 'react';
import axios from 'axios';

function App() {
  const [text, setText] = useState('');
  const [sentiment, setSentiment] = useState('');
  const [emoji, setEmoji] = useState('');
  const handleSubmit = async () => {
    const response = await axios.post('http://localhost:3001/api/sentiment',{text});                                         
    const sent = response.data.sentiment;
    setSentiment(sent);
    setEmoji(sent === 'Positive' ? '😊' : '😔');
  };
  return (
    <div>
      <textarea value={text} onChange={(e) => setText(e.target.value)} />
      <button onClick={handleSubmit}>Check Sentiment</button>
      <p>Sentiment: {sentiment} {emoji}</p>
    </div>
  );
}
export default App;