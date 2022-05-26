import random
from words import word_list

class Parachute:

    def __init__(self):
        # self._word_list = []
        # self._word = self._word_list(random.randint(0, (len(self._word_list) - 1)))
        self._lives = 4
        self._parachute = []
        #We would have to put the parachute image above
    
    def _get_word():
        _word = random.choice(word_list)
        return _word.lower()
    
    # def word_spacing(_word):
    #   word_spacing = "_ " * len(_word)
    #   return word_spacing

    def word_as_list(_word, new_letter):
      word_spacing = "_ " * len(_word)
      word_as_list = [_word]
      indices = [i for i, letter in enumerate(_word) if letter == new_letter]
      for index in indices:
        word_as_list[index] == new_letter
      word_spacing = ''.join(word_as_list)
      return word_spacing
      


    def parachute(lives):
        parachute = [
# No Lives Lost
'''  
  ___
 /___\\
 \   /
  \ /
   O
  /|\\
  / \\
     
^^^^^^^''', 
# 1 Life Lost
'''
 /___\\
 \   /
  \ /
   O
  /|\\
  / \\
    
^^^^^^^''', 
# 2 Lives Lost
'''
 \   /
  \ /
   O
  /|\\
  / \\
     
^^^^^^^''', 
# 3 Lives Lost
'''
  \ /
   O
  /|\\
  / \\
     
^^^^^^^''', 
# Dead
'''
   O
  /|\\
  / \\
     
^^^^^^^''']
        for x in range(len(parachute)):
            print (parachute[x])

    def cut_line(self):
        #Removes a line from parachute if guess doesn't give a new letter
        return self.parachute.pop(0)