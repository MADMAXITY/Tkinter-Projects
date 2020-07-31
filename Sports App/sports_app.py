import tkinter as tk
from tkinter import *
from tkinter import StringVar
from tkinter import messagebox
from selenium import webdriver

class sports:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('600x500')
        self.root.title("Sports App")

        photo = PhotoImage(file="download.png")
        self.root.iconphoto(False, photo)

        C = Canvas(self.root, bg="blue", height=600, width=500)
        filename = PhotoImage(file='6814141_preview.png')
        background_label = Label(self.root, image=filename)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        l1 = tk.Label(self.root,text="From The Lovers of Sports To the Lovers of Sports").place(x=170,y=400)

        b1 = Button(self.root,text= 'Next', command = self.des1).place(x=550,y=450)
        self.root.mainloop()
    def des1(self):
        self.root.destroy()
        self.login()
    def login(self):
        self.root = tk.Tk()
        self.root.geometry('600x500')
        self.root.title("Sports App")

        photo = PhotoImage(file="download.png")
        self.root.iconphoto(False, photo)

        C = Canvas(self.root, bg="blue", height=600, width=500)
        filename = PhotoImage(file='6814141_preview.png')
        background_label = Label(self.root, image=filename)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)



        self.username = StringVar()
        self.password = StringVar()

        Entry(self.root,textvariable = self.username,width=15).place(x=250,y=200)
        Entry(self.root,textvariable=self.password, width=15).place(x=250, y=230)
        Button(self.root,text='Login',command=self.check1).place(x=275,y=260)

        mainloop()

    def check1(self):

        if self.username.get()=="" or self.password.get()=="":
            messagebox.showwarning(title='Warning', message='You Must fill all the boxes!')
        elif self.username.get()  != "s" or self.password.get() != "s":
            messagebox.showwarning(title='Warning', message='Wrong Username/password!')
        else:
            self.root.destroy()
            self.menu()
    def menu(self):
        self.root = tk.Tk()
        
        self.root.geometry('600x500')
        self.root.title("Sports App")

        photo = PhotoImage(file="download.png")
        self.root.iconphoto(False, photo)

        C = Canvas(self.root, bg="blue", height=600, width=500)
        filename = PhotoImage(file='6814141_preview.png')
        background_label = Label(self.root, image=filename)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        Button(self.root,text='Football',command= self.football,height='3',width='10').place(x=40,y=60)
        Button(self.root, text='Cricket', height='3',command=self.cricket, width='10').place(x=270, y=60)
        Button(self.root, text='Tennis', height='3', command=self.tennis,width='10').place(x=480, y=60)

        Button(self.root, text='Hockey', height='3',command=self.Hockey, width='10').place(x=40, y=250)
        Button(self.root, text='Basketball', height='3',command=self.basketball, width='10').place(x=270, y=250)
        Button(self.root, text='F1 Racing',command=self.f1racing,height='3', width='10').place(x=480, y=250)


        mainloop()

    def football(self):
        self.best_player =  'Lionel Messi'
        self.best_team = 'Belgium'
        self.board = 'FIFA'
        self.game_type = 'Team'
        self.num_players = '11'
        self.last_world_cup_winner = 'France'
        self.most_world_c_wins = 'France'
        self.link = 'https://www.fifa.com/'
        self.root.destroy()
        self.last_win()

    def cricket(self):
        self.best_player = 'Virat Kohli'
        self.best_team = 'India'
        self.board = 'ICC'
        self.game_type = 'Team'
        self.num_players = '11'
        self.last_world_cup_winner = 'England'
        self.most_world_c_wins = 'Australia'
        self.link = 'https://www.icc-cricket.com/'
        self.root.destroy()
        self.last_win()

    def tennis(self):
        self.best_player = 'Roger Federer'
        self.best_team = 'Germany'
        self.board = 'ITFT'
        self.game_type = 'Individual/Duo'
        self.num_players = '1/2'
        self.last_world_cup_winner = 'Spain'
        self.most_world_c_wins = 'Germany'
        self.link = 'https://www.itftennis.com/en/'
        self.root.destroy()
        self.last_win()

    def Hockey(self):
        self.best_player = 'Sidney Crosby'
        self.best_team = 'Switzerland'
        self.board = 'IHF'
        self.game_type = 'Team'
        self.num_players = '6'
        self.last_world_cup_winner = 'Netherlands'
        self.most_world_c_wins = 'Switzerland'
        self.link = 'http://www.fih.ch/'
        self.root.destroy()
        self.last_win()

    def basketball(self):
        self.best_player = 'LeBron James'
        self.best_team = 'USA'
        self.board = 'FIBA'
        self.game_type = 'Team'
        self.num_players = '5'
        self.last_world_cup_winner = 'Spain'
        self.most_world_c_wins = 'USA'
        self.link = 'http://www.fiba.basketball/'
        self.root.destroy()
        self.last_win()
    def f1racing(self):
        self.best_player = 'Mika Häkkinen'
        self.best_team = 'UK'
        self.board = 'FIA'
        self.game_type = 'Individual'
        self.num_players = '1'
        self.last_world_cup_winner = 'UK'
        self.most_world_c_wins = 'UK'
        self.link = 'https://www.formula1.com/'
        self.root.destroy()
        self.last_win()



    def last_win(self):
        self.root = tk.Tk()
        self.root.geometry('600x500')
        self.root.title("Sports App")

        photo = PhotoImage(file="download.png")
        self.root.iconphoto(False, photo)

        C = Canvas(self.root, bg="blue", height=600, width=500)
        filename = PhotoImage(file='6814141_preview.png')
        background_label = Label(self.root, image=filename)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)


        l =  Label(self.root,text='Best Player : '+self.best_player,bg = 'black',fg = 'white').place(x=40,y=60)
        l1 = Label(self.root, text='Best Team : ' + self.best_team, bg='black', fg='white').place(x=40, y=100)
        l2 = Label(self.root,text='Board : '+self.board,bg = 'black',fg = 'white').place(x=40,y=140)
        l = Label(self.root, text='Game Type : ' + self.game_type, bg='black', fg='white').place(x=40, y=180)
        l = Label(self.root, text='Players in a Team : ' + self.num_players, bg='black', fg='white').place(x=40, y=220)
        l = Label(self.root, text='Last WC Winner : ' + self.last_world_cup_winner, bg='black', fg='white').place(x=40, y=260)
        l = Label(self.root, text='Most WC Wins : ' + self.most_world_c_wins, bg='black', fg='white').place(x=40, y=300)
        #l = Label(self.root, text='Best Player : ' + self.best_player, bg='black', fg='white').place(x=40, y=340)
        b = Button(self.root, text='Back',command = self.dest, height=4, width=12).place(x=300, y=100)
        b = Button(self.root,text = 'Visit Webpage',command=self.selen,height =4,width=12).place(x=300,y=220)

        self.root.mainloop()
    def dest(self):
        self.root.destroy()
        self.menu()

    def selen(self):
        win = webdriver.Chrome('chromedriver.exe')
        win.get(self.link)


















if __name__ =="__main__":
    o = sports()
