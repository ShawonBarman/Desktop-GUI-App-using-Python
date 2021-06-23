# first install pygame by using the command which is pip install pygame
import pygame           #it is a module that is used for creating video games. It includes computer graphics and sound libraries.
import tkinter as tkr   #that is used for creating graphical user interfaces.
#it is used to open or save thing. So it has an open and safve functions that will enable you to open up dialog boxed to save or open them.
from tkinter.filedialog import askdirectory   #askdirectory basically is going to be responsible for presenting the user with a pop up window to choose a directory to use.
import os  #os module basically provides functions that allows you to interact with the user's operating system.

musicPlayer = tkr.Tk()
musicPlayer.title("Music Player")

#create a variable that will be used to prompt a user to choose the directory that contains their music files.
directory = askdirectory()
os.chdir(directory)   #os.chdir() method in python used to change the current working directory to specified path. It takes only a single argument as new directory path.
#create a variable that the music files from that directory will be assigned  to.
songlist = os.listdir()   #python method os.listdir() returns a list containing the names of the entries in the directory given by path.
#python tkinter Listbox widget is used to display the list items to the user. We can place only text items in the Listbox and all text items contain the same font and color.
playlist = tkr.Listbox(musicPlayer, font = "Helvetica 12 bold", bg = "yellow", selectmode=tkr.SINGLE)
for item in songlist:
    pos = 0
    playlist.insert(pos, item)
    pos = pos + 1

#initialize the pygame
pygame.init()
#initialize the pygame.mixer
pygame.mixer.init()

def play():  #that will control the playing of the music.
    pygame.mixer.music.load(playlist.get(tkr.ACTIVE))   #pygame/mixer.music.load() is the pygame module for controlling streamed audio and also loads a music file for playback.
    #to use the set method to set and change the value of any value that is stored within the tkinter variable.
    var.set(playlist.get(tkr.ACTIVE))   #this is doing basically is going to set whatever music was selected from the playlist that is active is going to set that.
    pygame.mixer.music.play()  #this play() method is what's going to be responsible for playing the selected music.

#this function will be responsible for existing or stopping the music player.
def exitMusicPlayer():
    pygame.mixer.music.stop()
#this function that we can use to pause the current music that is playing.
def pause():
    pygame.mixer.music.pause()
#this function willl be responsible for pausing the music ang agaim
def unpause():
    pygame.mixer.music.unpause()

button1 = tkr.Button(musicPlayer, width=5, height=3, font="Helvetica 12 bold", text="PLAY", bg="red", fg="white", command=play)
button2 = tkr.Button(musicPlayer, width=5, height=3, font="Helvetica 12 bold", text="STOP", bg="purple", fg="white", command=exitMusicPlayer)
button3 = tkr.Button(musicPlayer, width=5, height=3, font="Helvetica 12 bold", text="PAUSE", bg="green", fg="white", command=pause)
button4 = tkr.Button(musicPlayer, width=5, height=3, font="Helvetica 12 bold", text="UNPAUSE", bg="blue", fg="white", command=unpause)

var = tkr.StringVar()  #this StringVar is a class from tkinter. It is used to monitor changes to tkinter variables, and it also expects the default values to be a string.
songtitle = tkr.Label(musicPlayer, font="Helvetica 12 bold", textvariable=var)

songtitle.pack()
button1.pack(fill="x")
button2.pack(fill="x")
button3.pack(fill="x")
button4.pack(fill="x")
playlist.pack(fill="both", expand="yes")

musicPlayer.mainloop()