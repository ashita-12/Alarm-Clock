from tkinter.ttk import Combobox
from tkinter import Label, Tk, Frame, Radiobutton, IntVar
from PIL import ImageTk, Image
from pygame import mixer
from datetime import datetime
from time import sleep
import threading

# Colors
bg_color = '#ffffff'
co1 = "#566FC6"  # blue
co2 = "#000000"  # black

# Window
window = Tk()
window.title("")
window.geometry('350x150')
window.configure(bg=bg_color)

# Frame up
frame_line = Frame(window, width=400, height=5, bg=co1)
frame_line.grid(row=0, column=0)

frame_body = Frame(window, width=400, height=290, bg=bg_color)
frame_body.grid(row=1, column=0)

# Configuring frame body
img = Image.open('C:\\Users\\ashit\\OneDrive\\Desktop\\Alarm Clock\\image.png')
img = img.resize((100, 100))
img = ImageTk.PhotoImage(img)

app_image = Label(frame_body, height=100, image=img, bg=bg_color)
app_image.place(x=10, y=10)

name = Label(frame_body, text="Alarm", height=1, font=('Ivy 18 bold'), bg=bg_color)
name.place(x=125, y=10)

# Hour
label_hour = Label(frame_body, text="hour", height=1, font=('Ivy 10 bold'), bg=bg_color, fg=co1)
label_hour.place(x=127, y=40)
c_hour = Combobox(frame_body, width=2, font=('arial 15'))
c_hour['values'] = ("00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12")
c_hour.current(0)
c_hour.place(x=130, y=58)

# Minute
label_minute = Label(frame_body, text="min", height=1, font=('Ivy 10 bold'), bg=bg_color, fg=co1)
label_minute.place(x=177, y=40)
c_min = Combobox(frame_body, width=2, font=('arial 15'))
c_min['values'] = tuple(f"{i:02d}" for i in range(60))
c_min.current(0)
c_min.place(x=180, y=58)

# Second
label_second = Label(frame_body, text="sec", height=1, font=('Ivy 10 bold'), bg=bg_color, fg=co1)
label_second.place(x=227, y=40)
c_sec = Combobox(frame_body, width=2, font=('arial 15'))
c_sec['values'] = tuple(f"{i:02d}" for i in range(60))
c_sec.current(0)
c_sec.place(x=230, y=58)

# Period
label_period = Label(frame_body, text="period", height=1, font=('Ivy 10 bold'), bg=bg_color, fg=co1)
label_period.place(x=277, y=40)
c_period = Combobox(frame_body, width=3, font=('arial 15'))
c_period['values'] = ("AM", "PM")
c_period.current(0)
c_period.place(x=280, y=58)

def activate_alarm():
    t = threading.Thread(target=alarm)
    t.start()

def deactivate_alarm():
    print('Deactivate alarm:', selected.get())
    mixer.music.stop()

selected = IntVar()

rad1 = Radiobutton(frame_body, font=('arial 10 bold'), value=1, text="Activate", bg=bg_color, command=activate_alarm, variable=selected)
rad1.place(x=125, y=95)

def sound_alarm():
    mixer.music.load('C:\\Users\\ashit\\OneDrive\\Desktop\\Alarm Clock\\morning-joy-alarm-clock-20961.mp3')
    mixer.music.play()
    selected.set(0)

rad2 = Radiobutton(frame_body, font=('arial 10 bold'), value=2, text="Deactivate", bg=bg_color, command=deactivate_alarm, variable=selected)
rad2.place(x=187, y=95)

def alarm():
    while True:
        control = selected.get()
        print(control)

        alarm_hour = c_hour.get()
        alarm_min = c_min.get()
        alarm_sec = c_sec.get()
        alarm_period = c_period.get()
        alarm_period = str(alarm_period).upper()

        now = datetime.now()

        current_hour = now.strftime("%I")
        current_min = now.strftime("%M")
        current_sec = now.strftime("%S")
        current_period = now.strftime("%p")

        if control == 1:
            if alarm_period == current_period:
                if alarm_hour == current_hour:
                    if alarm_min == current_min:
                        if alarm_sec == current_sec:
                            print("Time to take a break!")
                            sound_alarm()
        sleep(1)

mixer.init()

window.mainloop()