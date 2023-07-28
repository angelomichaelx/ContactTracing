##Michael Angelo P. Biag
##BSCPE 1-4

#importing file
import tkinter as tk
import csv

#creating class
class search_area(tk.Frame):
    def __init__(self, master = None):
        super().__init__(master)
        self.configure(bg = "light blue")

#creating buttons and search bar for search area
        self.search_title = tk.Label(self, text = "SEARCH YOUR ENTRY HERE", font = ("Times", 30), bg = "light blue")
        self.search_title.place(x = 115, y = 25)

        self.search_label = tk.Label(self, text = "Enter Name to Search:", font = ("Times", 15), bg = "light blue")
        self.search_label.place(x = 125, y = 100)

        self.search_entry = tk.Entry(self, bg = "light blue")
        self.search_entry.place(x = 550, y = 100)

        self.search_button = tk.Button(self, text= "  Search  ", command = self.search_name, bg = "white")
        self.search_button.place(x = 385, y = 100)