import word


# Funktion erhält den erkannten Satz und verarbeitet diesen pro Wort in einer Schleife.
# Danach wird das Wort genauestens untersucht. Am Ende wird der Originalsatz mit dem nun gekürzten Satz verglichen.
def sentence_detection(sentence):
    global token
    global found_words
    
    found_words = []

    for token in sentence:
        check_word()
    
    #Build list of words which can be returned
    words = []
    for wd in found_words:
        words.append(word.Word.get_lemma(wd))
    return words


# Als erstes wird der POS untersucht. Wenn einer der Fälle eintritt, wird das Wort nicht weiter beachtet,
# sondern in der Konsole mit einigen Daten ausgegeben. Kommt das Wort in keinen der Fälle,
# wird es in einer weiteren Funktion auf den TAG überprüft.
def check_word():
    if not (token.pos_ == "AUX" or token.pos_ == "PUNCT" or token.pos_ == "PART"):
        check_specific()
    #else:
    #    print("Rausgeflogen wegen POS:"
    #          " \nText: " + token.text +
    #          " \nLemma: " + token.lemma_ +
    #          " \nPos: " + token.pos_ +
    #          " \nTag: " + token.tag_ +
    #          " \nDep: " + token.dep_ +
    #          " \n-----------------------")


# Nach dem POS wird der TAG untersucht. Wenn einer der Fälle eintritt, wird das Wort nicht gespeichert,
# sondern in der Konsole mit einigen Daten ausgegeben. Kommt das Wort in keinen der Fälle wird es zusammen mit
# dem POS als Liste in die Liste "found_words" eingefügt.
def check_specific():
    if not (token.tag_ == "PPER" or token.tag_ == "ART" or token.tag_ == "ADJD" or token.tag_ == "PROAV"
            or token.tag_ == "PRF" or token.tag_ == "PIS" or token.tag_ == "VAFIN" or token.tag_ == "PPOSAT"
            or token.tag_ == "PDS"):
        new_word = word.Word(token.pos_, token.tag_, token.lemma_, token.dep_)
        found_words.append(new_word)
    #else:
    #    print("Rausgeflogen wegen TAG:"
    #          " \nText: " + token.text +
    #          " \nLemma: " + token.lemma_ +
    #         " \nPos: " + token.pos_ +
    #          " \nTag: " + token.tag_ +
    #          " \nDep: " + token.dep_ +
    #          " \n-----------------------")
