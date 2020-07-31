# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 00:31:42 2019

@author: Shankar Jadhav
"""

from tkinter import *
import time
root = Tk()
root.geometry('300x200')
clock = Label(root,width=12, font=('times', 20, 'bold'), bg='green')
clock.place(x=60,y=60)

def tick():
# get the current local time from the PC
    time2 = time.strftime('%H:%M:%S')
# if time string has changed, update it
    clock.config(text=time2)
# calls itself every 200 milliseconds
# to update the time display as needed
# could use >200 ms, but display gets jerky
    clock.after(200, tick)
tick()
root.mainloop( )