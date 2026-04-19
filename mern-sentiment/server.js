const express = require('express');
const axios = require('axios');
const app = express();
app.use(express.json());
const cors = require('cors');
app.use(cors());

app.post('/api/sentiment', async (req, res) => {
  try {
    const { text } = req.body;
    const response = await axios.post('http://127.0.0.1:5000/predict', { text });
    res.json(response.data);
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});


app.listen(3001, () => console.log('Server on 3001'));