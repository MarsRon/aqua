import markovify
from time import time

MODEL_FILE = "./aqua.json"

print(f"Loading model file {MODEL_FILE}")
start = time()
with open(MODEL_FILE, 'r') as file:
  aqua = markovify.Text.from_json(file.read())
end = time()
print(f"Aqua model loaded in {(end-start)*1000:.3f}ms\n")

# Generate sentences
print("Generate sentences")
for i in range(5):
  start = time()
  sentence = aqua.make_sentence()
  end = time()
  print(f"{i+1}. {(end-start)*1000:.3f}ms: {sentence}")

print()

# Generate short sentences less than 50 characters
print("Generate short sentences")
for i in range(5):
  start = time()
  sentence = aqua.make_short_sentence(max_chars=50)
  end = time()
  print(f"{i+1}. {(end-start)*1000:.3f}ms: {sentence}")
