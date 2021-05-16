from tkinter import *
import tkinter.font as font
import random

top = Tk()
playlist = []
myRolls = []

def addSong():
    playlist.append(E1.get())
    E1.delete(0, END)

def printList():
    print(playList)

def exportPlaylist():
    with open('playList.txt', 'w') as f:
        for song in playList:
            f.write("%s\n" % song)

def clearWindow():
    for widget in top.winfo_children():
        widget.destroy()

def mainMenu():
    clearWindow()
    LMain = Label(top, text = "Block 5 GUIs")
    LMain.grid(column = 0, row = 1)
    
    B1Main = Button(text = "Week 1", bg = "#b00b69", command= week1)
    B1Main.grid(column = 0, row = 2)
    
    B2Main = Button(text = "Week 2", bg = "#646319", command= week2)
    B2Main.grid(column = 0, row = 3)
    
    B3Main = Button(text = "Week 3", bg = "#C29898")
    B3Main.grid(column = 0, row = 4)

def week1():
    clearWindow()
    #this is a Label widget
    L1 = Label(top, text="Playlist Generator")
    L1.grid(column= 0, row= 1)

    #this is a Text Entry widget
    E1 = Entry(top, bd = 5)
    E1.grid(column = 0, row = 2)

    #this is a Button widget
    B1 = Button(text=" press this button to add the thing that you just typed to a list that exists somewhere on this computer.  ", bg = "#00C603", command = addSong)
    B1.grid(column = 0, row = 8)

    B2 = Button(text = "press this button to print the list that you just made a few seconds ago.", bg = "#DF0000", command = printList)
    B2.grid(column = 1, row = 1)

    B3 = Button(text = "press this button to export the list that you just made a few seconds ago.", bg = "#8a7e42", command = exportPlaylist)
    B3.grid(column = 1, row = 2)

    Bclear = Button(text = "press this button to break the button or something, I don't really know. I don't get paid enough for this.", bg = "#b88g78")
    bclear.grid(column = 2, row = 3)


def week2():
    def rollDice():
        #access the entry data
        rollTimes = E2W2.get()
        dieType = E2W2.get()
        
        #clear window

        #perform dice roll calculations
        for x in range(0, int(rollTimes)):
            myRolls.append(random.randint(1, int(dieType)))

        #display the result with two labels and  button that goes to main menu
        
        

    clearWindow()

    L1W2 = Label(top, text= "Dice Rollor App")
    L1W2.grid(column = 2, row = 1)

    L2W2 = Label(top, text= "# of sides")
    L2W2.grid(column = 0, row = 2)

    L3W2 = Label(top, text= "# of rolls")
    L3W2.grid(column = 3, row = 2)

    E1W2 = Entry(top, bd = 5)
    E1W2.grid(column = 0, row = 3)

    E2W2 = Entry(top, bd = 5)
    E2W2.grid(column = 3, row = 3)

    B1W2 = Button(text= "Roll em", bg = "yellow")
    B1W2.grid(column = 2, row = 4)

if __name__ == "__main__":
    mainMenu()
    top.mainloop()
