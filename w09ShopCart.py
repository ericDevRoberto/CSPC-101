print("Welcome to the Shopping Cart Program!")

option = 0

cart_itens = []

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

        cart_itens.append(item_cart)

        print(f"'{item_cart}' has been added to the cart.")

    elif option == 2:

        print("The contents of the shopping cart are:")

        for item in cart_itens:
            print(f"{item}")


print("\nThank you. Goodbye.")