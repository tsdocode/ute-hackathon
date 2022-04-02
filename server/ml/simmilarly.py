import spacy

class Simmilarly:
    def __init__(self):
        self.nlp = spacy.load('en_core_web_sm')

    def predict(self, text1, text2):
        doc1 = self.nlp(text1)
        doc2 = self.nlp(text2)
        return doc1.similarity(doc2)
