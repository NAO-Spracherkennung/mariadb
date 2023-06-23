#!/usr/bin/python
# -*- coding:utf-8 -*-

import os
import spacy
from flask import request, jsonify, Flask
from db_util import getDbConnection
from weighting import setup as weighting_setup

import counter
import db_connector
import sentence_algorithm
import requests

TRANSCRIBER_HOST = os.getenv("TRANSCRIBER_HOST", "127.0.0.1")
TRANSCRIBER_PORT = os.getenv("TRANSCRIBER_PORT", "5002")

cursor = getDbConnection()
weighting_setup(cursor)
app = Flask(__name__)




@app.route('/', methods=['GET'])
def get_request():
    question = request.args.get('question')
    if question is None or len(question) < 1:
        return jsonify("This is the server of nao.")
    nlp = spacy.load("de_core_news_sm")
    doc = nlp(question)
    found_words = sentence_algorithm.sentence_detection(doc)
    i = 0
    while i < len(found_words):
        found_words[i] = found_words[i].lower()
        wd = db_connector.get_generic_term(found_words[i], cursor)
        if wd is None:
            i += 1
            continue
        found_words[i] = wd
        i += 1
    caseID = counter.count_ids(found_words, cursor)
    if caseID is None:
        return jsonify("Ich habe diese Frage nicht verstanden oder ich habe dazu leider keine Antwort.")
    answer = db_connector.get_answer(caseID, cursor)
    if answer is None:
        return jsonify("-1")
    return answer


@app.route('/', methods=['POST'])
def post_request():

    url = 'http://'+TRANSCRIBER_HOST+':'+TRANSCRIBER_PORT+'/'
    files = {'file': request.files['file']}
    question = requests.post(url, files=files).text

    if question is None or len(question) < 1:
        return jsonify("This is the server of nao.")
    
    nlp = spacy.load("de_core_news_sm")
    doc = nlp(question)
    found_words = sentence_algorithm.sentence_detection(doc)
    i = 0
    while i < len(found_words):
        found_words[i] = found_words[i].lower()
        wd = db_connector.get_generic_term(found_words[i], cursor)
        if wd is None:
            i += 1
            continue
        found_words[i] = wd
        i += 1
    caseID = counter.count_ids(found_words, cursor)
    if caseID is None:
        return jsonify("Ich habe diese Frage nicht verstanden oder ich habe dazu leider keine Antwort.")
    answer = db_connector.get_answer(caseID, cursor)
    if answer is None:
        return jsonify("-1")
    return answer