from game.guess import Guess
from game.parachute import Parachute
from game.service import Service
# _word = self._parachute._get_word

class Director:
    def __init__(self):
        self._is_playing = True
        self._guess = Guess()
        self._parachute = Parachute()
        self._service = Service()
        _new_word = self._parachute._get_word

    def start_game(self):
        while self._is_playing:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()


    def get_inputs(self):
        #Shows guess status
        print(self._parachute.word_as_list)
        #Shows parachute status
        print(self._parachute.parachute[0])
        #prompts guess
        new_letter = self._guess.get_guess()
        return new_letter

    def do_updates(self, new_letter, _new_word):
        #Checks if letter was in word
        while not self._guess._guess and self._parachute._lives > 0:
            if len(new_letter) == 1 and new_letter.isalpha():
                if new_letter in self._service.guessed_letters():
                    print(f'You have already guessed the letter {new_letter}.')
                elif new_letter not in self._parachute._get_word():
                    print(f'{new_letter} is not in the word.')
                    self._parachute._lives -= 1
                    self._service.guessed_letters.append(new_letter)
                else:
                    print(f'Good guess! {new_letter} is in the word!')
                    self._service.guessed_letters.append(new_letter)
                    self._parachute.word_as_list(_new_word, new_letter)
                    if '_' not in self._parachute.word_as_list:
                        self._guess._guess = True

        return

    def do_outputs(self):
        #Updates lives accordingly
        #Updates parachute image
        #Checks if game is over
        return