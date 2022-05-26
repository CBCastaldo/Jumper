import random

class Parachute:

    def __init__(self):
        self._word_list = []
        self._word = self._word_list(random.randint(0, (len(self._word_list) - 1)))
        self._lives = 4
        self._parachute = ""
        #We would have to put the parachute image above
    
    def parachute():
        parachute = ['''  
  ___
 /___\\
 \   /
  \ /
   O
  /|\\
  / \\
     
^^^^^^^''', '''
 /___\\
 \   /
  \ /
   O
  /|\\
  / \\
    
^^^^^^^''', '''
 \   /
  \ /
   O
  /|\\
  / \\
     
^^^^^^^''', '''
  \ /
   O
  /|\\
  / \\
     
^^^^^^^''', '''
   O
  /|\\
  / \\
     
^^^^^^^''']
        for x in range(len(parachute)):
            print (parachute[x])

    def cut_line(self):
        #Removes a line from parachute if guess doesn't give a new letter
        return 