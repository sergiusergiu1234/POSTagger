

import spacy


class TaggerService():
    def __init__(self):
        pass

    def tag(text: str = None):
        if text is not None:
            nlp = spacy.load("./output/model-best")
            doc = nlp(text)
            analysis = {
            "sentence": text,
            "tokens": [
                {
                    "word": token.text,
                    "tag": token.tag_
                }
                for token in doc
            ]
        }
            return analysis
            