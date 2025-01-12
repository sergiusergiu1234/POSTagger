import spacy

# Load your trained model
nlp = spacy.load("./output/model-best")

# Define your custom sentences
sentences = [
    "Mingea  pe masa.",
    "II punem sare in mancare",
]

# Process each sentence and print the tokens with POS tags
for sentence in sentences:
    doc = nlp(sentence)
    print(f"Sentence: {sentence}")
    print("Tokens and POS tags:")
    for token in doc:
        print(f"{token.text:15} {token.pos_:10} {token.tag_}")
    print("\n")
