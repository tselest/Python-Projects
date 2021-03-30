# importing whole module
from tkinter import * 
from tkinter.ttk import *
  
# importing strftime function to
# retrieve system's time
# importing just time and then using time.strftime gives error
from time import strftime 
  
# creating tkinter window
window = Tk()
window.title('Clock')
  
# This function is used to 
# display time on the label
def digital():
    string = strftime('%H:%M:%S %p')
    label.config(text = string)
    label.after(1000, digital)
  
# Styling of the label widget >> Adding font, background and foreground
label = Label(window, font = ('jetbrains mono', 80), background = 'black', foreground = 'red')
  
# Placement of the clock at the centre of the tkinter window

label.pack(anchor = 'center')
digital()
  
mainloop()
