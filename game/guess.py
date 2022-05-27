from game.parachute import Parachute
class Guess:
    #Controls the guessed letters
    def __init__(self): #Lets the Class initialize the object's attributes.
        self._parachute = Parachute()
        self._guess  = ("_ " * len(self._parachute._word)) + "\n"
        self._letter = ""
        self._cut = "F"

    
    def update_guess(self, word): #Updates the underscores with correct letters
        if self._letter in word:
            index = word.index(self._letter)
            self._guess = self._guess[:(index * 2)] + self._letter + self._guess[(index * 2) + 1:]
            self._cut = "F"
        else:
            self._cut = "T"

    def check_guess(self, word): #Checks if the guessed letter is in the word.
        return ((self._guess.replace(" ", "")) == word)

    def get_guess(self): #Retrieves the guess
        return self._guess

    def set_letter(self, letter): #Sets the letter
        self._letter = letter
    
    def get_cut(self): #Initializes the parachute cut.
        return self._cut

    def check_victory(self, word): #Checks if the word has been completely guessed. (Currently Fails)
        # new = ''
        # for x in word:
        #     new += x
        # return new
       return word.replace(' ', '')
    