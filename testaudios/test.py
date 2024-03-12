from os import listdir
from os.path import isfile, join
import requests
import time

folder = '/Users/denis/dev/GitHub/nao/testaudios/male_age20_german/noisy/ohne_stopps'

onlyfiles = [f for f in listdir(folder) if isfile(join(folder, f))]

def transcribe():
    for file in onlyfiles:
        filename = folder + '/' + file
        with open(filename, 'rb') as f:
            start = time.time()
            r = requests.post('http://127.0.0.1:1222/', files={'file': f})
            r:dict = dict(r.json())
            end = time.time()
            print("--------------------")
            print("Question: " + file)
            print("Transcription:" + r['question'])
            print("Time: " + str(end - start))

transcribe()

#tiny: 0.3 sekunden