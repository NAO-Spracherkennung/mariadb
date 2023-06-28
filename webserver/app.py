#!/usr/bin/python
# -*- coding:utf-8 -*-

import spacy
from flask import request, jsonify, Flask
from db_util import getDbConnection
from weighting import setup as weighting_setup

import counter
import db_connector
import sentence_algorithm
import whisper
from transcription import transcribe

cursor = getDbConnection()
weighting_setup(cursor)
# load german spacy model
nlp = spacy.load("de_core_news_sm")
whisper_model = whisper.load_model("base")
app = Flask(__name__)


@app.route('/', methods=['POST'])
def post_request():

    # get audio with question from POST request
    files = {'file': request.files['file']}

    # save file to disk
    filename = "audio"
    with open(filename, 'wb') as f:
        f.write(files['file'].read())

    # get audio transcription from transcriber
    question = transcribe(filename, whisper_model)

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
