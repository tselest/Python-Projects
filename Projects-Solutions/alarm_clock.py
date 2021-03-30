#Importing all the necessary libraries to form the alarm clock:
 
from tkinter import *
import datetime
import time

import platform
try:
    import winsound # for windows
except:
    import os # for linux chads 

# winsound is not available for linux

#Defining the While loop for the alarm
def alarm(set_alarm_timer):
    while True:
        time.sleep(1)
        current_time = datetime.datetime.now()
        now = current_time.strftime("%H:%M:%S")
        date = current_time.strftime("%d/%m/%Y")
        #print("The Set Date is:",date)  >>> These two lines print the current time
        #print(now) >>> These two lines print the current time
        if now == set_alarm_timer:
            print("Wake up! Grab adsjdfhkjamakeup! ")
            if platform.system() == "Windows":
                winsound.Beep(5000,1000)
            elif platform.system() == "Linux":
                os.system('beep -f 5000')
            break

def actual_time():
    set_alarm_timer = f"{hour.get()}:{minute.get()}:{second.get()}"
    alarm(set_alarm_timer)
# create tkinter window
clock = Tk()
clock.title("Alarm Clock")
clock.geometry("320x200")
# tkinter labels
time_format=Label(clock, text= "Enter time in 24 hour format!", fg="blue",bg="orange",font="calibri").place(x=40,y=170)
setYourAlarm = Label(clock,text = "Alert Time",fg="blue",relief = "solid",font=("calibri",10,"bold")).place(x=120, y=10)
Hour_label = Label(clock,text = "Hour",fg="blue",relief = "solid",font=("calibri",10)).place(x=30, y=45)
Min_label  = Label(clock,text = "Minutes",fg="blue",relief = "solid",font=("calibri",10)).place(x=30, y=75)
Seconds_label = Label(clock,text = "Seconds",fg="blue",relief = "solid",font=("calibri",10)).place(x=30, y=105)

# The Variables we require to set the alarm(initialization):

hour   = StringVar()
minute = StringVar()
second = StringVar()

# Time required to set the alarm clock:
# Creating the entries >>> Adding hour-minute-second
hourTime= Entry(clock,textvariable = hour,bg = "pink",width = 15).place(x=95,y=45)
minTime= Entry(clock,textvariable = minute,bg = "pink",width = 15).place(x=95,y=75)
secTime = Entry(clock,textvariable = second,bg = "pink",width = 15).place(x=95,y=105)

# To take the time input by user and creating the clickable button:

submit = Button(clock,text = "Set Alarm",fg="red",width = 10,command = actual_time).place(x = 105,y=135)

# Starting Clock and Tkinter
clock.mainloop()
