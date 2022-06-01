# Notes. 
    # Wind Chill (ºF) = 35.74 + 0.6215T - 35.75(V0.16) + 0.4275T(V0.16)
    # T is the temperature in degrees Fahrenheit
    # V is the wind speed in miles per hour
    # V^0.16 means V to the power of 0.16, which can be found in Python using the ** operator.

# Imports.
import math

# Variables.
    # wind_speed??
windchill = 0

# Functions.
def windchill(temp,wind_speed):
    # for i in range(5, 60, 5):
        windchill = 35.74 + 0.6215 * temp - 35.75 * wind_speed ** 0.16 + 0.4275 * temp * wind_speed ** 0.16

def degree(celcius):
    celcius = windchill * 9 / 5 + 32

# Inputs.
temp = float(input("What is the temperature? "))
degree_system = input("Farenheit or Celcius (F/C)? ")
if degree_system.lower() == "c":
    celcius = degree_system


# Using functions.
windchill = windchill(temp,wind_speed)

# Display.

print(f"At a temperature of {temp}, with a wind speed of [windspeed], the windchill is: {windchill:.2f}")
