"""
+---------------------------------------------------------------------+
|     Created on Fri Nov  6 16:29:47 2020                             |
|     @author     :   AKASH KUMAR                                     |
|     @college    :   MIT Institute Moradabad                         |
|     @branch     :   Computer Science & Information Technology       |
|     @work as    :   Software Development & Machine Learning.        |
|     @website.   :   https://medium.com/@akashsaininasa.             |
+---------------------------------------------------------------------+
"""

#-------------------------------------------------------
from tkinter import*
import tkinter as tk
import mysql.connector
from mysql.connector import Error
#-----------------------------------------------------
root=tk.Tk()
root.geometry("600x490")
root.configure(bg="deep pink")
root.title(".......CORONA VIRUS TEST APP......")
# relief="solid"
Label(root,text="Covid-19 Test",font=('Helvetica', 10, 'bold'), bg="purple",fg='white',bd=1, relief="solid",width=71,height=1).place(x=13,y=10)
#Label(root,text="Application Version 2.7.1",width=25,bg="pink").pack(side=BOTTOM)
Label(root,text="ENTER YOUR NAME",font=('Helvetica',10,'bold'),bg='orange',fg='blue',bd=1, relief="solid",width=35,height=2).place(x=10,y=40)
#Label(root,text="BODY TEMP.", width=15,bg="powderblue").place(x=100,y=120)
Label(root,text="ENTER BODY TEMP.(in Cel.)",font=('Helvetica',10,'bold'),bg='orange',fg='blue',bd=1, relief="solid",width=35,height=2).place(x=10,y=80)
#Label(root,text="AGE", width=15,bg="powderblue").place(x=100,y=180)
Label(root,text="ENTER YOUR AGE",font=('Helvetica',10,'bold'),bg='orange',fg='blue',bd=1, relief="solid",width=35,height=2).place(x=10,y=120)
#Label(root,text="GENDER", width=15,bg="powderblue").place(x=100,y=240)
Label(root,text="ENTER GENDER(male/female/others)",font=('Helvetica',10,'bold'),bg='orange',fg='blue',bd=1, relief="solid",width=35,height=2).place(x=10,y=160)
#Label(root,text="BREATHING PROB.", width=15,bg="powderblue").place(x=100,y=300)
Label(root,text="HAHE BREATHING POBLEM?(yes/no)",font=('Helvetica',10,'bold'),bg='orange',fg='blue',bd=1, relief="solid",width=35,height=2).place(x=10,y=200)
#Label(root,text="NOSE PROB.", width=15,bg="powderblue").place(x=100,y=360)
Label(root,text="HAVE NOSE PROBLEM?(yes/no)",font=('Helvetica',10,'bold'),bg='orange',fg='blue',bd=1, relief="solid",width=35,height=2).place(x=10,y=240)
#Label(root,text="BODY PAIN PROB.", width=15,bg="powderblue").place(x=100,y=420)
Label(root,text="HAVE BODY PAIN?(yes/no)",font=('Helvetica',10,'bold'),bg='orange',fg='blue',bd=1, relief="solid",width=35,height=2).place(x=10,y=280)
#Label(root,text="CORONA REPORT", width=15,bg="powderblue").place(x=100,y=480)
Label(root,text="CORONA TEST REPORT",font=('Helvetica',10,'bold'),bg='orange',fg='blue',bd=1, relief="solid",width=35,height=2).place(x=10,y=320)
#-------------------------------------------------------------------------------------------------------------------
BT=DoubleVar()
AGE=DoubleVar()
GEN=StringVar()
BP=StringVar()
RN=StringVar()
BODYP=StringVar()
#------------------------------------------------------------------------------------------------------------
NAM=StringVar()
p,q,r,s,t,u,v,w=0,0,0,0,0,0,0,0
#-----------------------------------------------------------------------------------------------------------
t=Entry(root,text=NAM,width=45, bg="cyan2",bd=2)
t.place(x=310, y=40,height=35)
t1=Entry(root,text=BT,width=45, bg="cyan2",bd=2)
t1.place(x=310, y=80,height=35)
t2=Entry(root,text=AGE,width=45, bg="cyan2",bd=2)
t2.place(x=310, y=120,height=35)
t3=Entry(root,text=GEN,width=45, bg="cyan2",bd=2)
t3.place(x=310, y=160,height=35)
t4=Entry(root,text=BP,width=45, bg="cyan2",bd=2)
t4.place(x=310, y=200,height=35)
t5=Entry(root,text=RN,width=45, bg="cyan2",bd=2)
t5.place(x=310, y=240,height=35)
t6=Entry(root,text=BODYP,width=45, bg="cyan2",bd=2)
t6.place(x=310, y=280,height=35)
t7=Entry(root,width=45, bg="cyan2",bd=2)
t7.place(x=310, y=320,height=35)
#----------------------------------------------------------------------------------------------------------
def info():
   n=tk.Tk()
   n.geometry("620x500")
   n.configure(bg="blue")
   
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
   
   n.resizable(0,0)
   n.mainloop()
#-------------------------------------------------------------------------------------------------------------
Button(root,text="ABOUT",font=('Helvetica',10,'bold'),bg="purple",fg='white',
       width=22,height=2,bd=4, command=info).place(x=10, y=380)
def destroy():
    root.destroy()
Button(root,text="EXIT",font=('Helvetica',10,'bold'),bg="red",fg='white',
       width=22,height=2,bd=4, command=destroy).place(x=202, y=380)
#-------------------------------------------------------------------------------
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
     H=NAM.get()
     a=BT.get()
     b=AGE.get()
     C=GEN.get()
     if C=="male" or "Male" or "MALE" or "Others" or "others" or "OTHERS":
         c=1
     else:
         c=0
     D=BP.get()
     if D=="yes" or "YES" or "Yes":
         d=1
     else:
         d=0
     E=RN.get()
     if E=="yes" or "YES" or "Yes":
         e=1
     else:
         e=0
     F=BODYP.get()
     if F=="yes" or "YES" or "Yes":
         f=1
     else:
         f=0
    
     if a>0 and b>0 and c==1 and d==1 and e==1 and f==1:
      x_test=[a,b,c,d,e,f]
      y_predict=model.predict([x_test,])
      ref={1:"TEST IS POSITIVE", 0:"TEST IS NEGATIVE"}
      if(y_predict[0]==0):
        Label(root,text=str(ref[y_predict[0]]),width=39,height=2,bg="green",fg='blue',bd=4).place(x=310,y=320)
      else:
        Label(root,text=str(ref[y_predict[0]]),width=39,height=2,bg="red",fg='blue',bd=4).place(x=310,y=320)
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
        rp=Tk()
        rp.geometry("500x450")
        rp.configure(bg="blue")
        Label(rp,text="MIT LICENCE",width=25,bg="lightgreen").pack(side=BOTTOM)
        rp.title(".......COVID 19 TEST REPORT ......")
        Label(rp,text="TEST REPORT",width=25,bg="violet").pack(side=TOP)
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
        #-----------------------------------------------------------------------------
        def destroy1():
         rp.destroy()
        Button(rp,text="EXIT",width=8,bg="powderblue",command=destroy1).place(x=300,y=300)
        Button(rp,text="PRINT",width=8,bg="powderblue").place(x=140,y=300)
        rp.resizable(0,0)
        #----------------------------------------------------------------
      else:
       def report():
        rp=Tk()
        rp.geometry("500x450")
        rp.configure(bg="blue")
        #------------------------------------------------------------------------------
        Label(rp,text="MIT LICENCE",width=25,bg="lightgreen").pack(side=BOTTOM)
        rp.title(".......COVID 19 TEST REPORT ......")
        Label(rp,text="TEST REPORT",width=25,bg="violet").pack()
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
        #--------------------------------------------------------------------------------
        def destroy1():
           rp.destroy()
        #---------------------------------------------------------------------------------
        Button(rp,text="EXIT",width=8,bg="powderblue",command=destroy1).place(x=300,y=300)
        Button(rp,text="PRINT",width=8,bg="powderblue").place(x=140,y=300)
        rp.resizable(0,0)
        rp.mainloop()
      Button(root,text="TEST REPORT",font=('Helvetica',10,'bold'),bg="blue",fg='white',
       width=22,height=2,bd=4,command=report).place(x=395, y=430)
      #------------------------------------------------------------------------------------
     else:
         Label(root,text='TEST FAILED',width=39,height=2,bg="red",fg='blue',bd=4).place(x=310,y=320)
         #Label(root,text="TEST FAILED",width=13,bg="powderblue").place(x=300,y=480)
         speak.Speak("invalid input")
         speak.Speak("Please try again")
    #------------------------------------------------------------------------------------
    except:
        Label(root,text='TEST FAILED',width=39,height=2,bg="red",fg='blue',bd=4).place(x=310,y=320)
        # Label(root,text="TEST FAILED",width=13,bg="powderblue").place(x=300,y=480)
        speak.Speak("invalid input")
        speak.Speak("Please try again")
    #-------------------------------------------------------------------------------------
Button(root,text="START TEST",font=('Helvetica',10,'bold'),bg="green",fg='white',
       width=22,height=2,bd=4, command=Model).place(x=395, y=380)
#------------------------------------------------------------------------------------------------------
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

Button(root,text="ASSISTANT",font=('Helvetica',10,'bold'),bg="SeaGreen",fg='white',
       width=22,height=2,bd=4,command=AI).place(x=10, y=430)    
#----------------------------------------------------------------------------------------------------   
def Clear():
     Label(root,text="",width=39,height=2,bg="cyan2",bd=0.0000003).place(x=310,y=320)

Button(root,text="CLEAR",font=('Helvetica',10,'bold'),bg="orange",fg='white',
       width=22,height=2,bd=4, command=Clear).place(x=202, y=430)
#-------------------------------------------------------------------------------------------------
Button(root,text="TEST REPORT",font=('Helvetica',10,'bold'),bg="blue",fg='white',
       width=22,height=2,bd=4).place(x=395, y=430)

root.resizable(0,0)
root.mainloop()
#-------------------------------------------------------------------------------------------------

'''     ------------- Thanks For Using It -------------        '''
