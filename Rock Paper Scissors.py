from random import randint

options = ["Rock","Paper","Scissors"]

Play = True

while Play == True :
    
    opponent = options[randint(0,2)]
    user = input("Rock,Paper,Scissors? ")
    
    if user == opponent :
        print("Oh!! Its a draw...The computer also choose " +str(opponent))
        
    elif user == "Rock" :
        if opponent== "Paper" :
            print("What a bummer!!  The computer chose "+ str(opponent) + ". You got wrapped like a burito.")
        else :
            print("Yeah!!  The computer choose" + str(opponent) + ". You busted it like a nail.")
            
    elif user == "Paper" :
        if opponent == "Scissors" :
            print("What a bummer!!  The computer choose " + str(opponent) + ". You got totally ripped.")
        else :
            print("Yeah!!  The computer choose " + str(opponent) + ". You wrapped it like a burito.")
            
    elif user=="Scissors" :
        if opponent == "Rock" :
            print("What a bummer!!  The computer choose " + str(opponent) + ". You got busted like a nail.")
        else :
            print("Yeah!!  The computer choose " + str(opponent) + ". You ripped it totally.")
            
    else:
        print("You know that this game has only 3 options...right?")
        
    again = input("Do you want to play the game again? Y or N ")
    if again == "N" :
        Play = "False"
    
    opponent == options[randint(0,2)]
    
print("Thank You for playing the game.")
