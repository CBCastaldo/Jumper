from game.guess import Guess
from game.parachute import Parachute
from game.service import Service

class Director: #Directs the game.
    def __init__(self): #Lets the Class initialize the object's attributes.
        self._is_playing = True
        self._guess = Guess()
        self._parachute = Parachute()
        self._service = Service()
        # self._guess.check_victory == False
        # self.victory = self._guess.check_victory(self._parachute._word)
        self._prompt = "Guess a letter [a-z]: "
        self._game_over = "Game Over"
        self._victory = "Congratulations! You win!"

    def start_game(self): #Tells the game while functions to run while the game is running.
        while self._is_playing:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()

    def get_inputs(self): #Gathers the guess input
        self._service.read_letter(self._guess.get_guess())
        self._service.print_list(self._parachute.get_parachute())
        letter = input(self._prompt)
        if len(letter) != 1:
            print('Please enter a single letter.')
            letter = input(self._prompt)
        elif letter.isalpha() == False:
            print('Please enter a letter.')
            letter = input(self._prompt)
        self._guess.set_letter(letter)
        self._guess.check_victory(self._guess._guess)

    def do_updates(self): #Updates the underscored word with the inputed letter.
        self._guess.update_guess(self._parachute.get_word())
        self._parachute.cut_line(self._guess.get_cut())
        # self._guess.check_victory(self._guess._guess)

    def do_outputs(self): #Ends the game if lives are completely used, Ends the game if won (Fails), keeps the game running and sends it back for another input.
        # while self._guess.check_victory(self._parachute._word) == False:
        if self._parachute.get_lives() == 0:
            self._service.read_letter(self._game_over)
            self._service.print_list(self._parachute.get_parachute())
            self._is_playing = False

        # elif self._guess.check_victory(self._parachute._word) == True:
        #     self._service.read_letter(self._victory)
        #     self._is_playing = False
            

        # elif self._guess.check_guess(self._parachute.get_word()):
        #     self._is_playing = True
        #     self._service.read_letter(self._guess.get_guess())
        elif self._guess.check_victory(self._guess._guess) == self._parachute._word:
            self._service.read_letter(self._victory)
            self._is_playing = False
        else:
            self._is_playing = True
        # else:
        #     self._service.read_letter(self._victory)
        #     self._is_playing = False