#Inputs
childs_meal_price = float(input("What is the price of a child's meal? "))
adults_meal_price = float(input("What is the price of an adult's meal? "))
how_many_children = int(input("How many children are there? "))
how_many_adults = int(input("How many adults are there? "))
tax_rate = float(input("What is the sales tax rate? "))

#Subtotal computed and display
subtotal = round(childs_meal_price * how_many_children + adults_meal_price * how_many_adults, 2)
print(f"\nSubtotal: ${format(subtotal, '.2f')}")

#Sales computed and display
sales_tax = round(subtotal * (tax_rate / 100), 2)
print(f"Sales tax: ${format(sales_tax, '.2f')}")

#Total computed and display
total = round(subtotal + sales_tax, 2)
print(f"Total: ${format(total, '.2f')}\n")

##Payment security logic
payment_denied = True

#Computing input
payment_amount = float(input("What is the payment amount? "))
change = round(payment_amount - total, 2)

#Verifing if is sufficient
while payment_denied:
    if payment_amount < total:
        print("\nPayment amount insufficient!")
        payment_amount = float(input("\nWhat is the new payment amount? "))
        change = round(payment_amount - total, 2)
    else:
        payment_denied = False

#Payment display
print(f"Change: ${format(change, '.2f')}")