# -*- coding: utf-8 -*-
""" project name : covid-19 test application """
"""
Created on Fri Jun 6 16:29:47 2020

@author.    : AKASH KUMAR
@institute. : MIT Institute Moradabad india
@branch.    : Computer Science & Information Technology
@work as.   : Software Devlope & Machine Learning Engineer
@website.   : https://medium.com/@akashsaininasa
@github.    : https://github.com/Akash671

"""


import tkinter as tk
from tkinter import*
import mysql.connector
from mysql.connector import Error




root=tk.Tk()
root.geometry("500x620")
root.configure(bg="skyblue")


root.title(".......CORONA VIRUS TEST APP......")

Label(root,text="Covid-19 Test",width=25,bg="powderblue").pack()


Label(root,text="Application Version 2.7.1",width=25,bg="pink").pack(side=BOTTOM)
Label(root,text="YOUR NAME", width=15,bg="powderblue").place(x=100,y=60)
Label(root,text="BODY TEMP.", width=15,bg="powderblue").place(x=100,y=120)
Label(root,text="AGE", width=15,bg="powderblue").place(x=100,y=180)
Label(root,text="GENDER", width=15,bg="powderblue").place(x=100,y=240)
Label(root,text="BREATHING PROB.", width=15,bg="powderblue").place(x=100,y=300)
Label(root,text="NOSE PROB.", width=15,bg="powderblue").place(x=100,y=360)
Label(root,text="BODY PAIN PROB.", width=15,bg="powderblue").place(x=100,y=420)
Label(root,text="CORONA REPORT", width=15,bg="powderblue").place(x=100,y=480)
#Label(root,text="number", width=15,bg="powderblue").place(x=100,y=530)
'''Label(root,text="number", width=15,bg="powderblue").place(x=100,y=1020)
Label(root,text="number", width=15,bg="powderblue").place(x=100,y=1120)
Label(root,text="number", width=15,bg="powderblue").place(x=100,y=1220)
Label(root,text="number", width=15,bg="powderblue").place(x=100,y=1320)
Label(root,text="number", width=15,bg="powderblue").place(x=100,y=1420)
Label(root,text="number", width=15,bg="powderblue").place(x=100,y=1520)
Label(root,text="number", width=15,bg="powderblue").place(x=100,y=1620)'''



BT=DoubleVar()
AGE=DoubleVar()
GEN=StringVar()
BP=StringVar()
RN=StringVar()
BODYP=StringVar()
'''
BT=StringVar()
AGE=StringVar()
GEN=StringVar()
BP=StringVar()
RN=StringVar()
BODYP=StringVar()
'''
g=StringVar()
h=StringVar()

p,q,r,s,t,u,v,w=0,0,0,0,0,0,0,0

Entry(root,text=h, width=15).place(x=300,y=60)
Entry(root,text=BT,width=15).place(x=300,y=120)
Entry(root,text=AGE, width=15).place(x=300,y=180)
Entry(root,text=GEN,width=15).place(x=300,y=240)
Entry(root,text=BP, width=15).place(x=300,y=300)
Entry(root,text=RN, width=15).place(x=300,y=360)
Entry(root,text=BODYP, width=15).place(x=300,y=420)

Entry(root,text=g, width=15).place(x=300,y=480)


def info():
   n=tk.Tk()
   n.geometry("620x500")
   n.configure(bg="blue")
  # n.configure(background="grey")
   
   n.title("INFORMATION WHAT CONTAIN IS THIS GUI")
   Label(n,text="Supporetd By MIT Moradabad",width=30,bg="violet").pack(side=BOTTOM)
   Label(n,text="Information About Application",bg="powderblue",
          font=('Helvetica',20,'bold')).pack()
   data='''HELLO GUYS THIS APPLIACTION DEVLOPED BY AKASH KUMAR IN 6 NOV.
           2020 AND IT IS
           OUR ML BASED PROJECT FOR CHECKING CORONA VIRUS ,BY WHICH I AM
           MAKING A MODEL ,BY THIS MODEL,I HAVE TAKEN A SMALL DATA WHICH
           IS PREPARED BY LOCAL DOCTOR, WITH THE HELP OF THAT DATA ,MY   
           MACHINE PERFORMED A PREDICTIVE ANALYSIS WHEATHER THE PATIENT 
           IS SUFFERING FROM CORONA OR NOT.
           IN MY THIS GUI I HAVE PROVIDED THREE BUTTONS ON FIRST WINDOW:
                  1. ABOUT
                  2. TEST
                  3. EXIT
                  4. ASSISTANT
                  5. TEST REPORT
           THE FIRST BUTTON IS RESPONSIBLE FOR ALL INFO ABOUT GUI WHICH 
           IS U READ ON THIS PAGE OF THE SECOND WINDOW OF THIS GUI.THE 
           TEST BUTTON IS RESPONSIBLE FOR PREDICTIVE ANALYSIS WHEATHER
           THE PATIENT IS SUFFERING FROM CORONA VIRUS OR NOT.IN WHICH 
           THE USER HAS TO GIVEN SOME INPUT LIKE; BODYTEMPERATURE,AGE,
           GENDER,BREATHINGPROB,RUNNING NOSE,BODYPAIN.THE THIRD BUTTON
           IS FOR EXIT OR TERMINATE3 OUR GUI.AND ONE MORE THING WHENEVER
           ANY PATIENT IS WANT TO CHECK THEIR TEST,THE WHOLE INFORMATION
           IS ALSO GET STORED IN BACKENED THROUGH XAMPP SERVER by SQL QUERY.
           PLZ GUYS GIVE  A VALUABLE FEEDBACK WHEATHER IS LITTLE BIT SIMPLE 
           APPROACH FOR ANYONE WHO WANT TO PERFORM THE TEST,SUGGESTIONS ARE
           WELCOME .THANK YOU'''
   Label(n,text=data,relief="solid",font=("Helvetica",10),bg="light blue").pack()
   #Button(n,text="BACK",relief="solid",
       #command=root,font=("bold",18)).place(x=250,y=430)
   
   n.resizable(0,0)
   n.mainloop()
#       Button(root,text="INFORMATION",relief="solid",
#       command=info,font=("bold",18)).place(x=30,y=100)

   
Button(root,text="ABOUT",width=8,bg="powderblue",command=info).place(x=86,y=530)



def destroy():
    #conn.close()
    root.destroy()


Button(root,text="EXIT",width=8,bg="powderblue",command=destroy).place(x=337,y=530)
 

def Model():
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    import seaborn as sns
    import win32com.client as wincl
    #import time
    speak = wincl.Dispatch("SAPI.SpVoice")
    mydb=mysql.connector.connect(host='localhost',
                            user='root',
                            password='',
                            database='covid_19')
    mycursor=mydb.cursor()


    data=pd.read_excel(r"D:\vs\ML\data_corna.xlsx")
    data=data.drop(["Government Id"],axis=1)
    data["Body_temp"].fillna(data["Body_temp"].median(),inplace=True)
    data["Age"].fillna(data["Age"].median(),inplace=True)
    
    
    from sklearn.preprocessing import LabelEncoder
    le=LabelEncoder()
    data["Gender"]=le.fit_transform(data["Gender"])
    data["Infection_propb"]=le.fit_transform(data["Infection_propb"])
    
    
    Y=data["Infection_propb"]
    X=data.drop(["Infection_propb"],axis=1)
    from sklearn.linear_model import LogisticRegression
    model=LogisticRegression()
    
    model.fit(X,Y)
    try:
     H=h.get()
     a=BT.get()
     b=AGE.get()
     C=GEN.get()
     if C=="male":
         c=0
     else:
         c=1
     D=BP.get()
     if D=="yes":
         d=1
     else:
         d=0
     E=RN.get()
     if E=="yes":
         e=1
     else:
         e=0
     F=BODYP.get()
     if F=="yes":
         f=1
     else:
         f=0
    
     if a>=0 and b>0 and c>=0 and d>=0 and e>=0 and f>=0:
      #x_test=[BT.get(),AGE.get(),
      #        GEN.get(),BP.get(),RN.get(),BODYP.get()]
      x_test=[a,b,c,d,e,f]
      y_predict=model.predict([x_test,])
      ref={1:"TEST IS POSITIVE", 0:"TEST IS NEGATIVE"}
      Label(root,text=str(ref[y_predict[0]]),width=13,bg="powderblue").place(x=300,y=480)
      text=str(ref[y_predict[0]])
      speak.Speak("Your covid 19")
      speak.Speak(text)
      sql="INSERT INTO corona_patient_data_2020(Patient_Name,Body_Temp,Age,Gender,Breath_Prob,Nose_Prob,Body_Pain,Test_Report) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"
      val=(H,a,b,C,D,E,F,text)
      mycursor.execute(sql,val)
      mydb.commit()
      p,q,r,s,t,u,v,w=H,a,b,C,D,E,F,text
      if y_predict[0]==0:   
       def report():
        rp=tk.Tk()
        rp.geometry("500x520")
        rp.configure(bg="blue")
        Label(rp,text="MIT LICENCE",width=25,bg="lightgreen").pack(side=BOTTOM)


        rp.title(".......COVID 19 TEST REPORT ......")
        Label(rp,text="TEST REPORT",width=25,bg="violet").pack()
        #Label(root,text="application version 2.7.1",width=25,bg="powderblue").pack(side=BOTTOM)
        Label(rp,text="YOUR NAME", width=15,bg="powderblue").place(x=120,y=60)
        Label(rp,text="BODY TEMP.", width=15,bg="powderblue").place(x=120,y=90)
        Label(rp,text="AGE", width=15,bg="powderblue").place(x=120,y=120)
        Label(rp,text="GENDER", width=15,bg="powderblue").place(x=120,y=150)
        Label(rp,text="BREATHING PROB.", width=15,bg="powderblue").place(x=120,y=180)
        Label(rp,text="NOSE PROB.", width=15,bg="powderblue").place(x=120,y=210)
        Label(rp,text="BODY PAIN PROB.", width=15,bg="powderblue").place(x=120,y=240)
        Label(rp,text="CORONA REPORT", width=15,bg="powderblue").place(x=120,y=270)
    
        Label(rp,text=p, width=15,bg="powderblue").place(x=280,y=60)
        Label(rp,text=q, width=15,bg="powderblue").place(x=280,y=90)
        Label(rp,text=r, width=15,bg="powderblue").place(x=280,y=120)
        Label(rp,text=s, width=15,bg="powderblue").place(x=280,y=150)
        Label(rp,text=t, width=15,bg="powderblue").place(x=280,y=180)
        Label(rp,text=u, width=15,bg="powderblue").place(x=280,y=210)
        Label(rp,text=v, width=15,bg="powderblue").place(x=280,y=240)
        Label(rp,text=w, width=15,bg="lightgreen").place(x=280,y=270)
    
    
        def destroy1():
         #conn.close()
         rp.destroy()
        #def Print():
            
        Button(rp,text="EXIT",width=8,bg="powderblue",command=destroy1).place(x=300,y=300)
        Button(rp,text="PRINT",width=8,bg="powderblue").place(x=140,y=300)
        rp.resizable(0,0)
        rp.mainloop()
      else:
       def report():
        rp=tk.Tk()
        rp.geometry("500x520")
        rp.configure(bg="blue")
        Label(rp,text="MIT LICENCE",width=25,bg="lightgreen").pack(side=BOTTOM)



        rp.title(".......COVID 19 TEST REPORT ......")
        Label(rp,text="TEST REPORT",width=25,bg="violet").pack()
        #Label(root,text="application version 2.7.1",width=25,bg="powderblue").pack(side=BOTTOM)
        Label(rp,text="YOUR NAME", width=15,bg="powderblue").place(x=120,y=60)
        Label(rp,text="BODY TEMP.", width=15,bg="powderblue").place(x=120,y=90)
        Label(rp,text="AGE", width=15,bg="powderblue").place(x=120,y=120)
        Label(rp,text="GENDER", width=15,bg="powderblue").place(x=120,y=150)
        Label(rp,text="BREATHING PROB.", width=15,bg="powderblue").place(x=120,y=180)
        Label(rp,text="NOSE PROB.", width=15,bg="powderblue").place(x=120,y=210)
        Label(rp,text="BODY PAIN PROB.", width=15,bg="powderblue").place(x=120,y=240)
        Label(rp,text="CORONA REPORT", width=15,bg="powderblue").place(x=120,y=270)
    
        Label(rp,text=p, width=15,bg="powderblue").place(x=280,y=60)
        Label(rp,text=q, width=15,bg="powderblue").place(x=280,y=90)
        Label(rp,text=r, width=15,bg="powderblue").place(x=280,y=120)
        Label(rp,text=s, width=15,bg="powderblue").place(x=280,y=150)
        Label(rp,text=t, width=15,bg="powderblue").place(x=280,y=180)
        Label(rp,text=u, width=15,bg="powderblue").place(x=280,y=210)
        Label(rp,text=v, width=15,bg="powderblue").place(x=280,y=240)
        Label(rp,text=w, width=15,bg="red").place(x=280,y=270)
    
    
        def destroy1():
         #conn.close()
         rp.destroy()
        #def Print():
            
        Button(rp,text="EXIT",width=8,bg="powderblue",command=destroy1).place(x=300,y=300)
        Button(rp,text="PRINT",width=8,bg="powderblue").place(x=140,y=300)
        rp.resizable(0,0)
        rp.mainloop()

      Button(root,text="TEST REPORT",width=12,bg="powderblue",command=report).place(x=220,y=560)  

      #Button(root,text="TEST REPORT",width=12,bg="powderblue",command=report).place(x=220,y=560)  

     # if y_pred[0]==1:
     #   speak.Speak("Your Covid 19 test is positive")
        #text="Welcome in digital \ncovid 19 test app"
        #speak.Speak(str(ref[y_predict]))
     # else:
      #    speak.Speak("your covid 19 test is negative")
     else:
         Label(root,text="TEST FAILED",width=13,bg="powderblue").place(x=300,y=480)
         # Label(root,text="TEST FAILED",width=13,bg="powderblue").place(x=300,y=450)
         speak.Speak("invalid input")
         speak.Speak("Please try again")
    except:
        Label(root,text="TEST FAILED",width=13,bg="powderblue").place(x=300,y=480)
        speak.Speak("invalid input")
        speak.Speak("Please try again")
    


Button(root,text="TEST",width=8,bg="powderblue",command=Model).place(x=270,y=530)

def AI():
    import win32com.client as wincl
    import time
    speak = wincl.Dispatch("SAPI.SpVoice")
    text="Welcome in digital \ncovid 19 test app"
    speak.Speak(text)
    
    text="Follow these instruction to start covid 19 test "
    speak.Speak(text)
    
    text="First Instruction"
    speak.Speak(text)
    text="Read all data entrys carefully"
    speak.Speak(text)
    text="Secound Instruction"
    speak.Speak(text)
    text="Fill all data entres based on your medical report"
    speak.Speak(text)
    text="Third Instruction"
    speak.Speak(text)
    text="Click On Test Button"
    speak.Speak(text)
    speak.Speak("After sometime you will see your your covid 19 test report on corona test screen")
    speak.Speak("Thanks For Using AI ASSISTANT")
    
    
    
    
    
Button(root,text="ASSISTANT",width=8,bg="powderblue",command=AI).place(x=153,y=530)

#def Clear():
    
def Clear():
     Label(root,text=" "*30,width=13,bg="powderblue").place(x=300,y=480)
     
Button(root,text="CLEAR",width=6,bg="powderblue",command=Clear).place(x=220,y=530)

Button(root,text="TEST REPORT",width=12,bg="powderblue").place(x=220,y=560)  

# 
#Entry(root,text=h, width=15).place(x=300,y=530)

#Entry(root,text=a,width=15).place(x=300,y=60)



root.resizable(0,0)
root.mainloop()


'''     ------------- Thanks For It -------------        '''
