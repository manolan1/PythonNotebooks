
"""
    Script name: prophecy.py
       Function: User is as for a question. Then a random string from
                 the list prophecies is returned. (The question is
                 never used in the script.)
"""

import random

prophecies = ['It is certain', 'It is decidedly so', 'Yes definitely', 
              "Reply hazy try again",'Ask again later', 
              'Concentrate and ask again', "My reply is no", 
              "The outlook not so good", "Very doubtful"]

question = input("What is your question? ")

answer_selection = random.randint(0, len(prophecies) -1)
print("Prophecy from the Oracle: ", prophecies[answer_selection])
