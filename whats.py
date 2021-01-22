import tkinter as tk
from tkinter import*


root=tk.Tk()
root.geometry("500x520")
root.configure(bg="skyblue")

root.title("Chat APP")
Label(root,text="OPTION",width=10,bd=4,bg="violet",font=('calibre',13,'normal')).pack()
Label(root,text="Application Version 1.0.0",width=25,bd=4,bg="pink",font =('calibre',13,'normal')).pack(side=BOTTOM)

B=StringVar()
H=StringVar()

Entry(root,text=H,width=30,bd=3,font = ('calibre',13,'normal')).place(x=100,y=220)
Entry(root,text=B,width=30,bd=3,font = ('calibre',13,'normal')).place(x=100,y=130)

#user_input=H.get()
def BOT():
 from chatterbot import ChatBot
 from chatterbot.trainers import ListTrainer
 con=[
    "Hello",
    "Hi there!",
    "How are you doing?",
    "I'm doing great.",
    "That is good to hear",
    "Thank you.",
    "You're welcome",
    "what is your name?",
    "virtual human",
    "my name is akash kumar",
    "ok i will rememmber",
    "what is my name?",
    "your name is akash kumar"
    ]
 
 #trainer = ChatterBotCorpusTrainer(chatbot)
 chatbot = ChatBot("Ron Obvious")
 trainer = ListTrainer(chatbot)
 trainer.train(con)


 # The following loop will execute each time the user enters input
   # a=str(input("1).chat\n2).exit\nchoose option : "))
   # if a=="exit":
   #break
    #else:
 user_input=H.get()
 try:
         #user_input = input("Enter something : ")
         #user_input=H.get()
         bot_response = chatbot.get_response(user_input)
         #print(bot_response)
         Label(root,text=bot_response,width=30,bd=3,font = ('calibre',13,'normal'),bg="powderblue").place(x=100,y=130)

         # Press ctrl-c or ctrl-d on the keyboard to exit
         return bot_response
 except (KeyboardInterrupt, EOFError, SystemExit):
        return "error"
#user_input=H.get()
def WEB():
    import web
Button(root,text="DOWNLOAD CODE",width=14,bd=3,bg="green",command=WEB).place(x=180,y=300)
Button(root,text="YOU",width=15,bd=6,bg="cyan",command=BOT).place(x=100,y=170)
Button(root,text="BOOT",width=15,bd=6,bg="cyan",).place(x=100,y=80)

def destroy():
    #conn.close()
    root.destroy()
Button(root,text="EXIT",width=14,bd=3,bg="red",command=destroy).place(x=180,y=270)
root.resizable(0,0)
root.mainloop()
