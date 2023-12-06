# Wrapper for the Markov chain

import markovify
import re

# https://github.com/jsvine/markovify#extending-markovifytext
class Aqua(markovify.Text):
  re_punctuation = re.compile(r' ([.,?!;:’)…–-]|n’t)|([‘(]) ')
  re_ellipsis = re.compile(r'(?<=\W)(…) +')

  def word_join(self, words):
    sentence = ' '.join(word.split('::')[0] for word in words)
    # Discard extra space in between punctuation: Eat . Eat
    sentence = re.sub(self.re_punctuation, r'\1', sentence)
    # Discard extra space after … starts a sentences
    sentence = re.sub(self.re_ellipsis, r'\1', sentence)
    return sentence
