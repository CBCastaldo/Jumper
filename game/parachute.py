import random
from game.words import word_list

class Parachute:

    def __init__(self):
        self._word_list = word_list
        # self._word_list = ['clock', 'fat', 'waist', 'locate', 'bathtub']
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


    def cut_line(self, cut):
        if cut == "T":
            self._lives = self._lives - 1
            self._parachute.pop(0)
        else:
            return 

    def get_parachute(self):
        if self._lives >= 1:
            return self._parachute
        else:
            return self._game_over

    def get_lives(self):
        return self._lives

    def get_word(self):
        return list(self._word)
    