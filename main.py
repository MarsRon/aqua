from fastapi import FastAPI
import markovify
import time
import uvicorn
from os import environ

app = FastAPI()
port = int(environ.get('PORT', 3000))

with open('./aqua.json', 'r') as file:
  aqua_model = markovify.Text.from_json(file.read())

@app.get('/')
def root():
  return {'endpoints': ['/aqua']}

@app.get('/aqua')
def aqua(short: bool = False):
  start = time.perf_counter()
  while True:
    if short == True:
      response = aqua_model.make_short_sentence(max_chars=50)
    else:
      response = aqua_model.make_sentence()
    if response is not None:
      break
  end = time.perf_counter()
  return {
    'response': response,
    'compute_time': end - start
  }

uvicorn.run(app, host='0.0.0.0', port=port)
