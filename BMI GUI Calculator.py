from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
root = Tk()
root.title('BMI Calculator')
root.geometry('514x496')
image = Image.open("bmi.jpg")
photo = ImageTk.PhotoImage(image)
Label(image=photo).pack()

def bmi_calculate():
    height = float(h.get())
    weight = float(w.get())
    height=height/3.281
    calculate = round(weight/height**2)
    if calculate < 18.5 :
        Label(root, text = f"BMI is {calculate}, Underweight",font = ("Times", "16", "bold"), width = 30).place(x = 60, y= 370)
    elif (calculate > 18.5) and (calculate < 25):
        Label(root, text = f"BMI is {calculate}, Normal",font = ("Times", "14", "bold"), width = 30).place(x = 60, y= 370)
    elif (calculate > 25) and (calculate < 30):
        Label(root, text = f"BMI is {calculate}, Slightly overweight",font = ("Times", "14", "bold"), width = 30).place(x = 60, y= 370)
    elif (calculate > 30):
        Label(root, text = f"BMI is {calculate}, Obesity Class 1",font = ("Times", "14", "bold"), width = 30).place(x = 60, y= 370)
    else:
        Label(root, text = f"BMI is {calculate}, Obesity Class 2",font = ("Times", "14", "bold"), width = 30).place(x = 60, y= 370)
h = StringVar()
w = StringVar()

Label(root, text = "BMI CALCULATOR", font = ("Times", "28", "bold"), width=18).place(x = 60,y=25)
Label(root, text = "Enter Your Height in feet", font = ("Times", "20", "bold"),width = 25).place(x = 60,y=115)
Entry(root, textvariable = h, font = ("Times", "16", "bold"), width = 6 ).place(x = 225, y = 160)

Label(root, text = "Enter Your Weight in kg", font = ("Times", "20", "bold"), width=25).place(x = 60,y=220)
Entry(root, textvariable = w, font = ("Times", "16", "bold"), width = 6 ).place(x = 225, y = 267)

Button(root, text = "Calculate", command = bmi_calculate, font = ("Times", "16", "bold")).place(x = 210, y=320)
root.mainloop()