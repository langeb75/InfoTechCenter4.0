# Programmer: Mr.Lange
# Date: 2.8.2023
# Program: Weather System Updates

#Import Libraries here
import random

#Create weather conditon in a list and choose it randomly
def weather():
    weatherForcast = ["Snowing", "Blizzard", "Raining", "Foggy", "Windy", "Icy", "Sunshine"]
    weatherCondition = random.choice(weatherForcast)
    return weatherCondition

# Variable to call weather() once in our VRS()
weatherAlert = weather()

print(weatherAlert)

# VRS() to respond to the weather condition
def vehicleResponseSystem():
    print("HOwdy")