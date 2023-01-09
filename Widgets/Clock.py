import tkinter
import time


def time_clock():
    current_time = time.strftime('%H : %M : %S')
    clock.config(text=current_time)  # Sets the time on Label.
    clock.after(60, time_clock)  # Call function once after given time.


window = tkinter.Tk()
window.geometry('250x200')  # Dimension of Clock window.
window.title("python.ints_")
tkinter.Label(window, text='Digital Clock', font='times 24 bold').pack(pady=20)
clock = tkinter.Label(window, font='Arial 24 bold', fg='white', bg='#000000')
clock.pack(pady=20, ipadx=10)
time_clock()

window.mainloop()
