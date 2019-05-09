import random

num=random.randint(1,20)
number_of_attempt=0

while number_of_attempt < 3 :
    print("Guess the number between 1 & 20")
    guess=input()
    guess=int(guess)
    
    number_of_attempt=number_of_attempt+1
    
    if guess>num :
        print("Bhai thoda aaram se.. Itna bhi bada nahi hai.")
        print("You still have "+str(3 - number_of_attempt)+" attempts left.")
        
    elif guess<num :
        print("Itna bhi chota nahi hai...  ")
        print("You still have "+ str(3 - number_of_attempt) + " attempts left.")
        
    elif guess==num :
        print("Bhai launda hoshiyar hai")
        print("You guessed the right number in " +str(number_of_attempt)+ " attempts")
        break

print("The number was " + str(num) )
