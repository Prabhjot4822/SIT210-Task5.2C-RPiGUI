# Import necessary libraries
from tkinter import *
import tkinter.font
from gpiozero import LED
import RPi.GPIO

# Set the GPIO mode to BCM (Broadcom SOC channel numbering)
RPi.GPIO.setmode(RPi.GPIO.BCM)

# Define hardware connections for Red, Green, and Blue LEDs
ledR = LED(14)
ledG = LED(15)
ledB = LED(18)

# Create a Tkinter window for the GUI
win = Tk()
win.title("LED SWITCHER")
myFont = tkinter.font.Font(family='Helvetica', size=14, weight='bold')

# Define event functions for toggling LEDs
def ledRswitch():
    if ledR.is_lit:
        ledR.off()
        ledRbutton["text"] = "RED ON"
    else:
        ledR.on()
        ledRbutton["text"] = "RED OFF"

def ledGswitch():
    if ledG.is_lit:
        ledG.off()
        ledGbutton["text"] = "GREEN ON"
    else:
        ledG.on()
        ledGbutton["text"] = "GREEN OFF"

def ledBswitch():
    if ledB.is_lit:
        ledB.off()
        ledBbutton["text"] = "BLUE ON"
    else:
        ledB.on()
        ledBbutton["text"] = "BLUE OFF"

# Function to clean up GPIO and close the window
def close():
   RPi.GPIO.cleanup()
   win.destroy()

# Create GUI widgets (buttons) for controlling LEDs
ledRbutton = Button(win, text='RED ON', font=myFont, command=ledRswitch, bg="grey", height=2, width=30)
ledRbutton.grid(row=0, column=1)

ledGbutton = Button(win, text='GREEN ON', font=myFont, command=ledGswitch, bg="grey", height=2, width=30)
ledGbutton.grid(row=1, column=1)

ledBbutton = Button(win, text='BLUE ON', font=myFont, command=ledBswitch, bg="grey", height=2, width=30)
ledBbutton.grid(row=2, column=1)

exitbutton = Button(win, text='EXIT', font=myFont, command=close, bg="red", height=1, width=8)
exitbutton.grid(row=4, column=1)

# Handle window close event to perform cleanup
win.protocol("WM_DELETE_WINDOW", close)

# Start the Tkinter main loop
win.mainloop()