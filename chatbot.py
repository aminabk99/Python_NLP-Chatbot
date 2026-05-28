import string
import random


# 1. Define a vocabulary (words the bot understands)
vocabulary = {
    "hello", "world", "how", "are", "you", "i", "am", "fine", "thank", "what",
    "is", "your", "name", "my", "bot", "good", "morning", "day"
}

# 2. Tokenize input text
def tokenize_text(text):
    # Convert to lowercase
    text = text.lower()

    # Remove punctuation
    translator = str.maketrans('', '', string.punctuation)
    text = text.translate(translator)

    # Split into words
    words = text.split()

    # Replace unknown words with [UNK]
    tokenized_words = []
    for word in words:
        if word in vocabulary:
            tokenized_words.append(word)
        else:
            tokenized_words.append("[UNK]")

    return tokenized_words


# 3. Define a co-occurrence map 
co_occurrence_map = {
    "hello": ["how", "world", "there"],
    "how": ["are", "is"],
    "are": ["you"],
    "you": ["today", "doing", "too"],
    "i": ["am", "feel"],
    "am": ["fine", "good"],
    "fine": ["thank", "you"],
    "thank": ["you"],
    "what": ["is", "your"],
    "is": ["your", "it"],
    "your": ["name"],
    "my": ["name"],
    "name": ["is"],
    "bot": ["hello"],
    "good": ["morning", "day"],
    "morning": ["how"],
    "day": ["how"]
}


# 4. Generate a response based on user input
def generate_response(prompt):
    tokenized_prompt = tokenize_text(prompt)
    generated_words = []

    for token in tokenized_prompt:
        if token != "[UNK]" and token in co_occurrence_map:
            generated_words.append(random.choice(co_occurrence_map[token]))
        elif token != "[UNK]":
            generated_words.append(token)
        # [UNK] tokens are ignored

    # Return response
    if generated_words:
        return " ".join(generated_words)
    else:
        return "I'm not sure how to respond to that."


# 5. Main program loop
def main():
    print("Rule-Based Chatbot")
    print("Type 'exit' to quit.\n")

    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            print("Bot: Goodbye!")
            break

        response = generate_response(user_input)
        print("Bot:", response)


# 6. Run the chatbot
if __name__ == "__main__":
    main()
