# Programmer: Mr. Lange
# Date Merged: 2.6.2023
# Merged Welcome Screen and Gasoline Branches - Stable


"""
Our Welcome Screen will start our Program letting
drivers know that the InfoTech Center 4.0 OS is loading
"""

#Import Libraries Here
import time
import sys  # I imported the system library for further use in code.
import random
from time import sleep


timeToSleep = 2

print("\n\n\033[1;33;40mWelcome - InfotechCenter 4.0\n")
time.sleep(timeToSleep)


x = 0
a = 0

while x != 20:
    x += 1
    b = ("\033[1;33;40mInfotech Center 4.0 OS is loading" + "." * a)
    a = a + 1
    sys.stdout.write('\r'+b) # \r prints a carriage return first, so `b` is printed on top of the previous line.
    time.sleep(0.5)
    if a == 4:
        a = 0
    if x == 20:
        print('\n\n\033[1;32;40mMission Accomplished - Retina Scanned - Access Granted\n')







# Programmer: Mr.Lange
# Date: 1.30.2023
# Program: Infotech Center 4.0 - Gasoline

"""
We will create a Function that will tell us our Fuel Gauge level
   - Create a List with Gas Levels
   - Randomize and choose from the list to determine our gas level

Create a Function to determine our closest Gas Station
   - Create a list of gas stations
   - Randomnly choose a gas station from the list

Create a Function to determine our gas level and closest gas station
   - Print Gas level
   - Print Closest Gas Station
"""




# Gas Level Function
def gasLevelGauge():
    gasLevelList = ["Empty","Low","Quarter Tank","Half Tank","Three Quarter Tank","Full Tank"]
    currentGasLevel = random.choice(gasLevelList)
    return currentGasLevel

# Variable calling gasLevelGuage function to store its value
gasLevelIndicator = gasLevelGauge()

# List of Gas Stations Function
def listOfGasStations():
   gasStations = ["Shell","Costco","Buc-ee's","Speedway","7-11","Circle-K","Meijer","Marathon"]
   gasStationNearby = random.choice(gasStations)
   return gasStationNearby

# Determine Gas Level & Closest gas station
def gasLevelAlert():
    milesToGasStationLow = round(random.uniform(1, 25), 2)
    milesToGasStationQuartTank = round(random.uniform(26, 50), 2)
    if gasLevelIndicator == "Empty":
        print("***WARNING YOU ARE ON EMPTY***")
        sleep(1)
        print("Calling Emergency Contact")
    elif gasLevelIndicator == "Low":
        print("****Warning****")
        sleep(1)
        print("Your gas tank is extremely low, checking Google Maps for the closest gas station.")
        sleep(1)
        print("The closest gas station is",listOfGasStations(),"which is",milesToGasStationLow,"miles away.")
    elif gasLevelIndicator == "QuarterTank":
        print("***Warning***")
        sleep(1)
        print("Your gas tank is at a Quarter Tank and the closest gas station is",listOfGasStations(),"which is",milesToGasStationQuartTank,"miles away.")
    elif gasLevelIndicator == "Half Tank":
        print("Your gas tank is a half of a tank full which is plenty of gas to make it to your destinations today.")
    elif gasLevelIndicator == "Three Quarter Tank":
        print("Your gas tank is at three quarters of a tank which is "
              "plenty of gas to make it to your destinations today.")
    else:
        print("Your gas tank is full - Yeah! - Congratulations - Vroom Vroom.")






# Programmer: Mr. Lange
# Date: 2.8.2023
# Program: Weather System Updates


#Create weather conditon in a list and choose it randomly
def weather():
    weatherForcast = ["Snowing", "Blizzard", "Rain", "Foggy", "Windy", "Icy", "Sunshine"]
    weatherCondition = random.choice(weatherForcast)
    return weatherCondition

# Variable to call weather() once in our VRS()
weatherAlert = weather()


# VRS() to respond to the weather condition
def vehicleResponseSystem():
    if weatherAlert == "Snowing":
        print("\nNWS has changed your Alarm by 15 minutes because of the weather forcast of",weatherAlert)
        print("VRS has been engaged only allowing your vehicle to go 45 MPH")
    elif weatherAlert == "Blizzard":
        print("\nNWS has changed your Alarm by 30 minutes because of the weather forcast of",weatherAlert)
        print("VRS has been engaged only allowing your vehicle to go 35 MPH")
    elif weatherAlert == "Rain":
        print("\nNWS is calling for",weatherAlert,",please drive extra carefully.")
    elif weatherAlert == "Foggy":
        print("\nNWS is calling for",weatherAlert,"conditions, please drive extra careful.")
    elif weatherAlert == "Windy":
        print("\nNWS is calling for",weatherAlert,"conditions, please drive extra careful.")
    elif weatherAlert == "Icy":
        print("\nNWS has changed your Alarm by 60 minutes because of the weather forcast of",weatherAlert)
        print("VRS has been engaged only allowing your vehicle to go 25 MPH")
    else:
        print("\nNWS is calling for",weatherAlert,"drive safely and have a wonderful day!")
        




#Call Function Here

vehicleResponseSystem()
gasLevelAlert()