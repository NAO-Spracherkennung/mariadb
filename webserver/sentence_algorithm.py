from word import Word


# Funktion erhält den erkannten Satz und verarbeitet diesen pro Wort in einer Schleife.
# Danach wird das Wort genauestens untersucht. Am Ende wird der Originalsatz mit dem nun gekürzten Satz verglichen.
def sentence_detection(sentence):
    found_words = []

    for token in sentence:
        found_words = check_word(token, found_words)
    
    #Build list of words which can be returned
    words = []
    for word in found_words:
        words.append(Word.get_lemma(word))
    return words


# Als erstes wird der POS untersucht. Wenn einer der Fälle eintritt, wird das Wort nicht weiter beachtet,
# sondern in der Konsole mit einigen Daten ausgegeben. Kommt das Wort in keinen der Fälle,
# wird es in einer weiteren Funktion auf den TAG überprüft.
def check_word(token, found_words):
    if not (token.pos_ == "AUX" or token.pos_ == "PUNCT" or token.pos_ == "PART"):
        found_words = check_specific(token, found_words)
    return found_words


# Nach dem POS wird der TAG untersucht. Wenn einer der Fälle eintritt, wird das Wort nicht gespeichert,
# sondern in der Konsole mit einigen Daten ausgegeben. Kommt das Wort in keinen der Fälle wird es zusammen mit
# dem POS als Liste in die Liste "found_words" eingefügt.
def check_specific(token, found_words):
    if not (token.tag_ == "PPER" or token.tag_ == "ART" or token.tag_ == "ADJD" or token.tag_ == "PROAV"
            or token.tag_ == "PRF" or token.tag_ == "PIS" or token.tag_ == "VAFIN" or token.tag_ == "PPOSAT"
            or token.tag_ == "PDS"):
        new_word = Word(token.pos_, token.tag_, token.lemma_, token.dep_)
        found_words.append(new_word)

    return found_words