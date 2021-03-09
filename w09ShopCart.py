print("Welcome to the Shopping Cart Program!")

option = 0

cart_itens = []

cart_prices = []

quantities = []

total = 0

while option != 5:    

    print("\nPlease select one of the following:")
    print("1. Add item")
    print("2. View cart")
    print("3. Remove item")
    print("4. Compute total")
    print("5. Quit")
    option = int(input("Please enter an action: "))

    if option == 1:
        item_cart = input("What item would you like to add? ")

        item_price = float(input(f"What is the price of {item_cart}? "))

        quantity = float(input(f"How many? "))

        if quantity != 0:

            cart_itens.append(item_cart)

            cart_prices.append(item_price)

            quantities.append(quantity)

            print(f"'{item_cart}' has been added to the cart.")
        else:

            print(f"'{item_cart}' hasn't been added to the cart.")

    elif option == 2:

        print("The contents of the shopping cart are:")

        for i in range(len(cart_itens)):
            print(f"{cart_itens[i]} - ${cart_prices[i]:.2f} x {quantities[i]}")
    
    elif option == 3:

        remove_item = int(input("Which item would you like to remove? "))

        cart_itens.pop(remove_item - 1)

        cart_prices.pop(remove_item - 1)

        quantities.pop(remove_item - 1)

        print("Item removed.")

    elif option == 4:

        for n in range(len(cart_prices)):

            price = cart_prices[n] * quantities[n]

            total += price

        print(f"The total price of the items in the shopping cart is ${total:.2f}")        
        

print("\nThank you. Goodbye.")