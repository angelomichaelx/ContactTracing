##Michael Angelo P. Biag
##BSCPE 1-4

#importing 
import tkinter as tk
import csv
from tkinter import messagebox

#creating class
class add_data(tk.Frame):
    def __init__(self, master = None):
        super().__init__(master)
        self.configure(bg = "light blue")

# title
        self.personal = tk.Label(self, text = "CONTACT TRACING FORM", font=("Times", 20), bg = "light blue")
        self.personal.place(x = 180, y = 5)