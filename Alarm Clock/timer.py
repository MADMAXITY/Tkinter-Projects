from tkinter import *
import time
root = Tk()



































def closer():
    print('hello')

root.geometry('300x200')
clock = Label(root,width=12, font=('times', 20, 'bold'), bg='black',fg='white')
but=Button(root,width=12,command=root.destroy,bg='green',text='Set an Alarm').place(x=110,y=100)


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