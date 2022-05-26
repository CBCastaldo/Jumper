# from game.parachute import Parachute
from pickle import FALSE


class Guess:

    def __init__(self):
        # self._guess = "_ " * len(word)
        self._guess = False
        return 
    
    def update_guess(self, parachute):
        # Here is where we would keep track of letters that were correct among the guess
        pass

    def word_as_list(_word, new_letter):
      word_spacing = "_ " * len(_word)
      word_as_list = [_word]
      indices = [i for i, letter in enumerate(_word) if letter == new_letter]
      for index in indices:
        word_as_list[index] == new_letter
      word_spacing = ''.join(word_as_list)
      return word_spacing

    def get_guess(self):
        guess = input('Guess a letter [a-z]: ').lower()
        return guess

    