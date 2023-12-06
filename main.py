from os import environ
from time import perf_counter

from fastapi import FastAPI
import uvicorn
from aqua import Aqua

# Constants
PORT = int(environ.get('PORT', 3000))
MODEL_FILE = "./aqua.json"
SHORT_SENTENCE_MAX_CHAR = 50
MARKOV_TRIES = 100

app = FastAPI()

# Load Aqua model
with open(MODEL_FILE, 'r') as file:
  aqua_model = Aqua.from_json(file.read())

# Endpoints
@app.get('/')
def root():
  return {
    'endpoints': ['/aqua'],
    'author': 'MarsRon',
    'contact': 'marsron204@gmail.com'
  }

@app.get('/aqua')
def aqua(short: bool = False):
  start = perf_counter()
  if short:
    response = aqua_model.make_short_sentence(
      max_chars=SHORT_SENTENCE_MAX_CHAR,
      tries=MARKOV_TRIES
    )
  else:
    response = aqua_model.make_sentence(tries=MARKOV_TRIES)
  end = perf_counter()

  return {
    'response': response,
    'compute_time': end - start
  }

# Start the API server
uvicorn.run(app, host='0.0.0.0', port=PORT)
