acounts = []
balances = []
acount_name = ""
total = 0
count = 0

print("Enter the names and balances of bank accounts (type: quit when done)")

while acount_name != "quit":

    acount_name = input("What is the name of this account? ")

    if acount_name != "quit":

        balance = float(input("What is the balance? "))

        acounts.append(acount_name)
        balances.append(balance)

print("\nAccount Information:")

for i in range(len(acounts)):

    print(f"{acounts[i]} - ${balances[i]}")
    total += balances[i]
    count += 1


print(f"\nTotal ${total}")

average = total / count

print(f"Average ${average:.2f}")