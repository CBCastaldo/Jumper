import random
from game.words import word_list

class Parachute:
    # Creates the ASCII art for the parachute, 

    def __init__(self): #Lets Class initialize the listed objects.
        self._word_list = word_list
        self._word = self._word_list[random.randint(0, (len(self._word_list) - 1))]
        self._lives = 4
        self._parachute = [ "  ___",
                            " /___\\",
                            " \   /",
                            "  \ /",
                            "   O",
                            "  /|\\",
                            "  / \\",
                            "      ",
                            "^^^^^^^"]
        self._game_over = ["   X",
                           "  /|\\",
                           "  / \\",
                           "^^^^^^^"]


    def cut_line(self, cut): #Cuts a line from the parachute.
        if cut == "T":
            self._lives = self._lives - 1
            self._parachute.pop(0)
        else:
            return 

    def get_parachute(self): #Draws the current Parachute
        if self._lives >= 1:
            return self._parachute
        else:
            return self._game_over

    def get_lives(self): #Retrieves the number of lives.
        return self._lives

    def get_word(self): #Retrieves the randomly chosen word.
        return list(self._word)
    