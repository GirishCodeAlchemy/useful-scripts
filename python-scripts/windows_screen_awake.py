#! /usr/bin/python3

# Import required modules
import pyautogui
import time

# Disable FAILSAFE feature (so you can stop the program manually)
pyautogui.FAILSAFE = False

# Run this code indefinitely
while True:
    # Wait for 15 seconds (customize as needed)
    time.sleep(120)

    # Move the mouse pointer to the upper left corner (0,0)
    for i in range(0, 100):
        pyautogui.moveTo(0, i * 5)

    # Simulate pressing the Shift key (customize as needed)
    for i in range(0, 3):
        pyautogui.press('shift')
