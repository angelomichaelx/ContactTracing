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

    def search_name(self):
        name_entry = self.search_entry.get()

        #data informationg files
        with open("information.csv", "r", newline = "") as file:
            reader = csv.reader(file)
            found_entries = []
            for row in reader:
                if name_entry in row[0]:
                    found_entries.append(row)

        #print
        if found_entries:
            for i, entry in enumerate(found_entries):
                result = f"Name: {entry[0]}\n"
                result += f"Gender: {entry[1]}\n"
                result += f"Date of Birth: {entry[2]}\n"
                result += f"Age: {entry[3]}\n"
                result += f"Email Address: {entry[4]}\n"
                result += f"Name of City: {entry[5]}\n"
                result += f"Vaccination Status: {entry[6]}\n"
                result += f"Symptoms of COVID-19: {entry[7]}\n"
                result += f"Exposure to COVID-19: {entry[8]}\n"
                result += f"COVID-19 Test Status: {entry[9]}"

                result = tk.Label(text = result, font = ("Arial", 20) , justify=("left"), bg = "light blue")
                result.place(x = 180, y = 200)
                
        #if the user are not registered
        else:
            noresult = tk.Label(text="ERROR!PERSON IS NOT REGISTERED.")
            noresult.place(x = 25, y = 100)