from tkinter import *
class Application(Frame):
    # main class for calculator
    def __init__(self,master):   #master represents the parent widget.
        # initialize the frame
        super(Application, self).__init__(master)
        self.task = ""
        self.UserIn = StringVar()
        self.grid()   #grid() method is used to register widgets with the grid geometry manager. The geometry manager manages the placement and layout of the elements of the GUI
        self.create_widgets()

    def create_widgets(self):
        # create all the buttons for calculator.
        # user input stored  as an Entry widget
        self.user_input = Entry(self, bg="#5BCBAC", bd=29, insertwidth=4, width=24, font=("Verdana", 20, "bold"), textvariable=self.UserIn, justify=RIGHT)
        self.user_input.grid(columnspan=4)

        self.user_input.insert(0, "0")

        # button for value 7
        self.button1 = Button(self, bg="#98DBC8", bd=12, text="7", padx=33, pady=25,
                                font=("Helvetica", 20, "bold"), command=lambda: self.buttonClick(7))
        self.button1.grid(row=2, column=0, sticky=W)

        # button for value 8
        self.button2 = Button(self, bg="#98DBC8", bd=12, text="8", padx=33, pady=25,
                              font=("Helvetica", 20, "bold"), command=lambda: self.buttonClick(8))
        self.button2.grid(row=2, column=1, sticky=W)

        # button for value 9
        self.button3 = Button(self, bg="#98DBC8", bd=12, text="9", padx=33, pady=25,
                              font=("Helvetica", 20, "bold"), command=lambda: self.buttonClick(9))
        self.button3.grid(row=2, column=2, sticky=W)

        # button for value 4
        self.button4 = Button(self, bg="#98DBC8", bd=12, text="4", padx=33, pady=25,
                              font=("Helvetica", 20, "bold"), command=lambda: self.buttonClick(4))
        self.button4.grid(row=3, column=0, sticky=W)

        # button for value 5
        self.button5 = Button(self, bg="#98DBC8", bd=12, text="5", padx=33, pady=25,
                              font=("Helvetica", 20, "bold"), command=lambda: self.buttonClick(5))
        self.button5.grid(row=3, column=1, sticky=W)

        # button for value 6
        self.button6 = Button(self, bg="#98DBC8", bd=12, text="6", padx=33, pady=25,
                              font=("Helvetica", 20, "bold"), command=lambda: self.buttonClick(6))
        self.button6.grid(row=3, column=2, sticky=W)

        # button for value 1
        self.button7 = Button(self, bg="#98DBC8", bd=12, text="1", padx=33, pady=25,
                              font=("Helvetica", 20, "bold"), command=lambda: self.buttonClick(1))
        self.button7.grid(row=4, column=0, sticky=W)

        # button for value 2
        self.button8 = Button(self, bg="#98DBC8", bd=12, text="2", padx=33, pady=25,
                              font=("Helvetica", 20, "bold"), command=lambda: self.buttonClick(2))
        self.button8.grid(row=4, column=1, sticky=W)

        # button for value 3
        self.button9 = Button(self, bg="#98DBC8", bd=12, text="3", padx=33, pady=25,
                              font=("Helvetica", 20, "bold"), command=lambda: self.buttonClick(3))
        self.button9.grid(row=4, column=2, sticky=W)

        # button for value 0
        self.button0 = Button(self, bg="#98DBC8", bd=12, text="0", padx=33, pady=25,
                              font=("Helvetica", 20, "bold"), command=lambda: self.buttonClick(0))
        self.button0.grid(row=5, column=0, sticky=W)

        # button for addition sign
        self.Addbutton = Button(self, bg="#98DBC8", bd=12, text="+", padx=37, pady=25,
                              font=("Helvetica", 20, "bold"), command=lambda: self.buttonClick("+"))
        self.Addbutton.grid(row=2, column=3, sticky=W)

        # button for subtraction sign
        self.Subbutton = Button(self, bg="#98DBC8", bd=12, text="-", padx=40, pady=25,
                                font=("Helvetica", 20, "bold"), command=lambda: self.buttonClick("-"))
        self.Subbutton.grid(row=3, column=3, sticky=W)

        # button for multiplication sign
        self.Mulbutton = Button(self, bg="#98DBC8", bd=12, text="*", padx=39, pady=25,
                                font=("Helvetica", 20, "bold"), command=lambda: self.buttonClick("*"))
        self.Mulbutton.grid(row=4, column=3, sticky=W)

        # button for division sign
        self.Divbutton = Button(self, bg="#98DBC8", bd=12, text="/", padx=40, pady=23,
                                font=("Helvetica", 20, "bold"), command=lambda: self.buttonClick("/"))
        self.Divbutton.grid(row=5, column=3, sticky=W)

        # button for equal sign
        self.Equalbutton = Button(self, bg="#E6D72A", bd=12, text="=", padx=33, pady=24,
                                font=("Helvetica", 20, "bold"), command=self.CalculateTask)
        self.Equalbutton.grid(row=5, column=1, sticky=W)

        # button for AC
        self.Clearbutton = Button(self, bg="#E6D72A", bd=12, text="AC", width=28, padx=7,
                                font=("Helvetica", 20, "bold"), command=self.ClearDisplay)
        self.Clearbutton.grid(row=1, columnspan=4, sticky=W)

        #button for decimal
        self.decimal = Button(self, bg="#98DBC8", bd=12, text=".", padx=37, pady=23,
                                font=("Helvetica", 20, "bold"), command=lambda: self.buttonClick("."))
        self.decimal.grid(row=5, column=2, sticky=W)

    def buttonClick(self, number):
        self.task = str(self.task) + str(number)
        self.UserIn.set(self.task)

    def CalculateTask(self):
        self.data = self.user_input.get()
        try:
            self.answer =  eval(self.data)
            self.displayText(self.answer)
            self.task = self.answer
        except SyntaxError as e:
            self.displayText("Invalid Syntex!")
            self.task = ""

    def displayText(self, value):
        self.user_input.delete(0, END)
        self.user_input.insert(0, value)

    def ClearDisplay(self):
        self.task = ""
        self.user_input.delete(0, END)
        self.user_input.insert(0, "0")

calculator = Tk()
calculator.title("Calculator")
app = Application(calculator)
# make window fixed
calculator.resizable(width=False, height=False)
calculator.mainloop()
