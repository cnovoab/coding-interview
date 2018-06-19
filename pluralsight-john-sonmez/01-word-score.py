# Word score
# ---------------------------------------------------------------------------------
# You are tasked with writing the scoring algorithm for a simple word game. In this
# game, players will submit their word and receive back the score of their word. The
# goal of the game is for the players to try and figure out how to make the highest
# scoring words based on the scores they are getting back.
#
# - In order to score a word, you will add up the point value of each letter in the word.
# - The word doesn't have to be a real word, just a string of characters.
# - The scoring system for the game is:
# F = 3, J = 6, X = 12, A, I, E, O = 2, T = 5 and all other letters are 0.
# - It does not matter if the letter is upper or lower case.
# - You can ignore any non letter input in the string and assume the string will be at
# most 50 characters long.

import sys
scores = {
      'f': 3,
      'j': 6,
      'x': 12,
      'a': 2,
      'e': 2,
      'i': 2,
      'o': 2,
      't': 5
}

def score_word(word):
    return sum([scores.get(i, 0) for i in word])

word = str(sys.argv[1]).lower()
score = score_word(word)
print("The score for the word {} is: {}".format(word, str(score)))
