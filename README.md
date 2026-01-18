Rule-Based NLP Chatbot

## Overview
This project implements a simple **rule-based chatbot** in Python that demonstrates fundamental **Natural Language Processing (NLP)** concepts like **tokenization**, **vocabulary filtering**, and **response generation** with the use of predefined word co-occurrence rules.  

---

## How It Works

### Vocabulary Filtering
The chatbot recognizes only a predefined set of words.  
Any word outside this vocabulary is replaced with the special token **`[UNK]`**, mimicking how real NLP systems handle unknown input.

### Tokenization
User input is:
- Converted to lowercase  
- Stripped of punctuation  
- Split into individual word tokens  

### Co-Occurrence Mapping
A predefined **co-occurrence map** defines which words can logically follow others.  
This acts as the chatbot’s rule-based “knowledge base.”

### Response Generation
For each recognized word:
- A related word is randomly selected  
- Unknown tokens (`[UNK]`) are ignored  
- Selected words are concatenated to form a response  

If no valid response can be generated, a default message is returned.

---

## Features
- Rule-based chatbot logic (no machine learning)
- Tokenization with punctuation removal
- Unknown word handling using `[UNK]`
- Randomized response generation

---

## Technologies Used
- **Python 3**
- Standard Python libraries

