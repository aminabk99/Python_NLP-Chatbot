"""
Rule-Based NLP Chatbot
A simple chatbot demonstrating core NLP concepts: tokenization,
vocabulary filtering, unknown word handling, and rule-based response generation.
"""

import string
import random


# --- Vocabulary ---
# The set of words the chatbot recognizes. Any word outside this set
# is replaced with the [UNK] (unknown) token.

VOCABULARY = {
    "hello", "world", "how", "are", "you", "i", "am", "fine", "thank", "what",
    "is", "your", "name", "my", "bot", "good", "morning", "day"
}


# --- Co-Occurrence Map ---
# Defines which words can logically follow others.
# This acts as the chatbot's rule-based knowledge base.

CO_OCCURRENCE_MAP = {
    "hello":   ["how", "world", "there"],
    "how":     ["are", "is"],
    "are":     ["you"],
    "you":     ["today", "doing", "too"],
    "i":       ["am", "feel"],
    "am":      ["fine", "good"],
    "fine":    ["thank", "you"],
    "thank":   ["you"],
    "what":    ["is", "your"],
    "is":      ["your", "it"],
    "your":    ["name"],
    "my":      ["name"],
    "name":    ["is"],
    "bot":     ["hello"],
    "good":    ["morning", "day"],
    "morning": ["how"],
    "day":     ["how"],
}


def tokenize(text: str) -> list[str]:
    """
    Tokenize input text into a list of known words.

    Steps:
    1. Lowercase the input
    2. Strip punctuation
    3. Split into individual word tokens
    4. Replace any word not in the vocabulary with [UNK]
    """
    text = text.lower().translate(str.maketrans("", "", string.punctuation))

    return [
        word if word in VOCABULARY else "[UNK]"
        for word in text.split()
    ]


def generate_response(user_input: str) -> str:
    """
    Generate a response by mapping each recognized token to a
    related word using the co-occurrence map.

    Unknown tokens ([UNK]) are ignored.
    Returns a fallback message if no valid response can be built.
    """
    tokens = tokenize(user_input)

    response_words = [
        random.choice(CO_OCCURRENCE_MAP[token])
        for token in tokens
        if token != "[UNK]" and token in CO_OCCURRENCE_MAP
    ]

    return " ".join(response_words) if response_words else "I'm not sure how to respond to that."


def main():
    """Run the chatbot in an interactive loop."""
    print("Rule-Based NLP Chatbot")
    print("Type 'exit' to quit.\n")

    while True:
        user_input = input("You: ").strip()

        if not user_input:
            continue

        if user_input.lower() == "exit":
            print("Bot: Goodbye!")
            break

        print(f"Bot: {generate_response(user_input)}")


if __name__ == "__main__":
    main()
