import random
from words import word_list

class Parachute:

    def __init__(self):
        # self._word_list = []
        # self._word = self._word_list(random.randint(0, (len(self._word_list) - 1)))
        self._lives = 4
        self._parachute = []
        #We would have to put the parachute image above
    
    def get_word():
        word = random.choice(word_list)
        return word.lower()

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