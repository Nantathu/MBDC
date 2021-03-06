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
        global var
        var = pickle.load(open('var_data.pickle', 'rb'))

def button_clear():
    entry.delete(0, END)
    entry.insert(0, 0)
    variable = 0

def button_log():
    messagebox.showinfo('Qbi moment last occured at:', current_date)

#Main window functions and configuration.
window = Tk()
window.title("Qbi moment counter")
window.configure(bg = "black")
window.geometry("254x129")
window.resizable(False, False)

#Path of the pickle file that contains variable data.
file = pathlib.Path('var_data.pickle')

#Current date
current_date = datetime.today().strftime('%Y-%m-%d-%H:%M')

#Entries
entry = Entry(window, width="8")
entry.grid(row = 0, column = 3, sticky = W)

#Declaration of "var" variable to read data from pickle file.
if file.exists():
    var = pickle.load(open('var_data.pickle', 'rb'))
elif file.exists() == False:
    variable = 0
    pickle.dump(variable, open('var_data.pickle', 'wb'))

#Checks if file exists to update var value
if file.exists():
    entry.insert(0, var)
else:
    entry.insert(0, 0)

#Buttons
psycha = Label(window, text = "Qbi moment: ", bg = "black", fg = "white")
psycha.grid(row = 0, column = 1, sticky = W)
button_psy = Button (window, text = "QBI MOMENT", bg = "black", fg = "white", activebackground = "white", activeforeground = "black", width = "10", command = lambda: button_click(1))
button_psy.grid(row = 0, column = 0, sticky = E)
button_clear = Button (window, text = "CLEAR", bg = "black", fg = "white", activebackground = "white", activeforeground = "black", width = "35", command = button_clear)
button_clear.grid(row = 1, column = 0, columnspan = 4, sticky = W)
button_log = Button (window, text = "LOGS", bg = "black", fg = "white", activebackground = "white", activeforeground = "black", width = "35", command = button_log)
button_log.grid(row = 2, column = 0, columnspan = 4, sticky = W)
button_load = Button (window, text = "LOAD", bg = "black", fg = "white", activebackground = "white", activeforeground = "black", width = "35", command = load_data)
button_load.grid(row = 3, column = 0, columnspan = 4, sticky = W)
button_save = Button (window, text = "SAVE", bg = "black", fg = "white", activebackground = "white", activeforeground = "black", width = "35", command = save_data)
button_save.grid(row = 4, column = 0, columnspan = 4, sticky = W)

#Function closing main window.
window.protocol("WM_DELETE_WINDOW", on_closing)

#Function that keeps window running and not closing itself.
window.mainloop()
