<div align="center">

# 🗣️ Python NLP Chatbot
### Rule-Based Natural Language Processing — No ML Required

A Python chatbot that demonstrates core NLP concepts: tokenization, vocabulary filtering,
unknown word handling, and rule-based response generation. No models, no APIs, no dependencies.

![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![NLP](https://img.shields.io/badge/NLP-Rule--Based-orange?style=for-the-badge)
![No Dependencies](https://img.shields.io/badge/Dependencies-None-brightgreen?style=for-the-badge)

</div>

---

## How It Works

1. User types a message → input is lowercased and stripped of punctuation
2. Each word is checked against a defined vocabulary
3. Unrecognized words are replaced with the `[UNK]` token
4. Known tokens are mapped through a co-occurrence table to generate a response
5. If no valid response can be built, a fallback message is returned

---

## NLP Concepts Demonstrated

| Concept | Description |
|---|---|
| **Tokenization** | Splitting input into individual word tokens |
| **Vocabulary Filtering** | Recognizing only a predefined set of known words |
| **Unknown Token Handling** | Replacing out-of-vocabulary words with `[UNK]` |
| **Co-Occurrence Mapping** | Rule-based word association used to generate responses |
| **Response Generation** | Building a reply by randomly selecting from mapped words |

---

## Example Interaction

```
You: hello how are you
Bot: how are today

You: what is your name
Bot: is your is

You: tell me a joke
Bot: I'm not sure how to respond to that.
```

The third input contains no vocabulary words, so all tokens become `[UNK]` and the fallback triggers.

---

## Setup

No installation required — uses only Python's standard library.

**Requirements:** Python 3.11+

```bash
git clone https://github.com/aminabk99/Python_NLP-Chatbot
cd Python_NLP-Chatbot
python chatbot.py
```

---

## Project Structure

```
Python_NLP-Chatbot/
├── chatbot.py       # All chatbot logic
└── README.md
```

---

## Limitations

This is an intentionally minimal implementation built for learning purposes. It has a small fixed vocabulary, no context or memory between turns, and responses are not grammatically structured. For a production chatbot, see tools like [Rasa](https://rasa.com) or LLM-based agents.

---

## Hardest Part
Keeping it simple on purpose. It's tempting to add ML or an API call — the challenge was demonstrating that meaningful NLP pipeline stages (tokenize → filter → map → respond) work even at a tiny scale.

## Most Interesting
The `[UNK]` token pattern. It mirrors how real neural NLP systems handle out-of-vocabulary words — this project shows the concept in ~60 lines of pure Python.

---

<div align="center">
  <sub>Built by <a href="https://github.com/aminabk99">Amina Bilal</a> · <a href="https://linkedin.com/in/amina-bilal-926340382">LinkedIn</a></sub>
</div>
