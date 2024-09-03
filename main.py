from tkinter import *

window = Tk()
window.title("BMI Calculator")
window.geometry("300x240")
window.resizable(False, False)
window.config(bg="Dark Gray")


def calculateBMI():
    weight = float(weightEntry.get())
    height = float(heightEntry.get())

    pointHeight = height / 100
    pointHeightSquare = pointHeight * pointHeight
    return weight / pointHeightSquare


def checkValidNumbers():
    try:
        height = float(heightEntry.get())
        weight = float(weightEntry.get())
        return True
    except:
        return False


def runProgram():
    if checkValidNumbers():
        BMI = round(calculateBMI(), 2)
        BMIstr = str(BMI)
        if BMI <= 16.0:
            label.config(text=f"BMI = {BMIstr} / You are severely underweight",
                         font=("Arial", 12, "underline"), fg="#640606", bg="Dark Gray")
            label.place(x=150 - label.winfo_width() / 2, y=190)
            label.update()
            label.place(x=150 - label.winfo_width() / 2, y=190)
        elif 16.00 < BMI < 17.00:
            label.config(text=f"BMI = {BMIstr} / You are moderately underweight",
                         font=("Arial", 12, "underline"), fg="#C00909", bg="Dark Gray")
            label.place(x=150 - label.winfo_width() / 2, y=190)
            label.update()
            label.place(x=150 - label.winfo_width() / 2, y=190)
        elif 17.00 < BMI < 18.49:
            label.config(text=f"BMI = {BMIstr} / You are underweight",
                         font=("Arial", 12, "underline"), fg="#F10909", bg="Dark Gray")
            label.place(x=150 - label.winfo_width() / 2, y=190)
            label.update()
            label.place(x=150 - label.winfo_width() / 2, y=190)
        elif 18.50 < BMI < 24.99:
            label.config(text=f"BMI = {BMIstr} / You are normal",
                         font=("Arial", 12, "underline"), fg="Green", bg="Dark Gray")
            label.place(x=150 - label.winfo_width() / 2, y=190)
            label.update()
            label.place(x=150 - label.winfo_width() / 2, y=190)

        elif 25.00 < BMI < 29.99:
            label.config(text=f"BMI = {BMIstr} / You are overweight",
                         font=("Arial", 12, "underline"), fg="#F10909", bg="Dark Gray")
            label.place(x=150 - label.winfo_width() / 2, y=190)
            label.update()
            label.place(x=150 - label.winfo_width() / 2, y=190)
        elif 30.00 < BMI < 34.99:
            label.config(text=f"BMI = {BMIstr} / You are moderately obese",
                         font=("Arial", 12, "underline"), fg="#C00909", bg="Dark Gray")
            label.place(x=150 - label.winfo_width() / 2, y=190)
            label.update()
            label.place(x=150 - label.winfo_width() / 2, y=190)
        elif 35.00 < BMI <= 39.99:
            label.config(text=f"BMI = {BMIstr} / You are severely obese",
                         font=("Arial", 12, "underline"), fg="#640606", bg="Dark Gray")
            label.place(x=150 - label.winfo_width() / 2, y=190)
            label.update()
            label.place(x=150 - label.winfo_width() / 2, y=190)
        elif BMI > 40.00:
            label.config(text=f"BMI = {BMIstr} / You are morbidly obese",
                         font=("Arial", 12, "underline"), fg="Black", bg="Dark Gray")
            label.place(x=150 - label.winfo_width() / 2, y=190)
            label.update()
            label.place(x=150 - label.winfo_width() / 2, y=190)
    else:
        label.config(text="Enter a valid height and weight",
                     font=("Arial", 10), fg="Dark Red", bg="Dark Gray")
        label.place(x=150 - label.winfo_width(), y=190)
        label.update()
        label.place(x=150 - label.winfo_width() / 2, y=190)


label1 = Label(text="Body Mass Index Calculator")
label1.config(font=("Times new roman", 18, "underline"), fg="Black", bg="Dark Gray")
label1.pack()

label3 = Label(text="Enter your height (cm)")
label3.config(font=("Arial", 12, "underline"), fg="Black", bg="Dark Gray")
label3.place(x=150 - 61, y=50)

heightEntry = Entry()
heightEntry.config(width=25)
heightEntry.place(x=150 - 77, y=75)

label2 = Label(text="Enter your weight (kg)")
label2.config(font=("Arial", 12, "underline"), fg="Black", bg="Dark Gray")
label2.place(x=150 - 62.5, y=100)

weightEntry = Entry()
weightEntry.config(width=25)
weightEntry.place(x=150 - 77, y=125)

calculateButton = Button(command=runProgram)
calculateButton.config(text="Calculate")
calculateButton.place(x=150 - 30, y=155)

label = Label()

window.mainloop()
