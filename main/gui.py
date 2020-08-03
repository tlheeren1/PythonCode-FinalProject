"""
Program: gui.py
Author:  Tara Heeren
Date: 7/25/2020

This is the program that creates the gui to get file paths and run compare on files
"""
import tkinter as tk
import os as os
from tkinter.filedialog import askopenfile
from file_compare import file_compare as fc


def button_compare_on_click():
    try:
        file1 = entry_1.get()
    except:
        file1 = 1
    try:
        file2 = entry_2.get()
    except:
        label_action = tk.Label(main_window, text='Must input path/file of second file')
        label_action.grid(row=8, columnspan=180)
        file2 = 1
    try:
        user_delimiter = entry_4.get()
    except:
        label_action = tk.Label(main_window, text='Must input file delimiter (,|)')
        label_action.grid(row=8, columnspan=180)
        user_delimiter = 1
    try:
        file_name = entry_3.get()
    except:
        file_name = 1

    #print(file1) # debug
    #print(file2) # debug
    #print(user_delimiter) # debug
    #print(file_name) # debug
    #print(entry_3.get()) # debug

    if file1 != 1 and file2 != 1 and user_delimiter != 1:
        if os.path.isfile(str(file1)) and os.path.isfile(str(file2)) and entry_4.get():
            # print('In if 1') # debug
            if os.path.isfile(str(file1)) and os.path.isfile(str(file2)) and file_name != '':
                # print('In if 2') # debug
                # print(file_name)
                fc.compare_file(file1, file2, user_delimiter, file_name)
            else:
                # print('In else 1') # debug
                fc.compare_file(file1, file2, user_delimiter)
        else:
            # print('in else 2') # debug
            print('Please input file with the path and/or delimiter')
    else:
        print('Please input file(s) with the path and/or delimiter')


main_window = tk.Tk()
main_window.minsize(800, 200)
main_window.title('Compare files')
button_text = 'Browse'

label_file_path_1 = tk.Label(main_window, text='Path to File 1: ')
label_file_path_1.grid(row=1, columnspan=9)

label_file_path_2 = tk.Label(main_window, text='Path to File 2: ')
label_file_path_2.grid(row=2, columnspan=9)

label_file_output = tk.Label(main_window, text='Output File Name: ')
label_file_output.grid(row=3, columnspan=9)

label_file_delimiter = tk.Label(main_window, text='delimiter')
label_file_delimiter.grid(row=4, columnspan=9)

entry_1 = tk.Entry(main_window, width=100)
entry_1.grid(row=1, column=10, columnspan=180)

entry_2 = tk.Entry(main_window, width=100)
entry_2.grid(row=2, column=10, columnspan=180)

entry_3 = tk.Entry(main_window, width=100)
entry_3.grid(row=3, column=10, columnspan=180)

entry_4 = tk.Entry(main_window, width=100)
entry_4.grid(row=4, column=10, columnspan=180)

button_1 = tk.Button(main_window, text=button_text, width=10, state='disabled') # , command=button_start_on_click)
button_1.grid(row=1, column=190)

button_2 = tk.Button(main_window, text=button_text, width=10, state='disabled') #, command=button_2_on_click, state='disabled')
button_2.grid(row=2, column=190)

button_compare = tk.Button(main_window, text='Compare Files', width=20, command=button_compare_on_click)
button_compare.grid(row=6, column=1, columnspan=20, sticky=tk.W+tk.E)

button_exit = tk.Button(main_window, text='Exit', width=20,
                        command=main_window.destroy).grid(row=6, column=25, columnspan=25, sticky=tk.W+tk.E)

main_window.mainloop()
