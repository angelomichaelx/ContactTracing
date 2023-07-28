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