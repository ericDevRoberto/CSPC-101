import random

wanna_play = "yes"

while wanna_play == "yes":

    play_count = 0

    number = random.randint(1,100)

    answer = 0    

    while number != answer:        

        print(f"What is the magic number? {number}")
        
        answer = int(input("What is your guess? "))

        if number > answer:

            play_count = play_count +1
            print("Higher")
        
        elif number < answer:

            play_count = play_count +1
            print("Lower")
        
        else:

            play_count = play_count +1
            print("You guessed it!")
    
    print(f"You played {play_count} times")

    wanna_play = input("Do You want to play again? ")


print("Thanks for Play!")

