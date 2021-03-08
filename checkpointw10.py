itens = []

item = ""

print("Please enter the items of the shopping list (type: quit to finish):")

while item != "quit":

    item = input("Item: ")

    if item != "quit":

        itens.append(item)


print("\nThe shopping list is:")

for i in itens:   

    print(i)

print("\nThe shopping list with indexes is:")

for i in range(len(itens)):    
    item = itens[i]

    print(f"{i}. {item}")

number_change = int(input("Which item would you like to change? "))

new_item = input("What is the new item? ")

itens[number_change] = new_item

print("\nThe shopping list with indexes is:")

for i in range(len(itens)):    
    item = itens[i]

    print(f"{i}. {item}")

