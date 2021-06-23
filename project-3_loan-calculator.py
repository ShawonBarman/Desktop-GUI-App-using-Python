#import tkinter module which used to create GUI - standard interface to TK GUI Toolkit
from tkinter import *

#create a user defined class named: LoanCalculator which holds it's own
#data members and member functions.
class LoanCalculator:
    def __init__(self):  #special method in python class - constructor of a python class
        window = Tk()   #creates a window to house the calculator bits
        window.title("Loan Calculator")  #sets the titlw
        window.configure(background = "light green")  #sets background color for window

        #create input boxes: label function creates a display box to take input
        #the grid method gives it a table like structure
        #widgets are centered by default. Use sticky arguments to change:N,S,E,W
        Label(window, font="helvetica 12 bold", bg="light green", text="Annual Interest Rate").grid(row=1, column=1, sticky=W)
        Label(window, font="helvetica 12 bold", bg="light green", text="Number of years").grid(row=2, column=1, sticky=W)
        Label(window, font="helvetica 12 bold", bg="light green", text="Loan Amount").grid(row=3, column=1, sticky=W)
        Label(window, font="helvetica 12 bold", bg="light green", text="Monthly Payment").grid(row=5, column=1, sticky=W)
        Label(window, font="helvetica 12 bold", bg="light green", text="Total Payment").grid(row=6, column=1, sticky=W)

        #creates objects: firs 3objects to take inputs using entry() function
        self.annualInterestRateVar = StringVar()
        Entry(window, textvariable=self.annualInterestRateVar, justify=RIGHT).grid(row=1, column=2)
        self.numberofYearVar = StringVar()
        Entry(window, textvariable=self.numberofYearVar, justify=RIGHT).grid(row=2, column=2)
        self.loanAmountVar = StringVar()
        Entry(window, textvariable=self.loanAmountVar, justify=RIGHT).grid(row=3, column=2)
        self.monthlyPaymentVar = StringVar()
        lb1MonthlyPayment = Label(window, font="Helvetica 12 bold", bg="light green", textvariable=self.monthlyPaymentVar).grid(row=5, column=2, sticky=E)
        self.totalPaymentVar = StringVar()
        lb2TotalPayment = Label(window, font="Helvetica 12 bold", bg="light green", textvariable=self.totalPaymentVar).grid(row=6, column=2, sticky=E)

        #create button to calculate payment, when button is clicked it will the compute payment function
        btComputePayment = Button(window, text="Compute payment", bg="red", fg="white", font="Helvetica 14 bold", command=self.computePayment).grid(row=7, column=2, sticky=E)
        btClear = Button(window, text="Clear", bg="blue", fg="white", font="Helvetica 14 bold", command=self.delete_all).grid(row=7, column=8, padx=20, pady=20, sticky=E)

        window.mainloop()  #the mainlopp() function is used to run the application program

    #create function to compute total payment
    def computePayment(self):
        monthlyPayment = self.getMonthlyPayment(
            float(self.loanAmountVar.get()),
            float(self.annualInterestRateVar.get()) / 1200,
            int(self.numberofYearVar.get())
        )
        self.monthlyPaymentVar.set(format(monthlyPayment, "10.2f"))
        totalPayment = float(self.monthlyPaymentVar.get()) * 12 * int(self.numberofYearVar.get())
        self.totalPaymentVar.set(format(totalPayment, "10.2f"))

    def getMonthlyPayment(self, loanAmount, monthlyInterestRate, numberofYears):
        monthlyPayment = loanAmount * monthlyInterestRate / (1 - 1 / (1 + monthlyInterestRate)**(numberofYears*12))
        return monthlyPayment

    def delete_all(self):
        self.monthlyPaymentVar.set("")
        self.loanAmountVar.set("")
        self.annualInterestRateVar.set("")
        self.numberofYearVar.set("")
        self.totalPaymentVar.set("")

#call the class to run the program
LoanCalculator()