import spacy

# Load your trained model
nlp = spacy.load("./modelMorfologizerAndTokenizer/model-best")

# Define your custom sentences
sentences = [
    "Mingea sare pe masa.",
    "Am pus sare in ciorba."
    "Nicu casca ca un bou",
    "E bine sa porti casca pe santier."

]

# Process each sentence and print the tokens with POS tags
for sentence in sentences:
    doc = nlp(sentence)
    print(f"Sentence: {sentence}")
    # print("Tokens and POS tags:")
    
    for token in doc:
        
        print(f"{token.text:15} {token.pos_} {token.tag_}")
        print("\n")
