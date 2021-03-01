print("Enter a list of numbers, type 0 when finished.")

numbers = []

number = 1

count = 0

numbers_sum = 0

largest_number = 0

smallest_positive_number = 99999999

while number != 0:

    number = int(input("Enter number: "))

    numbers_sum += number

    if number > largest_number:
        
        largest_number = number

    elif number < smallest_positive_number and number > 0:

        smallest_positive_number = number

    if number != 0:

        numbers.append(number)

        count += 1 

print(f"The sum is: {numbers_sum}")

print(f"The average is: {numbers_sum / count}")

print(f"The largest number is: {largest_number}")

print(f"The smallest positive number is: {smallest_positive_number}")

print("The sorted list is:")

numbers.sort()

for numb in numbers:

    print(f"{numb}")