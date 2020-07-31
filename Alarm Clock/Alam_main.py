import tkinter as tk
from tkinter import *
import time
from tkinter import StringVar
from pygame import mixer

class alarm:
    
    #first window
    def st1_window(self):
        self.w1=tk.Tk()
        self.w1.title('Alarm')
        self.w1.geometry('300x200')
        
        time2 = time.strftime('%H:%M:%S')
        
        
        comment=Label(self.w1,text='Current Time',width=12,fg='white',bg='black').place(x=110,y=30)
        time_shower=Label(self.w1,text=time2,width=12,bg='black',fg='white',font=('bold',20)).place(x=60,y=60)
        set_alarm=Button(self.w1,text='Set an Alarm',width=12,command=self.set_it,bg='green',fg='white').place(x=110,y=110)
        
        self.w1.mainloop()
    
    def set_it(self):
        self.w1.destroy()
        
        self.w2=tk.Tk()
        self.w2.title('Set Alarm')
        self.w2.geometry('300x200')
        note=Label(self.w2,text='Enter time in 24 hours format as HH:MM').place(x=30,y=20)
        enter_time=Label(self.w2,text='Enter Time:',width=8,bg='black',fg='white').place(x=40,y=40)
        enter_note=Label(self.w2,text='Enter Message:',width=12,bg='black',fg='white').place(x=12,y=70)
        
        self.e1=StringVar(self.w2)
        
        ent=Entry(self.w2,width=12,textvariable=self.e1).place(x=110,y=40)
        
        self.e2=StringVar(self.w2)
        
        ent=Entry(self.w2,width=12,textvariable=self.e2).place(x=110,y=70)
        
        
        set_alamr=Button(self.w2,text='Set Alarm',bg='green',fg='white',command=self.setter).place(x=115,y=110)
        
    def setter(self):
        
        self.tie=self.e1.get()
        CurrentTime = time.strftime("%H:%M")
        if self.tie=='':
            messagebox.showwarning('Warning!','Enter valid time!')
            
        else:
            self.destruction()
            
            
    def destruction(self):
        self.w2.destroy()
        self.player()
        
            
    
        
            
            
        
       # '''else:
          #  self.w2.destroy()
            #print(self.tie)
            
           # self.w3=tk.Tk()
            #self.w3.geometry('300x200')
            #self.w3.title('Waiting for alarm')
            #show_info=Label(self.w3,text="Get back to your work, your alarm is on it's way",width='30',bg='purple',fg='white').place(x=30,y=30)'''
           
            
    def sjkn(self):
            self.w3.destroy()        
    def player(self):
        
            
            print(self.tie)
            
            self.w3=tk.Tk()
            self.w3.geometry('300x200')
            self.w3.title('Waiting for alarm')
            self.show_info3=Label(self.w3,text="Get back to your work, your alarm is on it's way",width='35',bg='black',fg='white').place(x=30,y=30)
            closer=Button(self.w3,text='Close This Tab',width=18,bg='green',fg='white',command=self.sjkn).place(x=30,y=80)
            self.w3.mainloop()
            #print('hello')
            CurrentTime = time.strftime("%H:%M")    
            while self.tie != CurrentTime:
    #label2.config(text ="The Alarm will Ring at {} ".format(AlarmTime))
    
                CurrentTime = time.strftime("%H:%M")
                time.sleep(2)
                
                
            if self.tie == CurrentTime:
                 #self.show_info3.configure(text='Playing song')
                 
                 print("now Alarm Musing Playing")
                 mixer.init()
                 mixer.music.load('2 - Orphans.mp3')
                 mixer.music.play()
                 #label2.config(text = "Alarm music playing.....")
                 self.alarm_playing()
                 #messagebox.showinfo(title= 'Alarm Message', message= "{}".format(self.e2.get()))
        
    def alarm_playing(self):
        self.new_w=tk.Tk()
        self.new_w.geometry('300x200')
        self.new_w.title('Playing Alarm')
        l1=Label(self.new_w,text='Your alarm is playing',bg='red',width=30).place(x=50,y=50)
        messagebox.showinfo('Alarm Message',self.e2.get())
        b1=Button(self.new_w,text='Stop',width=12,bg='red',fg='white',command=self.exitor).place(x=50,y=80)
        b2=Button(self.new_w,text='Snooze',width=12,bg='red',fg='white',command=self.snoozer).place(x=150,y=80)
        
    def exitor(self):
        mixer.music.pause()
        self.new_w.destroy()
        #pygame.mixer.pause()
    def snoozer(self):
        mixer.music.pause()
        self.new_w.destroy()
        
        CurrentTime = time.strftime("%H:%M")
    
    
    #57 02:57  02:59
    
    
        mins=CurrentTime[-2]+CurrentTime[-1]
        mins=int(mins)
        if mins<=57:
            mins+=2
        if mins<10:
            mins='0'+str(mins)
        newtime=CurrentTime[:-2:]+str(mins)
        self.tie=newtime
        #print(mins)
        #print(CurrentTime)
        #print(newtime)
        self.player()
        
        #print('snooze')

        
        
        
        
 #       

instance=alarm()
instance.st1_window()
        