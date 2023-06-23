class Word:
    def __init__(self, pos, tag, lemma, dep):
        self.pos = pos
        self.lemma = lemma
        self.tag = tag
        self.dep = dep

    def get_lemma(self):
        return self.lemma

    def get_tag(self):
        return self.tag
