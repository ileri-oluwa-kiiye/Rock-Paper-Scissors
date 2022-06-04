from platform import system_alias
from random import *
from time import sleep
#Imported sleep for a break after each loop/game

print('Welcome to this game.')


sys_score = 0
your_score = 0

while True:
    """Loop for the player to continually choose R,P or S"""
    sleep(3) #A 3s break after each game
    
    
    print("\nType R, P or S for Rock, Paper, Scissors respectively\nType 'quit' to end game.")
    myself= input('Type here:')
    print('\n')
    
    list = ['R', 'P', 'S']  #List that contains every choice the computer can make.

   
    if myself.lower() == 'quit':
        """Break the loop if the player ends the game"""
        print("You've ended the game.")
        break
        
    
    
    if myself.upper() == 'R':
        #If the player chooses Rock
        computer = choice(list)
        print(f'Player(R) ; Computer({computer})')
        
    elif myself.upper() == 'P':
        #If the player chooses paper
        computer = choice(list)
        print(f'Player(P) ; Computer({computer})')
        
    elif myself.upper() == 'S':
        #if the player chooses Scissors
        computer = choice(list)
        print(f'Player(S) ; Computer({computer})')
        
    
    
    else:  
        print("\nError. Please type either 'R', 'P' or 'S'")
        """The error message for when the player dosent choose right."""
    
        
    win = ['R', 'P', 'S']
    lose = ['S', 'R', 'P']
    #The lists for the repective values to either win or lose i.e R wins S and P wins R
    
    x = -1
    for items in win:
        """Loop for when you win the game"""
        while x< 2:
            x += 1
            if myself.upper() == win[x]:
                if computer == lose[x]:
                    your_score += 1
    
    
    x = -1
    for items in win:
        """Loop for when the computer wins the game"""
        while x<2:
            x+=1
            if computer == win[x]:
                if myself.upper()== lose[x]:
                    sys_score+=1

    if myself.upper() == computer:
        print('It is a tie')
        sys_score +=0
        your_score+= 0

    print(f"Your score is {your_score}")
    print(f"The computer's score is {sys_score}")


print(f"Your final score = {your_score}")
print(f"The computer's final score is {sys_score}")
if sys_score> your_score:
    print('The computer wins!!')

elif sys_score == your_score:
    print('It ended as a tie. Replay to break the tie.')

else:
    print('You win! Congratulations!')