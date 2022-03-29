#!/usr/bin/env python3
#Github: https://github.com/robertbaer-hetzner
#Autor: Robert Baer

# Game : hangman

# imports

# classes 

# functions

import random

def level_building(level):
    with open('words.txt', 'r') as file:
        wordlist = file.readline().split()    
    word_secret = random.choice(wordlist)
    while len(word_secret) != 2*int(level):
        word_secret = random.choice(wordlist)
    return word_secret;


levels = [ 

"""
   _________
    |/        
    |              
    |                
    |                 
    |               
    |                   
    |___                 
""",

"""
   _________
    |/   |      
    |              
    |                
    |                 
    |               
    |                   
    |___                 
""",

"""
   _________       
    |/   |              
    |   (_)
    |                         
    |                       
    |                         
    |                          
    |___                       
""",

"""
   ________               
    |/   |                   
    |   (_)                  
    |    |                     
    |    |                    
    |                           
    |                            
    |___                    
""",


"""
   _________             
    |/   |               
    |   (_)                   
    |   /|                     
    |    |                    
    |                        
    |                          
    |___                          
""",


"""
   _________              
    |/   |                     
    |   (_)                     
    |   /|\                    
    |    |                       
    |                             
    |                            
    |___                          
"""
"""
   ________                   
    |/   |                         
    |   (_)                      
    |   /|\                             
    |    |                          
    |   /                            
    |                                  
    |___                              
""",
"""
   ________
    |/   |     
    |   (_)    
    |   /|\           
    |    |        
    |   / \        
    |               
    |___   
"""

]

#START
if __name__ == "__main__":
    
    print("Welcome to Hangman! Please enter your name.")
    input_name = input("Name: ")
    print("And now the level difficulty.")
    input_level = input("Level 1 - 5 : ")
    print("Let the game begin!")

    word = level_building(input_level)
    word_underline = ""
    for x in range(len(word)):
        word_underline += " _ "
    word_underline.split()
    word_split = word.split()
    guess_word= ""
    counter = 0
    while counter < len(levels) or word != guess_word:
        print(levels[0] + "\n" + word_underline)
        guess = input("Your guess: ")
        for letter in word_split:
            if letter = guess:
                
        counter += 1


    
