first_rider_age = int(input("What is the age of the first rider? "))
first_rider_height = int(input("What is the height of the first rider? "))
have_second_rider = input("Is there a second rider (yes/no)? ")

if(first_rider_age < 18 and first_rider_age >= 12):
        golden_one = input("Does this rider have a golden passport (yes/no) ").lower()   

permission = False

if have_second_rider == "yes":  

    second_rider_age = int(input("What is the age of the second rider? "))
    second_rider_height = int(input("What is the height of the second rider? "))
    
    if(second_rider_age < 18 and second_rider_age >= 12):
        golden_two = input("Does this rider have a golden passport (yes/no) ").lower()   
    
    if (second_rider_height >= 62 and (second_rider_age >= 18 or golden_two == "yes")) or (first_rider_height >= 62 and (first_rider_age >= 18 or golden_one == "yes")):
        permission = True 

    elif  (second_rider_height >= 52 and second_rider_age >= 12) and (first_rider_height >= 52 and first_rider_age >= 12):
        
        if (second_rider_age >= 16 and first_rider_age >= 14) or (second_rider_age >= 14 and first_rider_age >= 16):
            permission = True

    if second_rider_height < 36:
        permission = False  

else:
   
    if golden_one == "yes":

        if first_rider_height >= 62 and first_rider_age >= 12 :
            permission = True
    
    else:
        if first_rider_height >= 62 and first_rider_age >= 18 :
            permission = True


if first_rider_height < 36:
    permission = False


if permission:
    print("Welcome to the ride. Please be safe and have fun!")
else:
    print("Sorry, you may not ride.")