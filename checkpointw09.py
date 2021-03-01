friends = []

friend = ""

while friend != "end":

    friend = input("\nType the name of a friend: ")

    if friend != "end":

        friends.append(friend)



print("\nYour friends are:")
for friend in friends:
    print(f"{friend}")