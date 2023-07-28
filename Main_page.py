##Michael Angelo P. Biag
##BSCPE 1-4

#IMPORTING FILES
import tkinter as tk
from add_data import add_data
from search_area import search_area
#creating class
class main_page(tk.Tk):
    def __init__(self):
        super().__init__()
        #title
        self.title("COVID-14 Contact Tracing APP")
        #size
        self.geometry("780x600")
        self.configure(bg = "light blue")
        #title
        self.main_title = tk.Label(self, text = "COVID-19 \n CONTACT TRACING \n FORM", font = ("Times", 45), bg = "light blue")
        self.main_title.place(x = 120, y = 10)
        
        #buttons
        self.add = tk.Button(self, text = "       Add       ", command = main_page.go_to_add_entry, font = ("Helvetica", 20), bg = "white")
        self.add.place(x = 325, y = 300)

        self.search = tk.Button(self, text = "     Search    ", command = main_page.go_to_search_entry, font = ("Helvetica", 20), bg = "white")
        self.search.place(x = 325, y = 400)

        self.exit = tk.Button(self, text = "       Exit       ", command = self.exit, font = ("Helvetica", 20),  bg = "white")
        self.exit.place(x = 325, y = 500)

    def go_to_add_entry():
        entry = add_data()
        entry.place(relwidth = 1, relheight = 1)

    def go_to_search_entry():
        search = search_area()
        search.place(relwidth = 1, relheight = 1)

    def exit(self):
        self.destroy()

if __name__=="__main__":
    covid = main_page()
    covid.mainloop()
        