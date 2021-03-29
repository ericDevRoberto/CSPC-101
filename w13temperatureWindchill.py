#celcius_to_fahrenheit() isn't used because now the result computes and shows answer in Celcius
def celcius_to_fahrenheit(value):

    return (value * 1.8) + 32

def windchill_fahrenheit(temperature, wind_speed):

    return 35.74 + 0.6215 * temperature - 35.75 * (wind_speed **0.16) + 0.4275 * temperature * (wind_speed ** 0.16)

def windchill_celcius(temperature, wind_speed):

    return 13.12 + 0.6215 * temperature - 11.37* (wind_speed ** 0.16) + 0.3965 * temperature * (wind_speed ** 0.16)

def windchill_calc(temperature, wind_speed, unit): 

    if unit == "f":

        windchill = windchill_fahrenheit(temperature, wind_speed)

        print(f"At temperature {temperature}F, and wind speed {wind_speed} mph, the windchill is: {windchill:.2f}F")
    
    elif unit == "c":

        windchill = windchill_celcius(temperature, wind_speed)

        print(f"At temperature {temperature}ºC, and wind speed {wind_speed} mph, the windchill is: {windchill:.2f}ºC")


#Program begin here
temperature = int(input("What is the temperature? "))

unit_medition = input("Fahrenheit or Celsius (F/C)? ").lower()

if unit_medition == "c" or unit_medition == "f":

    for number in range(1,61):

        if number % 5 == 0:
            windchill_calc(temperature = temperature, wind_speed = number, unit = unit_medition)

else:
     print("You can only choose 'F' for Fahrenheit or 'C' for Celsius")