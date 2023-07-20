#!/usr/bin/python
# -*- coding:utf-8 -*-

import spacy
from flask import request, jsonify, Flask
from db_util import getDbConnection
from weighting import setup as weighting_setup

import counter
import db_connector
import sentence_algorithm
from transcription import transcribe
import time

cursor = getDbConnection()
weighting_setup(cursor)
# load german spacy model
nlp = spacy.load("de_core_news_sm")
app = Flask(__name__)

def get_answer(question):
    # question is empty, respond with default message
    if question is None or len(question) == 0:
        return jsonify("This is the server of nao.")

    # annotes question with the german spacy model; adds tokens to words...
    processed_question = nlp(question)

    # removes irrelevant words and punctuation from question
    found_words = sentence_algorithm.sentence_detection(processed_question)

    # get generic form of each word
    for i, word in enumerate(found_words):
        found_words[i] = word.lower()
        wd = db_connector.get_generic_term(found_words[i], cursor)
        if wd is not None:
            found_words[i] = wd

    # based on weight of each word, get the caseID of the most relevant answer
    caseID = counter.count_ids(found_words, cursor)
    if caseID is None:
        return jsonify("Ich habe diese Frage nicht verstanden oder ich habe dazu leider keine Antwort.")

    # get answer with caseID from database
    answer = db_connector.get_answer(caseID, cursor)
    if answer is None:
        return jsonify("-1")

    return answer


@app.route('/', methods=['POST'])
def post_request():

    # get audio with question from POST request
    files = {'file': request.files['file']}

    # create binary file "audio" if it doesnt exist
    filename = "audio"
    with open(filename, 'wb') as f:
        f.write(files['file'].read())
    f.close()

    # measure time
    start = time.time()

    # get audio transcription from transcriber
    question = transcribe(filename)

    # measure time
    end = time.time()

    # print time
    print("--------------------")
    print("Time: " + str(end - start))
    print("Question: " + question)
    print("--------------------")

    return get_answer(question)
    
@app.route('/', methods=['GET'])
def get_request():
    question = request.args.get('question')

    print("--------------------")
    print("Question: " + question)
    print("--------------------")

    return get_answer(question)