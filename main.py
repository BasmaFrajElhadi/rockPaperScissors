from tkinter import *
from PIL import Image,ImageTk
from random import choice

myFrame = Tk()

myFrame.title("Rock Paper Scissors")
myFrame.configure(background= "SteelBlue1")

# pictures
rockImage = ImageTk.PhotoImage(Image.open("imgs/rockUser.png"))
paperImage = ImageTk.PhotoImage(Image.open("imgs/paperUser.png"))
scissorsImage = ImageTk.PhotoImage(Image.open("imgs/scissorsUser.png"))
rockImageComp = ImageTk.PhotoImage(Image.open("imgs/rockComp.png"))
paperImageComp = ImageTk.PhotoImage(Image.open("imgs/paperComp.png"))
scissorsImageComp = ImageTk.PhotoImage(Image.open("imgs/scissorsComp.png"))
# insert pictures
userLabel = Label(myFrame,image=scissorsImage,bg="SteelBlue1") 
compLabel = Label(myFrame,image=scissorsImageComp,bg="SteelBlue1") 
userLabel.grid(row=1,column=4) 
compLabel.grid(row=1,column=0) 
# scors
playerScore = Label(myFrame,text=0,font=100,bg="SteelBlue1",fg="white")
compScore = Label(myFrame,text=0,font=100,bg="SteelBlue1",fg="white")

playerScore.grid(row=1,column=3)
compScore.grid(row=1,column=1)

# indicators

userIndicator = Label(myFrame,font=50,text="USER",bg="SteelBlue1",fg="white").grid(row=0,column=3)
compIndicator = Label(myFrame,font=50,text="COMPUTER",bg="SteelBlue1",fg="white").grid(row=0,column=1)

message = Label(myFrame,font=50,bg="SteelBlue1",fg="white")
message.grid(row=3,column=2)

# update message
def updateMessage(msg):
    message['text'] = msg

def updateUserScore():
    score = int(playerScore["text"])
    score+=1
    playerScore['text'] = str(score)

def updateComputerScore():
    score = int(compScore["text"])
    score+=1
    compScore['text'] = str(score)

def checkWiner(player,computer):
    if player == computer:
        updateMessage("it's a tie")
    elif player == 'rock':
        if computer == 'paper':
            updateMessage('You Loose')
            updateComputerScore()
        else:
            updateMessage('You Win')
            updateUserScore()
    elif player == 'paper':
        if computer == 'scissors':
            updateMessage('You Loose')
            updateComputerScore()
        else:
            updateMessage('You Win')
            updateUserScore()
    elif player == 'scissors':#scissors
        if computer == 'rock':
            updateMessage('You Loose')
            updateComputerScore()
        else:
            updateMessage('You Win')
            updateUserScore()
    else:
        pass

# set the choices
choices = ['rock','paper','scissors']
# update choices
def updateChoices(click):
    # for computer
    compChoice = choice(choices)
    if compChoice == 'rock':
        compLabel.configure(image= rockImageComp)
    elif compChoice == "paper":
        compLabel.configure(image= paperImageComp)
    else:
        compLabel.configure(image= scissorsImageComp)
    # for user
    if click == 'rock':
        userLabel.configure(image= rockImage)
    elif click == "paper":
        userLabel.configure(image= paperImage)
    else:
        userLabel.configure(image= scissorsImage)
    
    checkWiner(click,compChoice)

# button
rock = Button(myFrame,width=20,height=2,text="ROCK",bg="#ff3e4d",fg="white",command=lambda:updateChoices("rock")).grid(row=2,column=1)
paper = Button(myFrame,width=20,height=2,text="PAPER",bg="#ff3e4d",fg="white",command=lambda:updateChoices("paper")).grid(row=2,column=2)
scissors = Button(myFrame,width=20,height=2,text="SCISSORS",bg="#ff3e4d",fg="white",command=lambda:updateChoices("scissors")).grid(row=2,column=3)

myFrame.mainloop()