loan = int(input("How large is the loan? "))
credit = int(input("How good is your credit history? "))
income = int(input("How high is your income? "))
payment = int(input("How large is your down payment? "))

decision = "no"

if loan >= 5:
    if credit >= 7 and income >= 7:
        decision = "yes"
    elif (credit >= 7 and payment >= 5) or (income >= 7 and payment >= 5):
        decision = "yes"
    else:
        decision= "no"
else:
    if credit < 4:
        decision= "no"
    else:
        if income >= 7 or payment >= 7:
            decision= "yes"
        elif income >= 4 and payment >= 4:
            decision = "yes"
        else:
            decision = "no"

print(f"\nLoan size: {loan}, Credit: {credit}, Income: {income}, Down Payment: {payment}, Decision: {decision}")