#Trivia Game Sample Project by Fred Winters
#10 questions, predetermined order
#Topic - World History
import tkinter as tk #Label wraparound, wraplength=400 (ex), anchor = 'center'(ex)
import os
import sys
global runningscore,stage,questionset,photo
stage = 0
runningscore = 0
chancelevel = 0
count = 0
def initclue(): #Creates the clue window
    global answer,clue,count
    cdisplay = tk.Toplevel() #defines the tkinter toplevel, this actually creates the window
    cdisplay.minsize(400,120) #400x80 defined
    cdisplay.maxsize(400,120)
    cdisplay.title("Clue")
    cmess = tk.Label(cdisplay,text=clue)
    cmess.place(x=0,y=0,width=400,height=40)
    chancestring = "You have: "+str(count)+" chance(s) left"
    cmess2 = tk.Label(cdisplay,text=chancestring)
    cmess2.place(x=0,y=40,width=400,height=40)
    cmessfin = tk.Button(cdisplay,text="Finish",command=lambda: cdisplay.destroy()) #use of lambda is to prevent the function from being immediately called upon initilization.
    cmessfin.place(x=150,y=80,width=100,height=40)
    cdisplay.wm_attributes("-topmost", 1)
    cdisplay.focus_force()
def initdifficulty(): #Creates the clue window
    global answer,clue,chancelevel,count
    def prompt():
        gobal
    def difficultyselect(setting):
        global chancelevel, count
        if setting == 'Easy':
            chancelevel = "Easy"
            count = 3
        elif setting == 'Medium':
            chancelevel = "Medium"
            count = 2
        elif setting == 'Hard':
            chancelevel = "Hard"
            count = 1
        ddisplay.destroy()
        importinginit()
    ddisplay = tk.Toplevel() #defines the tkinter toplevel, this actually creates the window
    ddisplay.minsize(360,300) #400x80 defined
    ddisplay.maxsize(400,200)
    ddisplay.title("Difficulty select")
    dmess = tk.Label(ddisplay,text="This game offers three difficulty settings, Easy, Medium, and Hard. Easy gives you three chances per question, Medium two chances and Hard only one chance per quesiton. Please make your choice by clicking the corresponding button",wraplength=360)
    dmess.place(x=0,y=0,width=360,height=200)
    dmessfin = tk.Button(ddisplay,text="Easy",command=lambda: difficultyselect("Easy")) #use of lambda is to prevent the function from being immediately called upon initilization.
    dmessfin.place(x=0,y=200,width=120,height=40)
    dmessfin = tk.Button(ddisplay,text="Medium",command=lambda: difficultyselect("Medium")) #use of lambda is to prevent the function from being immediately called upon initilization.
    dmessfin.place(x=120,y=200,width=120,height=40)
    dmessfin = tk.Button(ddisplay,text="Hard",command=lambda: difficultyselect("Hard")) #use of lambda is to prevent the function from being immediately called upon initilization.
    dmessfin.place(x=240,y=200,width=120,height=40)
    ddisplay.wm_attributes("-topmost", 1)
    ddisplay.focus_force()
def importinginit():
    global idisplay
    idisplay = tk.Toplevel()
    idisplay.minsize(400,200)
    idisplay.maxsize(400,200)
    idisplay.title("Trivia File Importing")
    imess = tk.Label(idisplay,text="Please enter the name of the file to import, with extension.")
    imess.place(x=0,y=0,width=400,height=50)
    imessentry = tk.Entry(idisplay)
    imessentry.place(x=0,y=50,width=400,height=40)
    imessfin = tk.Button(idisplay,text="Finish",command=lambda: importingfile(imessentry.get()))
    imessfin.place(x=150,y=150,width=100,height=50)
    potentialimports1 = os.listdir(".")
    finallist = []
    for a in potentialimports1:
        if a.endswith(".txt"):
            finallist.append(a)
    displaystringlist = "Potential imports: "
    for b in finallist:
        displaystringlist = displaystringlist + str(b)+","
    guipotential = tk.Message(idisplay,text=displaystringlist,width=400)
    guipotential.place(x=0,y=100,width=400,height=50)
    idisplay.wm_attributes("-topmost", 1)
    idisplay.focus_force()
def importingfile(namefile):
    global questionset, idisplay,questionset,answer,clue
    choice1 = namefile
    f = open(choice1,'r',encoding='UTF-8') #use of UTF-8 encoding to ensure that the file can be sucessfully opened regardless of operating system.
    questionset = f.read()
    questionset = questionset.split("\n")
    idisplay.destroy()
    window.wm_attributes("-topmost", 1) #topmost and focus_force() are used to call user attention to the display window rather than having it be buried by the main display window.
    window.focus_force()
    maindisplay.configure(text=questionset[stage])
    answerdisplay.configure(text=questionset[(stage+1)])
    answerdisplay2.configure(text=questionset[(stage+2)])
    answerdisplay3.configure(text=questionset[(stage+3)])
    answerdisplay4.configure(text=questionset[(stage+4)])
    clue=questionset[stage+5]
    answer = questionset[stage+6]
def questions(givenanswer):
    global answer,display,runningscore,count
    while count > 0:
        if givenanswer == answer: #if the correct answer is given,
            display2 = "Correct!"
            if count >= 2: #with both chances left, two points are given
                runningscore = runningscore + 2
                count = 0
            elif count == 1: #if only one chance is left, one point is given.
                runningscore = runningscore + 1
                count = 0
        else: #if the incorrect answer is given, subtract one chance and informs the user that they are incorrect.
            display2 = "Incorrect."
            count = count - 1
            if count == 1 or count == 2:
                initclue()
        break
    if count == 0:
        display = tk.Toplevel()
        display.minsize(350,80)
        display.maxsize(350,80)
        display.title("Answer:")
        msg1str = "The answer was: "+str(answer)
        msg1 = tk.Label(display,text=msg1str)
        msg1.grid(row=0,column=0,columnspan=4,sticky='N')
        msg2str = tk.Label(display,text=display2)
        msg2str.grid(row=1,column=0,columnspan=4,sticky='N')
        prompt1 = tk.Button(display,text="Finish",command=lambda: main1())
        prompt1.grid(row=2,column=0,columnspan=4,sticky='N')
        display.wm_attributes("-topmost", 1)
        display.focus_force()
        for N in range(0,3):
            display.columnconfigure(N,weight=1)
            display.rowconfigure(N,weight=1)
def main1():
    global questionset, stage, answer, display,runningscore,count,chancelevel
    if chancelevel == 'Easy':
        count = 3
    elif chancelevel == 'Medium':
        count = 2
    elif chancelevel == 'Hard':
        count = 1
    display.destroy() #destroys the answer window.
    stage = stage + 7 #shifting of "stage" in increments of 7, to jump to the next set.
    if stage < 70:
        maindisplay.configure(text=questionset[stage])
        answerdisplay.configure(text=questionset[(stage+1)])
        answerdisplay2.configure(text=questionset[(stage+2)])
        answerdisplay3.configure(text=questionset[(stage+3)])
        answerdisplay4.configure(text=questionset[(stage+4)])
        clue = questionset[stage+5]
        answer = questionset[stage+6]
    elif stage == 70: #if 10 games are finished(7 stages per game), terminates the game and displays a game over display.
        maindisplay.configure(text="Game finished.")
        edisplay = tk.Toplevel()
        edisplay.minsize(350,125)
        edisplay.maxsize(350,125)
        edisplay.title("Game Completed")
        endmessage = tk.Label(edisplay,text="Thank you for playing.")
        endmessage2 = tk.Label(edisplay,text="Final score:")
        endmessage3 = tk.Label(edisplay,text=runningscore)
        if runningscore > 15: #grading levels, from A to D
            gradelevel = "Grade: A-Good Job!"
        elif runningscore > 10 and runningscore < 16:
            gradelevel = "Grade: B-Good work."
        elif runningscore > 5 and runningscore < 11:
            gradelevel = "Grade: C-Some room for improvement.."
        elif runningscore < 6 and runningscore != 0:
            gradelevel = "Grade: D-???"
        elif runningscore == 0:
            gradelevel = "Grade: F-You failed completely."
        endfinal = tk.Label(edisplay,text=gradelevel)
        endbutton = tk.Button(edisplay,text="End",command=window.destroy)
        endmessage.place(x=0,y=0,width=350,height=25)
        endmessage2.place(x=0,y=25,width=350,height=25)
        endmessage3.place(x=0,y=50,width=350,height=25)
        endbutton.place(x=150,y=100,width=50,height=25)
        endfinal.place(x=0,y=75,width=350,height=25)
        edisplay.wm_attributes("-topmost", 1)
        edisplay.focus_force()
window = tk.Tk() #creates main tkinter window
window.wm_title("History Trivia: By Fred Winters") #sets title
window.minsize(width=450,height=1000) #450x1000 size
window.maxsize(width=450,height=1000)
maindisplay = tk.Label(window,text="Question Display",width=400,font=("Courier", 20),wraplength=450)
maindisplay.place(x=0,y=0,width=450,height=100)
answerdisplay = tk.Label(window,text="Answer Display",width=700,font=("Courier", 20),wraplength=450)
answerdisplay.place(x=0,y=100,width=450,height=100)
answerdisplay2 = tk.Label(window,text="Answer Display",width=700,font=("Courier", 20),wraplength=450)
answerdisplay2.place(x=0,y=200,width=450,height=100)
answerdisplay3 = tk.Label(window,text="Answer Display",width=700,font=("Courier", 20),wraplength=450)
answerdisplay3.place(x=0,y=300,width=450,height=100)
answerdisplay4 = tk.Label(window,text="Answer Display",width=700,font=("Courier", 20),wraplength=450)
answerdisplay4.place(x=0,y=400,width=450,height=100)
photoA = tk.PhotoImage(file="ButtonA.gif") #use of photos via tkinter, defined via tk.PhotoImage.
photoB = tk.PhotoImage(file="ButtonB.gif")
photoC = tk.PhotoImage(file="ButtonC.gif")
photoD = tk.PhotoImage(file="ButtonD.gif")
button1 = tk.Button(window,text="A",width=400,command=lambda: questions("A"),image=photoA) #lambda is used here to prevent the function from being called automatically upon creation of the button.
button1.place(x=0,y=600,width=450,height=100) #use of place
button2 = tk.Button(window,text="B",width=400,command=lambda: questions("B"),image=photoB)
button2.place(x=0,y=700,width=450,height=100)
button3 = tk.Button(window,text="C",width=400,command=lambda: questions("C"),image=photoC)
button3.place(x=0,y=800,width=450,height=100)
button4 = tk.Button(window,text="D",width=400,command=lambda: questions("D"),image=photoD)
button4.place(x=0,y=900,width=450,height=100)
initdifficulty()
window.mainloop() #tkinter mainloop
