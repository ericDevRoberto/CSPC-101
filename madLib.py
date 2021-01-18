print("Please enter the following:\n")

#Inputs
adjective = input("adjective: ")
animal = input("animal: ")
verbOne = input("verb: ")
exclamation = input("exclamation: ")
verbTwo = input("verb: ")
verbThree = input("verb: ")

#Logic a/an in the last phrase
article = "A"
vowel = ['a', 'e', 'i', 'o', 'u']

for letter in animal:
    if letter in vowel:
        article = "An"

#Printed message
print("\nYour story is:\n")
print(f"The other day, I was really in trouble. It all started when I saw a very")
print(f'{adjective} {animal} {verbOne} down the hallway. "{exclamation.capitalize()}!" I yelled. But all')
print(f"I could think to do was to {verbTwo} over and over. Miraculously,")
print(f"that caused it to stop, but not before it tried to {verbThree}")
print("right in front of my family.\n")

#Extra Message
print(f"PS: {article} {animal} was used in that history.")