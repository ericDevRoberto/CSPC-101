import random

wanna_play = "yes"

play_count = 0

while wanna_play == "yes":

    number = random.randint(1,100)

    answer = 0    

    while number != answer:
        

        print(f"What is the magic number? {number}")
        
        answer = int(input("What is your guess? "))

        if number > answer:

            print("Higher")
        
        elif number < answer:

            print("Lower")
        
        else:

            play_count = play_count +1

            print("You guessed it!")
    
    print(f"You played {play_count} times")

    wanna_play = input("Do You want to play again? ")


print("Thanks for Play!")

