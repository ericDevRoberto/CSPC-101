import math

def compute_area_square(side):
    square_area = side ** 2
    return square_area

def compute_area_rectangle(length, width):
    area = length * width
    return area

def compute_area_circle(radius):
    area = math.pi * radius ** 2
    return area

def compute_area (form, val_one, val_two = 0):

    if form == "square":
        return compute_area_square(val_one)
    
    elif form == "rectangle":
        return compute_area_rectangle(val_one, val_two)

    elif form == "circle":
        return compute_area_circle(val_one)

    else:
        print(f"{form} isn't a valid parameter")

option = ""

while option != "quit":

    option = input("What shape do you have? ")
    
    if option == "square":
        # Square calculation
        square_side = float(input("What is the length of a side of the square? "))
        square_area = compute_area(option, square_side)
        print(f"The area of the square is: {square_area}")

    elif option == "rectangle":
        #Retangule Calculation
        retangle_length = float(input("What is the length of the retangle? "))
        retangle_width = float(input("What is the width of the retangle? "))
        retangle_area = compute_area(option, retangle_length, retangle_width)
        print(f"The area of the rectangle is: {retangle_area}")

    elif option == "circle":
    #Circle calculation
        circle_radius = float(input("What is the radius of the circle? "))
        circle_area = compute_area(option, circle_radius)
        print(f"The area of the circle is: {circle_area:.2f}")

print("Quit program")

