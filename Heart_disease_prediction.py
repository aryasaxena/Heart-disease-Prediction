# import tkinter
from tkinter import*
#import prediction
from PIL import ImageTk,Image
window = Tk()
window.title("HEART DISEASE PREDICTOR")


l1 = Label(window,text="Heart Disease Prediction System",font=("garamond",15,"bold"))
l1.grid(row=0,column=0)


set_label = Label(window,text="Age",font=("Calibri",12,))
set_label.grid(row=1,column=0)
e1 = Entry()
e1.grid(row=1,column=1)

set_label = Label(window,text="Sex",font=("Calibri",12))
set_label.grid(row=2,column=0)
v1 = StringVar()
e2 = ("Male","Female")
p = OptionMenu(window,v1,*e2)
v1.set("Male")
p.grid(row=2,column=1)

set_label = Label(window,text="Chest Pain Type",font=("Calibri",12,))
set_label.grid(row=3,column=0)
v2 = StringVar()
e3 = ("atypical angima","asympomatic","typical angima","non-anginal pain")
p1 = OptionMenu(window,v2,*e3)
v2.set("typical angima")
p1.grid(row=3,column=1)

set_label = Label(window,text="Resting Blood Pressure",font=("Calibri",12,))
set_label.grid(row=4,column=0)
e4 = Entry()
e4.grid(row=4,column=1)

set_label = Label(window,text="Cholestral",font=("Calibri",12,))
set_label.grid(row=5,column=0)
e5 = Entry()
e5.grid(row=5,column=1)

set_label = Label(window,text="Fasting Blood Sugar",font=("Calibri",12,))
set_label.grid(row=6,column=0)
v6 = StringVar()
e6 = ("greater than 120mg/ml","lower than 120mg/ml")
p6 = OptionMenu(window,v6,*e6)
v6.set("lower than 120mg/ml")
p6.grid(row=6,column=1)


set_label = Label(window,text="Rest_ecg",font=("Calibri",12,))
set_label.grid(row=7,column=0)
v7 = StringVar()
e7 = ("ST.T wave abnormality","normal","left ventricular hypertrophy")
p7 = OptionMenu(window,v7,*e7)
v7.set("normal")
p7.grid(row=7,column=1)

set_label = Label(window,text="Max Heart Rate Achieved",font=("Calibri",12,))
set_label.grid(row=8,column=0)
e8 = Entry()
e8.grid(row=8,column=1)

set_label = Label(window,text="Excercise Induced Angina",font=("Calibri",12,))
set_label.grid(row=9,column=0)
v9 = StringVar()
e9 = ("yes","no")
p9 = OptionMenu(window,v9,*e9)
v9.set("no")
p9.grid(row=9,column=1)

set_label = Label(window,text="St Depression",font=("Calibri",12,))
set_label.grid(row=10,column=0)
e10 = Entry()
e10.grid(row=10,column=1)

set_label = Label(window,text="St_slope",font=("Calibri",12,))
set_label.grid(row=11,column=0)
v11 = StringVar()
e11 = ("downsloping","upsloping","flat")
p11 = OptionMenu(window,v11,*e11)
v11.set("upsloping")
p11.grid(row=11,column=1)

set_label = Label(window,text="Thalassemia",font=("Calibri",12,))
set_label.grid(row=12,column=0)
v12 = StringVar()
e12 = ("normal","reversible defect","fixed defect")
p12 = OptionMenu(window,v12,*e12)
v12.set("fixed defect")
p12.grid(row=12,column=1)

set_label = Label(window,text="num mMjor Vessels",font=("Calibri",12,))
set_label.grid(row=13,column=0)
e13 = Entry()
e13.grid(row=13,column=1)


img = Image.open("heart3.jpg")
render = ImageTk.PhotoImage(img)
l = Label(window,image = render)
l.image=render
l.place(x=450,y=25)



predict_rate = Button(window,text="Predict",font=("garamond",13,"bold"),bg="rosybrown")
predict_rate.grid(row=14,column=1)

#b = [self.e1]

window.geometry('1100x450')
window.mainloop()