# Programmer: Mr.Lange
# Date: 1.20.2023
# Program: Infotech Center Upgrades

"""
Our Welcome Screen will start our Program letting
drivers know that the InfoTech Center 4.0 OS is loading
"""

#Import Libraries Here
import time
import sys  # I imported the system library for further use in code.

timeToSleep = 2

print("\n\nWelcome - InfotechCenter 4.0")
time.sleep(timeToSleep)

#print("\nInfotech Center 4.0 OS is loading")
x = 0
a = 0

while x != 20:
    x += 1
    b = ("\033[1;33;40m Infotech Center 4.0 OS is loadin" + "." * a)
    a = a + 1
    sys.stdout.write('\r'+b) # \r prints a carriage return first, so `b` is printed on top of the previous line.
    time.sleep(0.5)
    if a == 4:
        a = 0
    if x == 20:
        print('\033[1;32;40m Done!')