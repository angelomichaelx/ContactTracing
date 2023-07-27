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

        # Ask the Full name of the user
        self.name = tk.Label(self, text = "Full Name:", bg = "light blue")
        self.name.place(x = 55, y = 50)

        self.name_entry = tk.Entry(self, bg = "light blue")
        self.name_entry.place(x = 140, y = 50)

        # Ask the Gender of the user
        self.gender = tk.Label(self, text = "Gender:", bg = "light blue")
        self.gender.place(x = 350, y = 50)

        self.gender_entry = tk.Entry(self, bg = "light blue")
        self.gender_entry.place(x = 445, y = 50)

        # Ask the date of birth of the user
        self.birthdate = tk.Label(self, text = "Date of Birth:", bg = "light blue")
        self.birthdate.place(x = 55, y = 100)

        self.birthdate_entry = tk.Entry(self, bg = "light blue")
        self.birthdate_entry.place(x = 140, y = 100)

        # Ask the age of the user
        self.age = tk.Label(self, text = "Age:", bg = "light blue")
        self.age.place(x = 350, y = 100)

        self.age_entry = tk.Entry(self, bg = "light blue")
        self.age_entry.place(x = 445, y = 100)

        # Ask the email adress
        self.email = tk.Label(self, text = "Email Address:", bg = "light blue")
        self.email.place(x = 55, y = 150)

        self.email_entry = tk.Entry(self, bg = "light blue")
        self.email_entry.place(x = 140, y = 150)

        # Ask the name of current city where he/she stay
        self.city = tk.Label(self, text = "Current City where you stay:", bg = "light blue")
        self.city.place(x = 280, y = 150)

        self.city_entry = tk.Entry(self, bg = "light blue")
        self.city_entry.place(x = 445, y = 150)
        
        # Ask the vaccination status
        self.vaccination = tk.Label(self, text = "Have you been vaccinated for COVID-19?", bg = "light blue")
        self.vaccination.place(x = 30, y = 200)

        self.choice = tk.StringVar()

        self.choice1= tk.Radiobutton(self, text = "Not yet", variable = self.choice, value = "Not yet", bg = "light blue")
        self.choice1.place(x = 30, y = 225)

        self.choice2= tk.Radiobutton(self, text = "1st Dose", variable = self.choice, value = "1st Dose", bg = "light blue")
        self.choice2.place(x = 30, y = 250)

        self.choice3= tk.Radiobutton(self, text = "2nd Dose", variable = self.choice, value = "2nd Dose", bg = "light blue")
        self.choice3.place(x = 30, y = 275)

        self.choice4= tk.Radiobutton(self, text = "1st Booster Shot", variable = self.choice, value = "1st Booster Shot", bg = "light blue")
        self.choice4.place(x = 30, y = 300)

        self.choice5= tk.Radiobutton(self, text = "2nd Booster Shot", variable = self.choice, value = "2nd Booster Shot", bg = "light blue")
        self.choice5.place(x = 30, y = 325)

        # Ask if there are symptoms of COVID-19
        self.symptom = tk.Label(self, text = "Do you have any symptoms of COVID-19?", bg = "light blue")
        self.symptom.place(x = 30, y = 375)

        self.symptomchoice = tk.StringVar()

        self.symptomchoice1 = tk.Radiobutton(self, text = "Yes", variable = self.symptomchoice, value = "Yes", bg = "light blue")
        self.symptomchoice1.place(x = 30, y = 400)
        
        self.symptomchoice2 = tk.Radiobutton(self, text = "No", variable = self.symptomchoice, value = "No", bg = "light blue")
        self.symptomchoice2.place(x = 30, y = 425)
        
        self.symptomchoice3 = tk.Radiobutton(self, text = "Uncertain", variable = self.symptomchoice, value = "Uncertain", bg = "light blue")
        self.symptomchoice3.place(x = 30, y = 450)

        # Ask if there are exposure on someone with COVID-19
        self.exposure = tk.Label(self, text = "Have you had in contact with somebody that has COVID symptoms in the past 7 days?", bg = "light blue")
        self.exposure.place(x = 300, y = 375)

        self.exposurechoice = tk.StringVar()

        self.exposurechoice1 = tk.Radiobutton(self, text = "Yes", variable = self.exposurechoice, value = "Yes", bg = "light blue")
        self.exposurechoice1.place(x = 300, y = 400)
        
        self.exposurechoice2 = tk.Radiobutton(self, text = "No", variable = self.exposurechoice, value = "No", bg = "light blue")
        self.exposurechoice2.place(x = 300, y = 425)
        
        self.exposurechoice3 = tk.Radiobutton(self, text = "Uncertain", variable = self.exposurechoice, value = "Uncertain", bg = "light blue")
        self.exposurechoice3.place(x = 300, y = 450)
        
        # Ask if tested positive on COVID-19 in the last 14 days
        self.test = tk.Label(self, text = "Have you been tested for COVID-19 in the last 14 days?", bg = "light blue")
        self.test.place(x = 300, y = 200)

        self.testchoice = tk.StringVar()

        self.testchoice1 = tk.Radiobutton(self, text = "No", variable = self.testchoice, value = "No", bg = "light blue")
        self.testchoice1.place(x = 300, y = 225)

        
        self.testchoice2 = tk.Radiobutton(self, text = "Yes - Positive", variable = self.testchoice, value = "Yes - Positive", bg = "light blue")
        self.testchoice2.place(x = 300, y = 250)
        
        self.testchoice3 = tk.Radiobutton(self, text = "Yes - Negative", variable = self.testchoice, value = "Yes - Negative", bg = "light blue")
        self.testchoice3.place(x = 300, y = 275)

        self.testchoice4 = tk.Radiobutton(self, text = "Yes - Pending", variable = self.testchoice, value = "Yes - Pending", bg = "light blue")
        self.testchoice4.place(x = 300, y = 300)

        #BUTTONS
         # Added a submit button 
        self.submit = tk.Button(self, text = "  Submit  ", command = self.get_data, bg = "green")
        self.submit.place(x = 200, y = 525)

        # Add an exit Button
        self.exit = tk.Button(self, text = "  Exit  ", command = self.close, bg = "red")
        self.exit.place(x = 350, y = 525)

    def close(self):
        self.master.destroy()
        # Get the information gathered from user
    def get_data(self):
        name = self.name_entry.get()
        gender = self.gender_entry.get()
        birthdate = self.birthdate_entry.get()
        age = self.age_entry.get()
        email = self.email_entry.get()
        city = self.city_entry.get()
        vaccinationstatus = self.choice.get()
        symptomstatus = self.symptomchoice.get()
        exposurestatus = self.exposurechoice.get()
        teststatus = self.testchoice.get()
         
        # Save the information gathered into excel file using csv
        with open("information.csv", "a", newline = "") as file:
            store = csv.writer(file)
            store.writerow([name, gender, birthdate, age, email, city, vaccinationstatus, symptomstatus, exposurestatus, teststatus])

        # Create a messagebox that will let the user know that their data has ben submitted
        messagebox.showinfo("Admin", "Thank you for your time. STOP THE SPREAD, WASH YOUR HANDS.")
        self.clear_entry()
