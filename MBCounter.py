from tkinter import *
from tkinter import messagebox
from datetime import datetime
import pathlib
import pickle



def button_click(number):
    current = entry.get()
    entry.delete(0, END)
    global variable
    variable = int(current) + int(number)
    entry.insert(0, int(variable))

def on_closing():
    if messagebox.askokcancel("Quit", "Are you sure you want to quit?"):
            window.destroy()

def save_data():
    pickle.dump(variable, open('var_data.pickle', 'wb'))

def load_data():
    if file.exists ():
        var

def button_clear():
    entry.delete(0, END)
    entry.insert(0, 0)
    global variable
    variable = 0

def button_log():
    messagebox.showinfo('Last mental breakdown:', current_date)



#Main window functions and configuration.
window = Tk()
window.title("Mental Breakdown Counter")
window.configure(bg="black")
window.geometry("254x129")
window.resizable(False, False)


#Declaration of "var" variable to read data from pickle file.
var = pickle.load(open('var_data.pickle', 'rb'))

#Path of the pickle file that contains variable data.
file = pathlib.Path('var_data.pickle')

#Current date
current_date = datetime.today().strftime('%Y-%m-%d-%H:%M')

#Entries
entry = Entry(window, width="8")
entry.grid(row = 0, column = 3, sticky = W)

#Checks if file exists to update var value
if file.exists():
    entry.insert(0, var)
else:
    entry.insert(0, 0)

#Buttons
psycha = Label(window, text="Mental breakdown", bg="black", fg="white")
psycha.grid(row = 0, column = 1, sticky = E)
button_psy = Button (window, text="MENTAL", bg="black", fg="white", activebackground="white", activeforeground="black", width="10", command=lambda: button_click(1))
button_psy.grid(row = 0, column = 0)
button_clear = Button (window, text="CLEAR", bg="black", fg="white", activebackground="white", activeforeground="black", width="35", command = button_clear)
button_clear.grid(row = 1, column = 0, columnspan = 4, sticky = W)
button_log = Button (window, text="LOGS", bg="black", fg="white", activebackground="white", activeforeground="black", width="35", command = button_log)
button_log.grid(row = 2, column = 0, columnspan = 4, sticky = W)
button_load = Button (window, text="LOAD", bg="black", fg="white", activebackground="white", activeforeground="black", width="35", command = load_data)
button_load.grid(row = 3, column = 0, columnspan = 4, sticky = W)
button_save = Button (window, text="SAVE", bg="black", fg="white", activebackground="white", activeforeground="black", width="35", command = save_data)
button_save.grid(row = 4, column = 0, columnspan = 4, sticky = W)

#Function closing main window.
window.protocol("WM_DELETE_WINDOW", on_closing)

#Function that keeps window running and not closing itself.
window.mainloop()
