import pygame
import tkinter as tk
from tkinter.filedialog import askdirectory
import os

music_player=tk.Tk()
music_player.title("Music Player")
music_player.geometry("450x350")
directory=askdirectory()
os.chdir(directory)
song_list=os.listdir()

play_list=tk.Listbox(music_player,font="Helvetica 10 bold",bg='cyan',selectmode=tk.SINGLE)
for item in song_list:
    pos=0
    play_list.insert(pos,item)
    pos+=1

pygame.init()
pygame.mixer.init()

def play():
    pygame.mixer.music.load(play_list.get(tk.ACTIVE))
    var.set(play_list.get(tk.ACTIVE))
    pygame.mixer.music.play()

def stop():
    pygame.mixer.music.stop()

def pause():
    pygame.mixer.music.pause()

def unpause():
    pygame.mixer.music.unpause()

B1=tk.Button(music_player, width=5,height=3,font="Helvetica 12 bold", text="PLAY", command=play, bg="cyan", fg="black")
B2=tk.Button(music_player,width=5,height=3,font="Helvetica 12 bold", text="STOP", command=stop, bg="purple", fg="black")
B3=tk.Button(music_player,width=5,height=3,font="Helvetica 12 bold", text="PAUSE", command=pause, bg="pink", fg="black")
B4=tk.Button(music_player,width=5,height=3,font="Helvetica 12 bold", text="UNPAUSE", command=unpause, bg="orange", fg="black")

var=tk.StringVar()
song_title=tk.Label(music_player,font="Helvetica 12 bold",textvariable=var)

song_title.pack()
B1.pack(fill="x")
B2.pack(fill="x")
B3.pack(fill="x")
B4.pack(fill="x")
play_list.pack(fill="both",expand="yes")
music_player.mainloop()

