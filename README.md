<div align="center">

# 🤖 Rule-Based NLP Chatbot
### Tokenization, Vocabulary Filtering, and Co-Occurrence Response Generation — No ML Required

A Python chatbot that demonstrates core **Natural Language Processing** concepts from scratch — tokenizing input, filtering unknown words with `[UNK]`, and generating responses using a **predefined co-occurrence map** — all without any machine learning library.

![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![NLP](https://img.shields.io/badge/NLP-Rule--Based-FF6600?style=for-the-badge&logo=openai&logoColor=white)
![No ML](https://img.shields.io/badge/No_ML-Pure_Logic-4CAF50?style=for-the-badge&logo=python&logoColor=white)
![Console](https://img.shields.io/badge/Interface-Console-555555?style=for-the-badge&logo=windowsterminal&logoColor=white)

</div>

---

## How It Works

1. User types a message into the console
2. Input is **lowercased** and **stripped of punctuation**, then split into tokens
3. Each token is checked against a fixed vocabulary — unknown words become **`[UNK]`** and are ignored
4. For each recognized word, a related word is randomly selected from a **co-occurrence map**
5. The selected words are joined and returned as the bot's response
6. If no recognized words are found, a default fallback message is returned

**NLP concepts covered:** 🔤 Tokenization · 📖 Vocabulary filtering · 🔗 Co-occurrence mapping · ❓ Unknown word handling

---

## Setup

**Requirements:** Python 3.11+ · No external libraries needed

**1. Clone & run**
```bash
git clone https://github.com/aminabk99/Python_NLP-Chatbot
cd Python_NLP-Chatbot
python chatbot.py
```

**Example interaction:**
```
You: hello how are you
Bot: how fine you
You: what is your name
Bot: is name your
You: xyz123
Bot: I'm not sure how to respond to that.
```

---

## Hardest Part
**Keeping the co-occurrence map coherent** — it's easy to add word pairs that produce grammatically nonsensical responses. Deciding which words logically follow others, and making sure the map covers enough of the vocabulary to generate useful output, required more thought than expected for such a small system.

## Most Interesting
**The `[UNK]` token** — replacing out-of-vocabulary words with a special token rather than crashing or ignoring input is a technique used in production LLMs at massive scale. Implementing it manually here makes the concept tangible: the model simply has no representation for words it has never seen.

---

## Files

- `chatbot.py` — full chatbot implementation (tokenizer, co-occurrence map, response generator, main loop)
- `README.md` — project overview

---

<div align="center">
  <sub>Built by <a href="https://github.com/aminabk99">Amina Bilal</a> · <a href="https://linkedin.com/in/amina-bilal-926340382">LinkedIn</a></sub>
</div>
