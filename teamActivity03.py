import math

#Core requirements

# Square calculation
square_side = float(input("What is the length of a side of the square? "))
square_area = square_side ** 2
print(f"The area of the square is: {square_area}")

#Retangule Calculation
retangle_length = float(input("What is the length of the retangle? "))
retangle_width = float(input("What is the width of the retangle? "))
retangle_area = retangle_length * retangle_width
print(f"The area of the retangle is: {retangle_area}")

#Circle calculation
circle_radius = float(input("What is the radius of the circle? "))
circle_area = math.pi * circle_radius ** 2
print(f"The area of the circle is: {circle_area}")

#Second strech challenge

#Volume/Area Calculation
volume_area_inicial_length = float(input("Put a length in centimeters: "))
volume_area_square = volume_area_inicial_length ** 2
volume_area_cicle = math.pi * volume_area_inicial_length ** 2
volume_area_cube = volume_area_inicial_length ** 3
volume_area_sphere = (4/3) * math.pi * volume_area_inicial_length ** 3

print(f"The area of the square is: {volume_area_square}")
print(f"The area of the cicle is: {volume_area_cicle}")
print(f"The volume of the cube is: {volume_area_cube}")
print(f"The volume of the sphere is: {volume_area_sphere}")

#Third strech challenge

# Square calculation in square meters
square_side = float(input("What is the length of a side of the square? (in centimeters) "))
square_area = (square_side ** 2)
print(f"The area of the square is: {square_area} cm^2")
print(f"The area of the square is: {square_area / 10000} m^2")

#Retangule Calculation in square meters
retangle_length = float(input("What is the length of the retangle? (in centimeters) "))
retangle_width = float(input("What is the width of the retangle? (in centimeters) "))
retangle_area = retangle_length * retangle_width 
print(f"The area of the retangle is: {retangle_area} cm^2")
print(f"The area of the retangle is: {retangle_area / 10000} m^2")

#Circle calculation in square meters
circle_radius = float(input("What is the radius of the circle? (in centimeters) "))
circle_area = math.pi * circle_radius ** 2 
print(f"The area of the circle is: {circle_area} cm^2")
print(f"The area of the circle is: {circle_area / 10000} m^2")