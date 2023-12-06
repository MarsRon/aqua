from aqua import Aqua
from time import perf_counter

# Constants
MODEL_FILE = "./aqua.json"
SHORT_SENTENCE_MAX_CHAR = 50
MARKOV_TRIES = 100

# Load Aqua model
print(f"Loading model file {MODEL_FILE}")
start = perf_counter()
with open(MODEL_FILE, 'r') as file:
  aqua = Aqua.from_json(file.read())
end = perf_counter()
print(f"Aqua model loaded in {(end-start)*1000:.3f}ms\n")

# Generate normal sentences
print("Normal sentences:")
for i in range(5):
  start = perf_counter()
  sentence = aqua.make_sentence(tries=MARKOV_TRIES)
  end = perf_counter()
  print(f"{i+1}. {sentence} ({(end-start)*1000:.3f}ms)")

print()

# Generate short sentences less than 50 characters
print("Short sentences:")
for i in range(5):
  start = perf_counter()
  sentence = aqua.make_short_sentence(
    max_chars=SHORT_SENTENCE_MAX_CHAR,
    tries=MARKOV_TRIES
  )
  end = perf_counter()
  print(f"{i+1}. {sentence} ({(end-start)*1000:.3f}ms)")
