const axios = require('axios');
require('dotenv').config();

const RASA_URL = process.env.RASA_URL || 'http://rasa:5005/model/parse';
const LLM_URL = process.env.LLM_URL || 'http://llm-runner:8000/generate';

// Given input text, call Rasa to get intent, then LLM for richer reply
async function aiRespond(text, storeId = '1') {
  // 1) Rasa parse
  let intent = null;
  try {
    const r = await axios.post(RASA_URL, {text});
    intent = r.data.intent.name;
  } catch (e) {
    console.error('Rasa parse failed', e.message);
  }

  // 2) If intent needs store check, call store API
  let storeState = null;
  try {
    const s = await axios.get(`${process.env.STORE_API || 'http://node-app:3000'}/stores/${storeId}`);
    storeState = s.data;
  } catch (e) {
    console.error('Store API failed', e.message);
  }

  // 3) Build prompt for LLM
  const prompt = `User said: "${text}"\nDetected intent: ${intent}\nStore state: ${JSON.stringify(storeState)}\nRespond concisely.`;
  const llmResp = await axios.post(LLM_URL, {prompt});
  return llmResp.data.text;
}

module.exports = { aiRespond };
