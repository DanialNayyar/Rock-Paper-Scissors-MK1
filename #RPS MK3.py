#RPS MK3

#Requirements:
#Display rules of the game at the start
#Computer has to randomly pick from rock paper scissors
#score has to be assigned to winner of each 'throw'
#make an option for best of 3, best of 5, upto 3 and upto 5
#Need to be able to compare user input against computer's random choice
# give option to play again after best of / upto option is complete 
# Code is not finished. Desired function ' upto 3/5 and best of 3/5 does not work 
# Will take a few days before coming back to it.
#But overall the code is fine, it keeps track of score, but does not lead 
#an end unless the code is manually stopped.




import random
import sys

print("""Welcome to the game, The aim of the game is simple,
Gain enough points against the computer and you will win. Each throw won, counts as one point.
If the computer wins the required number of points before you,
You lose!""")

choices = ['a', 'b', 'c', 'd' ]

starting = None

while starting not in choices:
    starting = input (" Select the letter corresponding to the number of rounds you would like to play. \n A) Up to 3 points \n B) Upto 5 points \n C) Best of 3 Points \n D) Best of 5 Points \n" ).lower()


if starting  == 'a':
    print( "You have selected: Upto 3 points ")
elif starting == 'b':
    print( "You have selected: Upto 5 points ")     
elif starting == 'c':
    print( "You have selected: Best of 3 points")
elif starting == 'd':
    print( "You have selected: Best of 5 points")


# use conditionals to call functions at the end
if starting == 'a':
    start = 3
elif starting == 'b':
    start = 5
elif starting =='c':
    starts = 3



#print ("Starting is working rn", starting, start)

user_score = 0
computer_score = 0
counter = 0


def start_3():
    global user_score, computer_score

    while (user_score < 3) and (computer_score < 3):
        game_list = ['rock', 'paper', 'scissors']
        comp_choice = random.choice(game_list)

        user_input = None

        while user_input not in game_list:
            user_input = input("Pick one from the list: Rock, Paper, Scissors \n " ).lower()
        if user_input == comp_choice:
            print ("User Choice: " + str(user_input))
            print("Computer Choice:" + str(comp_choice))
            print("Its a Tie!")
        else: 
            user_input != comp_choice
            if user_input == "rock":
                print("User choice:" + str(user_input)) 
                print("Computer Choice: ", comp_choice)
                if comp_choice == "paper":
                    computer_score +=1
                    print("computer won this throw", computer_score)
                    print("User score: ", user_score)
                if comp_choice == "scissors":
                    user_score = user_score +1
                    print("user won this throw:", user_score)
                    print("computer score: ", computer_score)
            if user_input == 'paper':
                print("User choice:" + str(user_input)) 
                print("Computer Choice: ", comp_choice)
                if comp_choice == "rock":
                    user_score = user_score+1 
                    print("User Won this throw: " + str(user_score))
                    print("Computer score:", computer_score)
                if comp_choice == "scissors":
                    computer_score = computer_score +1
                    print("computer won this throw:", computer_score)
                    print("user score:" + str(user_score))
            if user_input == 'scissors':
                print("User choice:" + str(user_input)) 
                print("Computer Choice: ", comp_choice)
                if comp_choice == "paper":
                    user_score = user_score+1 
                    print("User Won this throw: " + str(user_score))
                    print("Computer score:", computer_score)
                if comp_choice == "rock":
                    computer_score = computer_score+1
                    print("computer won this throw:", computer_score)
                    print("user score:" + str(user_score))           
                          
    exit
    print("User Score:" , user_score)
    print("Computer Score:" , computer_score)
    if user_score > computer_score:
        print("User Won!")
    else:
        print("Computer Won")





def start_5():
    global user_score, computer_score

    while (user_score < 5) and (computer_score < 5):
        game_list = ['rock', 'paper', 'scissors']
        comp_choice = random.choice(game_list)

        user_input = None

        while user_input not in game_list:
            user_input = input("Pick one from the list: Rock, Paper, Scissors \n " ).lower()
        if user_input == comp_choice:
            print ("User Choice: " + str(user_input))
            print("Computer Choice:" + str(comp_choice))
            print("Its a Tie!")
        else: 
            user_input != comp_choice
            if user_input == "rock":
                print("User choice:" + str(user_input)) 
                print("Computer Choice: ", comp_choice)
                if comp_choice == "paper":
                    computer_score +=1
                    print("computer won this throw", computer_score)
                    print("User score: ", user_score)
                if comp_choice == "scissors":
                    user_score = user_score +1
                    print("user won this throw:", user_score)
                    print("computer score: ", computer_score)
            if user_input == 'paper':
                print("User choice:" + str(user_input)) 
                print("Computer Choice: ", comp_choice)
                if comp_choice == "rock":
                    user_score = user_score+1 
                    print("User Won this throw: " + str(user_score))
                    print("Computer score:", computer_score)
                if comp_choice == "scissors":
                    computer_score = computer_score +1
                    print("computer won this throw:", computer_score)
                    print("user score:" + str(user_score))
            if user_input == 'scissors':
                print("User choice:" + str(user_input)) 
                print("Computer Choice: ", comp_choice)
                if comp_choice == "paper":
                    user_score = user_score+1 
                    print("User Won this throw: " + str(user_score))
                    print("Computer score:", computer_score)
                if comp_choice == "rock":
                    computer_score = computer_score+1
                    print("computer won this throw:", computer_score)
                    print("user score:" + str(user_score))           
                          
    exit
    print("User Score:" , user_score)
    print("Computer Score:" , computer_score)
    if user_score > computer_score:
        print("User Won!")
    else:
        print("Computer Won")




def best_of_3():
    global user_score, computer_score, counter

    while counter <2:
        game_list = ['rock', 'paper', 'scissors']
        comp_choice = random.choice(game_list)

        user_input = None

        while user_input not in game_list:
            user_input = input("Pick one from the list: Rock, Paper, Scissors \n " ).lower()
        if user_input == comp_choice:
            print ("User Choice: " + str(user_input))
            print("Computer Choice:" + str(comp_choice))
            print("Its a Tie!")
        else: 
            user_input != comp_choice
            if user_input == "rock":
                print("User choice:" + str(user_input)) 
                print("Computer Choice: ", comp_choice)
                if comp_choice == "paper":
                    counter +=1
                    computer_score +=1
                    print("computer won this throw", computer_score)
                    print("User score: ", user_score)
                    print(counter)
                if comp_choice == "scissors":
                    counter +=1
                    user_score = user_score +1
                    print("user won this throw:", user_score)
                    print("computer score: ", computer_score)
                    print(counter)
            if user_input == 'paper':
                print("User choice:" + str(user_input)) 
                print("Computer Choice: ", comp_choice)
                if comp_choice == "rock":
                    counter +=1
                    user_score = user_score+1 
                    print("User Won this throw: " + str(user_score))
                    print("Computer score:", computer_score)
                    print(counter)
                if comp_choice == "scissors":
                    counter +=1
                    computer_score = computer_score +1
                    print("computer won this throw:", computer_score)
                    print("user score:" + str(user_score))
                    print(counter)
            if user_input == 'scissors':
                print("User choice:" + str(user_input)) 
                print("Computer Choice: ", comp_choice)
                if comp_choice == "paper":
                    user_score = user_score+1
                    counter +=1 
                    print("User Won this throw: " + str(user_score))
                    print("Computer score:", computer_score)
                    print(counter)
                if comp_choice == "rock":
                    computer_score = computer_score+1
                    counter +=1
                    print("computer won this throw:", computer_score)
                    print("user score:" + str(user_score))
                    print(counter)       
                          
    exit
    print("User Score:" , user_score)
    print("Computer Score:" , computer_score)
    if user_score > computer_score:
        print("User Won!")
    else:
        print("Computer Won")

    
    


def best_of_5():
    global user_score, computer_score, counter

    while counter <5 and ( user_score < 3 and computer_score < 3):
        game_list = ['rock', 'paper', 'scissors']
        comp_choice = random.choice(game_list)

        user_input = None

        while user_input not in game_list:
            user_input = input("Pick one from the list: Rock, Paper, Scissors \n " ).lower()
        if user_input == comp_choice:
            print ("User Choice: " + str(user_input))
            print("Computer Choice:" + str(comp_choice))
            print("Its a Tie!")
        else: 
            user_input != comp_choice
            if user_input == "rock":
                print("User choice:" + str(user_input)) 
                print("Computer Choice: ", comp_choice)
                if comp_choice == "paper":
                    counter +=1
                    computer_score +=1
                    print("computer won this throw: ", computer_score)
                    print("User score: ", user_score)
                    #print(counter)
                if comp_choice == "scissors":
                    counter +=1
                    user_score = user_score +1
                    print("user won this throw:", user_score)
                    print("computer score: ", computer_score)
                    #print(counter)
            if user_input == 'paper':
                print("User choice:" + str(user_input)) 
                print("Computer Choice: ", comp_choice)
                if comp_choice == "rock":
                    counter +=1
                    user_score = user_score+1 
                    print("User Won this throw: " + str(user_score))
                    print("Computer score: ", computer_score)
                    #print(counter)
                if comp_choice == "scissors":
                    counter +=1
                    computer_score = computer_score +1
                    print("computer won this throw: ", computer_score)
                    print("user score: " + str(user_score))
                    #print(counter)
            if user_input == 'scissors':
                print("User choice: " + str(user_input)) 
                print("Computer Choice: ", comp_choice)
                if comp_choice == "paper":
                    user_score = user_score+1
                    counter +=1 
                    print("User Won this throw: " + str(user_score))
                    print("Computer score: ", computer_score)
                    #print(counter)
                if comp_choice == "rock":
                    computer_score = computer_score+1
                    counter +=1
                    print("computer won this throw: ", computer_score)
                    print("user score: " + str(user_score))
                    #print(counter)       
                          
    exit
    print("User Score:" , user_score)
    print("Computer Score:" , computer_score)
    if user_score > computer_score:
        print("User Won!")
    else:
        print("Computer Won")









if starting == 'a':
    start_3()

if starting == 'b':
    start_5()

if starting == 'c':
    best_of_3()

if starting == 'd':
    best_of_5()
#while starting == 'a' and start == 3:
