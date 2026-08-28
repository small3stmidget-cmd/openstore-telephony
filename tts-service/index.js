const express = require('express');
const bodyParser = require('body-parser');
const TTS_URL = process.env.TTS_URL || 'http://tts-service:5100/synthesize';
const axios = require('axios');

const app = express();
app.use(bodyParser.json());

app.post('/synthesize', async (req, res) => {
  const text = req.body.text || '';
  try {
    // This example proxies to Coqui TTS, adapt to your TTS API
    const r = await axios.post(TTS_URL, {text}, {responseType: 'arraybuffer'});
    // For simplicity, return the TTS bytes as base64
    const base64 = Buffer.from(r.data, 'binary').toString('base64');
    res.json({audio_base64: base64});
  } catch (e) {
    console.error('TTS failed', e.message);
    res.status(500).json({error: 'tts_failed'});
  }
});

app.listen(5100, () => console.log('TTS proxy listening on 5100'));
