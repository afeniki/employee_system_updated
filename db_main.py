import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from tkinter import ttk
from PIL import ImageTk, Image
import pymysql
import os
import shutil
import db_config

def on_tab_selected(event):
    selected_tab = event.widget.select()
    tab_text = event.widget.tab(selected_tab, "text")

    if tab_text == "All Records":
        print("All records tab selected")
    if tab_text == "Add New Record":
        print("Add new records tab selected")

def load_database_results():
    return


file_name = "default.png"
path = db_config.PHOTO_DIRECTORY + file_name
rows = None #none is an object that contains nothing
num_of_rows = None

form = tk.Tk()
form.title("Database Form")
form.geometry("500x280")

tab_parent = ttk.Notebook(form)  #helps to set up(design and manage) tabs
tab1 = ttk.Frame(tab_parent)
tab2 = ttk.Frame(tab_parent)

tab_parent.bind("<<NotebookTabChanged>>", on_tab_selected)

tab_parent.add(tab1, text="All Records")
tab_parent.add(tab2, text="Add New Record")


firstLabelTabOne = tk.Label(tab1, text="First Name:")
familyLabelTabOne = tk.Label(tab1, text="Family Name:")
jobLabelTabOne = tk.Label(tab1, text="Job Title:")

firstEntryTabOne = tk.Entry(tab1)
familyEntryTabOne = tk.Entry(tab1)
jobEntryTabOne = tk.Entry(tab1)

openImageTabOne = Image.open(path)
imgTabOne = ImageTk.PhotoImage(openImageTabOne)
imgLabelTabOne = tk.Label(tab1, image=imgTabOne)

buttonForward = tk.Button(tab1, text="Forward")
buttonBack = tk.Button(tab1, text="Back")

#ADD WIDGETS TO GRID ON TAB
firstLabelTabOne.grid(row=0, column=0, padx=15, pady=15)
firstEntryTabOne.grid(row=0, column=1, padx=15, pady=15)

familyLabelTabOne.grid(row=1, column=0, padx=15, pady=15)
familyEntryTabOne.grid(row=1, column=1, padx=15, pady=15)

jobLabelTabOne.grid(row=2, column=0, padx=15, pady=15)
jobEntryTabOne.grid(row=2, column=1, padx=15, pady=15)

imgLabelTabOne.grid(row=0, column=2, rowspan=3, padx=15, pady=15)

buttonBack.grid(row=3, column=0, padx=15, pady=15)
buttonForward.grid(row=3, column=2, padx=15, pady=15)


#ADDING WIDGETS FOR TAB2
firstLabelTabTwo = tk.Label(tab2, text="FirstName:")
familyLabelTabTwo = tk.Label(tab2, text="FamilyName:")
jobLabelTabTwo = tk.Label(tab2, text="Job Title:")

firstEntryTabTwo = tk.Entry(tab2)
familyEntryTabTwo = tk.Entry(tab2)
jobEntryTabTwo = tk.Entry(tab2)

openImageTwo = Image.open(path)
imageTabTwo = ImageTk.PhotoImage(openImageTabOne)
imgLabelTabTwo = tk.Label(tab2, image=imageTabTwo)

buttonCommit = tk.Button(tab2, text="Add Record To Database")
buttonAddImage = tk.Button(tab2, text="Add Image")

#ADD WIDGETS ON TAB TWO
firstLabelTabTwo.grid(row=0, column=0, padx=15, pady=15)
firstEntryTabTwo.grid(row=0, column=1, padx=15, pady=15)

familyLabelTabTwo.grid(row=1, column=0, padx=15, pady=15)
familyEntryTabTwo.grid(row=1, column=1, padx=15, pady=15)

jobLabelTabTwo.grid(row=2, column=0, padx=15, pady=15)
jobEntryTabTwo.grid(row=2, column=1, padx=15, pady=15)

imgLabelTabTwo.grid(row=0, column=2, rowspan=3, padx=15, pady=15)


buttonCommit.grid(row=4, column=1, padx=15, pady=15)
buttonAddImage.grid(row=4, column=2, padx=15, pady=15)


tab_parent.pack(expand=1, fill="both")

# Set up a connection object
# Write an SQL
# Set cursor object
# Fetch rows back from the database table
# Display result
form.mainloop()
