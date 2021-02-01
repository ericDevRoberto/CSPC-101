score = int(input("What is your score? "))

letter = "A"

if score >= 90:
    letter = "A"

elif score >= 80:
    letter = "B"

elif score >= 70:
    letter = "C"

elif score >= 60:
    letter = "D"

else:
    letter = "F"

def split(word): 
    return [char for char in word]

result = split(str(score))

if int(result[0]) == 9 or int(result[0]) <= 5:
    print()
else:
    if int(result[1]) >= 7:
        letter = letter + "+"
    elif int(result[1]) <= 3:
        letter = letter +  "-"

print(f"Your grade is: {letter}")

if score >= 70:
    print("Congratulations! You passed the class!")
else:
    print("Stay focused and you'll get it next time!")
