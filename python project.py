from tkinter import *
from tkinter import Button
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
class percent:
    def __init__(self,ver):                # constructors function
        self.ver = ver
        self.ver.geometry('1920x1080')         # to create size of gui by geometry
        self.bg = PhotoImage(file="D:\mitaoe.png")          # add bakground image
        self.bg_image = Label(self.ver, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)   # add backgrond  in Label

        Label(self.ver, text = "Roll Number ").place(x = 100 , y = 50 , width = 200 , height = 50)         # To add Line
        global  roll_number                  # function in throughout the program
        roll_number = StringVar()
        Entry(self.ver , bg = 'white',textvariable=roll_number ).place(x=350,y=50,width = 150 , height = 50 )    # taking input from user
        Button(self.ver , text = "VIEW PERFORMANCE" , command = self.view_score).place(x=650 , y= 50 , width =230 , height =50)   # Command from next function
    def view_score(self):         # user define function

        data = pd.read_csv("D:\my creat.csv", index_col=False)        # read csv file in coloumn and rows wise


        data = data.rename(columns={"name ": "Name"})                # renaming colomn with small letter
        data = data.rename(index=lambda x: x + 101)                  # using lambda function to start count from 101
        data["Total"] = data.sum(axis=1)                             # displaying sum of all subject from row
        say = roll_number.get()                                      # input roll no. from user
        k = data.loc[int(say), :]                                    # locating data from given  from  imported csv
        list = []                                                    # empty list
        for i in k:                                                  # for loop in which variable k is located in csv
            list.append(i)                                           # appending marks rollno. wise in the list
        name = list.pop(0)                                           # removing name column from the dataframe using pop
        list.pop(-1)                                                 #
        print(list)                                                  #
        x = ["PHY", "SIC", "EEE", "PP"]                              # list of subject assigned in x
        y = list                                                     # list of marks assigned in y
        plt.style.use("fivethirtyeight")                             # using a graph of one type in barplot named as 538
        plt.bar(x, y, alpha=0.6, width=0.8)                          # dimention of bars
        plt.xlabel(f"Student Name is {name}")                        # labeling x as names of student
        plt.ylabel("Marks")                                          # labeling y as marks
        plt.grid(b=True)                                             # showing gridlines behind bars
        for i in range(4):                                           # for loop
            plt.text(i, y[i], s=y[i], ha="center")                   # ha displaying result in center
        plt.tight_layout()                                           #
        percentge = 0                   # initializing percentage as zero
        for i in range(4):              # for loop and and range 4 for each subject
            percentge += list[i]        # list for each subject and summing all the data
        percentge = percentge / 4       # average of four sub
        if percentge > 75:              # if marks is greater than 75
            grade = "A"                 # printing grade a
        elif percentge > 50:            # if marks is greater than 50
            grade = "B"                 # printing grade b
        elif percentge > 25:            # if marks is greater than 25
            grade = "C"                 # printing grade c
        else:                           # otherwise
            grade = "Fail"              # printing fail

        plt.title(f"Score Card(Percetage = {percentge}% and Grade = {grade})")  # displaying label name as percentage and abstring
        plt.show()                                  # displaying result in form of graph

ver = Tk()                         # call to Tk function (create gui)
obj = percent(ver)                 # call to class function
ver.mainloop()                     # to performe gain and again