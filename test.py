import markovify

with open('./aqua.json', 'r') as file:
  aqua = markovify.Text.from_json(file.read())

# Generate sentences
for i in range(5):
  print(aqua.make_sentence())

print()

# Generate short sentences less than 50 characters
for i in range(5):
  print(aqua.make_short_sentence(max_chars=50))
