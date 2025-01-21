import spacy
from spacy.training import Example
from spacy.tokens import DocBin
import json

# Paths
path_to_model = "./outputt2vv/model-best"
path_to_test_data = "./datasets/ro_rrt-ud-test.spacy"

# Load trained spaCy model
nlp = spacy.load(path_to_model)

# Load test dataset
doc_bin = DocBin().from_disk(path_to_test_data)
test_docs = list(doc_bin.get_docs(nlp.vocab))  # Convert to list of spaCy Docs

# Create Examples for evaluation
examples = [Example(nlp(doc.text), doc) for doc in test_docs]

# Evaluate using spaCy's built-in function
scores = nlp.evaluate(examples)

# Print results
print(json.dumps(scores, indent=2))
