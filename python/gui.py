import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog

def mainw(): # Main Window
        window = Tk()
        window.geometry("400x150")
        window.title("TITLE ")
        button_name = Button(window,
                                text="Button Name",
                                command=command_name) # Button commnad line 22
        button_name.pack(side=tk.TOP)
        Exit_Button = Button(window,
                             text="Exit",
                             fg="black",
                             command=quit)
        Exit_Button.pack(side=tk.BOTTOM)
        window.mainloop()

def command_name(): #command for button on line 13
        popup = Tk()
        NS = ""
        A = ""
        popup.title("Title  ")
        popup.geometry("450x150+10+20")
        popup_txt = tk.Label(popup, text="Version " )
        Close_Button = Button(popup,
                                text="close",
                                command=popup.destroy)
        Close_Button.pack(side=tk.BOTTOM)
        About_Button = Button(popup,
                                text="reset",
                                command=quit)
        About_Button.pack(side=tk.BOTTOM)
        popup_txt.pack()
        popup_txt.mainloop()      
mainw()
