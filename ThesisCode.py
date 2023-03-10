# Create A program for Automated Feeding Machine

# 1st Create A menu. In The Menu that has TIME AND DATE TIME OF FEEDING, KILOGRAMS/GRAMS, and START OPERATIONS
# 2nd Create A Configuration For TIME AND DATE TIME OF FEEDING and KILOGRAMS/GRAMS
# Create A function of START OPERATION Where TIME OF FEEDING and KILOGRAMS/GRAMS Configuration WILL save
# In the Configuration for TIME OF FEEDING is We use the DS3231 RTC Module that control the Time(HRS) of the FEEDING
#
# In the Configuration of KILOGRAMS/GRAMS we used the LOADCELL.
#

from machine import Pin, SoftI2C
from lcd_api import LcdApi
from i2c_lcd import I2cLcd
from ds3231 import DS3231
from time import sleep

# Initializing The Buttons
button_up = Pin(12, Pin.IN)
button_down = Pin(14, Pin.IN)
button_select = Pin(13, Pin.IN)

# Initiate The Size and the Address of the LCD

I2C_ADDR = 0x27
totalRows = 2
totalColumns = 16

# Iniitalizing the I2C method for ESP32

i2c = SoftI2C(scl=Pin(22), sda=Pin(21), freq=10000)
# i2c = I2C(scl=Pin(5), sda=Pin(4), Freq=10000)
# Initializing the I2C method for ESP8266
lcd = I2cLcd(i2c, I2C_ADDR, totalRows, totalColumns)
# Initialization RealTime Clock Module

ds = DS3231(i2c)
# Printing The Time and Date
time = ds.get_time()
print("Year " + str(time[0]))
print("Month " + str(time[1]))
print("Day " + str(time[2]))
print("Hour " + str(time[3]))
print("Minute " + str(time[4]))
print("Second " + str(time[5]))


# Creating Array for Menu

menu = ["TIME AND DATE",
        "TIME OF FEEDING",
        "KILOGRAM/GRAMS",
        "START OPERATION"
        ]
TimeDate = menu[0]
TimeFeeding = menu[1]
KiloGrams = menu[2]
StartOps = menu[3]


options_menu = 0  # Main Menu State
select = 0  # Select Button State


# Creating Functions For RealTime Clock


def RealTime():
    date_time = ds.get_time()
    year = str(date_time[0])
    month = str(date_time[1])
    day = str(date_time[2])
    hour = str(date_time[3])
    minute = str(date_time[4])
    second = str(date_time[5])

# this Section is for displaying the Time, Date, Year, Month, and day to the LCD Screen
    lcd.clear()
    lcd.putstr("TIME: " + hour + ":" + minute + ":" + second)
    lcd.move_to(1, 0)
    sleep(10)
    lcd.clear()
    lcd.putstr("Date: " + year + "/" + month + "/" + day)
    sleep(10)


# RealTime()

# Time and Date Configuration


def Time_Date():
    DateTime = ds.get_time()
    year = 0
    month = 0
    day = 0
    hour = 0
    minute = 0
    second = 0
    if options_menu == 0:
        if button_select == True:
            print("The button was pressed")


Time_Date()


while True:
    Time_Date()
    if button_up.value() == True:
        lcd.clear()
        options_menu = max(options_menu - 1, 0)
        lcd.move_to(0, 0)
        lcd.putstr(f"{menu[options_menu]}")
    if button_down.value() == True:
        lcd.clear()
        options_menu = min(options_menu + 1, len(menu) - 1)
        lcd.move_to(0, 0)
        lcd.putstr(f"{menu[options_menu]}")
