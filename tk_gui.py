#!/usr/bin/env python3
"""
This is a basic tool that expects user input for the input file, which is
expected to be a CSV file with 2 columns:
first column will be imageA and column B is imageB
The idea is to compare both images, the program will resize them and compare
them using 2 different algorithms then will evaluate their similarity where
0 means that the images are fairly equal.
"""

import tkinter as tk
from tkinter import filedialog, messagebox
import image_diff_score

input_file_path = None

def run_process():
    print("Parameters:")
    print(f"in: {input_file_path}")
    image_diff_score.process_csv(input_file_path)


def close_app():
    print("Bye")
    app.destroy()

def select_input_file():
    global input_file_path
    input_file_path = filedialog.askopenfilename(filetypes=(("CSV files", "*.csv"), ("Any file", "*")))
    print(input_file_path)

# Create the Tkinter interface.
app = tk.Tk()
app.geometry('475x275')
app.title("Selecting CSV File")

# Create the window header.
header = tk.Label(app, text="Welcome to the image Compare tool", fg="blue", font=("Arial Bold", 14))
header.pack(side="top", ipady=10)

# Create the input button:
input_button = tk.Button(app, text='Select input file', command=select_input_file)
input_button.pack()


process_button = tk.Button(app, text='Process', width=25, command=run_process)
process_button.pack()

exit_button = tk.Button(app, text='Close', width=25, command=close_app)
exit_button.pack()

app.mainloop()
