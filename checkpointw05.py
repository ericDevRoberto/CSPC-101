firstNumber = int(input("What is the first number? "))
secondNumber = int(input("What is the second number? "))


if firstNumber > secondNumber:
    print("The first number is greater")

else:
    print("The first number is not greater")

if firstNumber == secondNumber:
    print("The numbers are equal")
else:
    print("The numbers are not equal")

if firstNumber < secondNumber:
    print("The second number is greater")

else:
    print("The second number is not greater")

animal = input("\nWhat is your favorite animal? ")

if animal.lower() == "bear":
    print("That's my favorite animal too!")
else:
    print("That one is not my favorite.")