# from game.parachute import Parachute

class Guess:

    def __init__(self):
        # self._guess = "_ " * len(word)
        self._guess = "_ _ _ _ _"
        return 
    
    def update_guess(self, parachute):
        # Here is where we would keep track of words that were correct among the guess
        return

    def get_guess(self):
        guess = input('Guess a letter [a-z]: ').lower()
        return guess

    