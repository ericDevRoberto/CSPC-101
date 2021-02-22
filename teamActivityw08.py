
print("How many columns and rows do you want in your multiplication table? 5")

for number in range(1,6):

    for digit in range(1,6):
        print(f"{digit * number:3}", end=" ")
    
    print()

print()

print("How many columns and rows do you want in your multiplication table? 12")

for number in range(1,13):

    for digit in range(1,13):
        print(f"{digit * number:3}", end=" ")
    
    print()
    
print()

print("How many columns and rows do you want in your multiplication table? 32")

for number in range(1,33):

    for digit in range(1,33):
        print(f"{digit * number:5}", end=" ")
    
    print()