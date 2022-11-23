#rock paper scissors game
#started on 06/08/2022 1330
#finished on  

#Requirements:
#Display rules of the game at the start
#Computer has to randomly pick from rock paper scissors
#score has to be assigned to winner of each 'throw'
#make an option for best of 3, best of 5, upto 3 and upto 5
#Need to be able to compare user input against computer's random choice
# give option to play again after best of / upto option is complete 


#Attempt 1
#    import random
# 
#   user_score = 0
#  computer_score = 0
#
#     game_list = ['Rock', 'Paper', 'Scissors']
#
#
#   random_computer_choice = random.choice(game_list)


#    user_input = None

#    while user_input not in game_list:
#        user_input = input('Pick an option: Rock, Paper or Scissors \n').capitalize()

#    if user_input == random_computer_choice:
#        print ('Computer chose: ' + random_computer_choice)
#        print ('Tie')


#    elif user_input == 'rock' and random_computer_choice == 'paper':
#        print ('Computer chose: ' + random_computer_choice)
#        print ('Paper beats Rock, \n You lose!')
#        computer_score =+1
        
#    elif user_input == 'paper' and random_computer_choice == 'rock':
#        print ('Computer chose: ' + random_computer_choice)
#        print ('Paper catches rock \n You win ')
#        user_score =+ 1 
        
#    else:
#        user_input == 'paper' and random_computer_choice == 'scissors'
#        print ('Computer chose: ' + random_computer_choice)
#        print ('Scissors cuts paper. \n You Lose!')

#    print('Computer_score is:'+ str(computer_score))

#    print('User_score is:' + str(user_score))


# The and function is causing problems, will have to do individual if/elif statements. (Start was fine though, uptill line 33)
# And function requires both to be tru. If one is true, and other isnt, it prdocues a weird answer e.g.

#Pick an option: Rock, Paper or Scissors 
#rock
#Computer chose: Paper
#Scissors cuts paper.
# You Lose!
#Computer_score is:0
#User_score is:0

#Attempt 2 

import random

print("""Welcome to the game, The aim of the game is simple,
Gain enough points against the computer and you will win. Each throw won, counts as one point.
If the computer wins the required number of points before you,
You lose!""")




choices = ['a','b','c','d','e']

choice = True
starting = None

while starting not in choices:
    starting = input ("Select the letter corresponding to the number of rounds you would like to play \n A) Upto 3 Points \n B) Upto 5 Points \n C) Best of 3 \n D) Best of 5 \n E) 1 Round \n").lower()
    
if starting == 'a':
    print (' You have selected: Upto 3 Points')

elif starting == 'b':
    print (' You have selected: Upto 5 Points') 
      
elif starting == 'c':
    print (' You have selected: Best of 3')
    
elif starting == 'd':
    print (' You have selected: Best of 5')
    
else:
    starting == 'e'
    print ( ' You have selected: 1 Round ')
   

user_score = 0
computer_score = 0


while True:

    game_list = ['ROCK', 'PAPER', 'SCISSORS']

    random_computer_choice = random.choice(game_list)

    user_input = None

    while user_input not in game_list:
        user_input = input('Pick an option: Rock, Paper or Scissors \n').upper()

    if user_input == random_computer_choice:
        print ('Computer chose: ' + random_computer_choice)
        print ('Tie')
        print ('Player score is' ,user_score)
        print ('Computer Score is', computer_score)

    else:
        user_input != random_computer_choice
        if user_input == 'PAPER':
            print ('You have picked ' , user_input)
            print ('Computer picked ' , random_computer_choice)
            if random_computer_choice == 'SCISSORS':
                print('Computer wins: Scisors cuts Paper')
                computer_score += 1
                print ('Computer Score is ', computer_score)
            elif random_computer_choice == 'ROCK':
                print ('Player wins: Paper catches Rock')
                user_score += 1
                print ('Player score is ' ,user_score)
        elif user_input == 'ROCK':
            print ('You have picked', user_input)
            print ('Computer picked' , random_computer_choice)
            if random_computer_choice == 'SCISSORS':
                print('Player wins: Rock destroys Scissors')
                user_score += 1
                print ('Player score is' ,user_score)
            elif random_computer_choice == 'PAPER':
                print ('Computer wins: Paper catches Rock')
                computer_score += 1
                print ('Computer Score is', computer_score)
        else:
            user_input == 'SCISSORS'
            print ('You have picked',  user_input)
            print ('Computer picked' , random_computer_choice)
            if random_computer_choice == 'PAPER':
                print('Player wins: Scissors cuts Paper')
                user_score += 1
                print ('Player score is' ,user_score)
            elif random_computer_choice == 'ROCK':
                print ('Computer wins: Rock destroys Scissors ')
                computer_score += 1
                print ('Computer Score is', computer_score)


            if user_score == 3  or computer_score == 3 and starting == 'a':
                print ('Player score:', user_score)
                print ('Computerscore:', computer_score)
                again = input('Would you like to play again? \n Yes or No? \n').lower()
                if again != 'yes':
                    break
            elif user_score or computer_score != 5 and starting == 'b':
                print ('Player score:', user_score)
                print ('Computerscore:', computer_score)
                continue
            elif user_score == 2 and starting == 'c':
                print ('Player score:', user_score)
                print ('Computerscore:', computer_score)
                print('You win!')
                break
            else: 
                user_score == 3 and starting == 'd'
                print ('Userscore:', user_score)
                print ('Computerscore:', computer_score)
                print('You win!')
                break


print(' Thank you for playing! \n Bye!')

# Code is not finished. Desired function ' upto 3/5 and best of 3/5 does not work 
# Will take a few days before coming back to it.
#But overall the code is fine, it keeps track of score, but does not lead 
#an end unless the code is manually stopped.

#Date: 06/08/22
