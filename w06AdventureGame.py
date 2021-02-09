first_lvl = True
second_lvl = True

def tip ():
    print("\nYou got a tip, try again!")

def over ():
    print("\nGame over, try again.")

print("\nWelcome to the Mystery Adventure!\n")

print("\nIn this game have many ends, some ends give you tips, then uses them to arrest the criminal!")
print("\nLet's Begin!")


print("You are a Royal Knight looking for a criminal named Ruprest, and you arrived in the city of Esgal and want information. You see two places, the Guild and a Tavern.\n")

# First layer
while first_lvl:

    first_choise = input("You want to go to the GUILD or the TAVERN? ").lower()

    if first_choise == "guild" or first_choise == "tavern" or first_choise == "store":
        
        first_lvl = False
    else:
        print("\nInvalid option, try again")

## GUILD Second Layer
if first_choise == "guild" :    

    print("\nYou entered the Guild and glimpsed the Great Hall of Heroes with many people there, and two people draw your attention, a strong barbarian and a curious Wizard.")

    while second_lvl:

        second_choice = input("\nDo You want to talk with the BARBARIAN or the WIZARD? ").lower()

        if second_choice == "barbarian" or second_choice == "wizard" or second_choice == "receptionist":
            
            second_lvl = False
        else:
            print("\nInvalid option, try again")
    
    ### BARBARIAN Third Layer
    if second_choice == "barbarian":

        print("\nDo You go to the barbarian, and He looks at you without interest.")

        third_choice = input("\nYou want to ASK information or PAY him? ").lower()

        if third_choice == "ask":
            print("\nYou try ask something but the barbarian shouted: I'm not a receptionist!!")
            over()

        elif third_choice == "pay":
            print("\nyou pay him and ask about Ruprest and the barbarian said: In the TAVERN, you will find something about that guy.")
            tip()

        else:
            print("\nThe barbarian didn't like you and hit you. You have fainted.")
            over()
    
    ### WIZARD Third Layer
    elif second_choice == "wizard":

        print("\nYou approach the Wizard, and he is distracted with a lightning ball, and you want some answers.")

        third_choice = input("\nDo You want to QUESTION him or PAY him for the information? ").lower()

        if third_choice == "question":
            print("\nThe Wizard says: Please, don't disturb me.")
            over()
        
        elif third_choice == "pay":
            print("\nThe Wizard stares you in angry: You offer money to my attention?! That is an offense! He transforms you into a rabbit, and now you are his pet.")
            over()

        else:
            print("\nYou do nothing, and the Wizard doesn't give attention.")
            over()
    
    ### RECEPTIONIST Third Layer
    elif second_choice == "receptionist":
        
        print("\nYou cross the Great Hall of Heroes and go to the receptionist. She gives you a big smile and says: -Can I help you?")

        third_choice = input("\nDo You want to ASK her or JOIN to guild? ").lower()

        if third_choice == "ask":
            print("\nThe receptionist says: I heard about that criminal. I suggest you go to the STORE at the city entrance.")
            tip()

        elif third_choice == "join":
            print("\nYou abandon the kingdom and become an adventurer living adventures for yourself.")
            over()

        else:
            print("\nYou fall in love with the beautiful receptionist and flee with her to another country.")
            over()

## TAVERN Second Layer
elif first_choise == "tavern":

    print("\nYou entered the TAVERN, which has some people there, and you look at table travelers and the tavern manager.")

    while second_lvl:

        second_choice = input("\nDo You want to talk to the TRAVELERS or the MANAGER? ").lower()

        if second_choice == "travelers" or second_choice == "manager":
            second_lvl = False

        else:
            print("\nInvalid option, try again")
        

    ### TRAVELERS Third Layer
    if second_choice == "travelers":

        print("\nYou approach the travelers, and everyone keeps silent")

        third_choice = input("\nDo You ASK about the criminal or DRINK with them? ").lower()

        if third_choice == "ask":
            print("\nThey hear you do questions but don't answer you, and you go back without information.")
            over()

        elif third_choice == "drink":
            print("\nYou take a glass and talk a lot with them, and they speak that the MANAGER knows something about this city.")
            tip()

        else:
            print("\nYou keep silent too, and they ignore you.")
            over()
    
    ### MANAGER Third Layer
    elif second_choice == "manager":
        
        print("\nWhen you approach him, He looks at you and stares at you, waiting for what you want.")

        third_choice = input("\nDo You want to give him gold for PAY by information or FACE him? ").lower()

        if third_choice == "pay":
            print("\n The manager says: With your money, I can give you a drink or a room, just it.")
            over()

        elif third_choice == "face":
            print("\nYour gaze admired him, and you did questions and indicated to talk with the RECEPTIONIST in the GUILD.")
            tip()

        else:
            print("\nHe scares you, and you come back to the kingdom without tips.")
            over()

## STORE Second Layer
elif first_choise == "store":

    print("\nIn the suburb, you found a store, then you enter there, and you look at that, and the counter doesn't have any person the place is empty.")

    third_choice = input("\nDo You want to go to the BACK of the store or CALL someone? ").lower()

    if third_choice == "back":
        print("\nYou go to the back of the store and find Ruprest! Then you arrest him and accomplish your mission.")
        print("\n You solved the mystery and win the game!")
    
    elif third_choice == "call":
        print("\nYou call some merchant, but you hear step sounds in the back of the store, and you go away.")
        over()
    
    else:
        print("\nYou keep in silence and go away.")
    