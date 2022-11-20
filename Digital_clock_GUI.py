from tkinter import Label,Tk
import time

#title and size
app_window=Tk()
app_window.title("Digital Clock")
app_window.geometry("420x150")
app_window.resizable(1,1)

#the font of the time and its colour, its border width and the background colour of the digital clock
text_font=("Boulder",68,'bold')
background="#ffffff"
foreground="#363529"
border_width=25

#combinig all element for label of the clock

label=Label(app_window,font=text_font,bg=background,fg=foreground,bd=border_width)
label.grid(row=0,column=1)

#main function for digital clock

def digital_clock():
    time_live=time.strftime("%H:%M:%S")
    label.config(text=time_live)
    label.after(200,digital_clock)

digital_clock()
app_window.mainloop()

