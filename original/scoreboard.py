from time import time
try:
    from Tkinter import *
except:
    from tkinter import *

class __Anzeige:
    
    def __init__(self):
        """Initialisierung des Programms, vergleichbar mit einem Konstruktor"""
        self.__games_sel = 0
        self.__points_sel = 0
        self.__time_sel = 0
        self.__overtime_sel = 0
        self.__is_timeouts = True
        self.__is_teamfouls = True
        self.__points_l = 0
        self.__points_r = 0
        self.__root = Tk()
        self.__root.title('Auswahl der Sportart')
        self.__root.config(bg='white')
        self.__scr_w = self.__root.winfo_screenwidth()
        self.__scr_h = self.__root.winfo_screenheight()
        self.__root.geometry('{0}x{1}'.format(self.__scr_w, self.__scr_h)) #Quelle: Stack Overflow: Display fullscreen mode on Tkinter
        self.__start_fullscreen()
        self.__root.bind('<Escape>', self.__end_fullscreen)
        self.__root.bind('<F11>', self.__start_fullscreen)
        self.__select_sport()

    def __do_nothing(self, *event):
        """Methode, die nichts tut. Nützlich, um die Funktionalität mancher Tasten an der Tastatur zu stoppen"""
        pass
        
    def __start_fullscreen(self, *event):
        """Starten des Vollbildmodus

           Quelle: Stack Overflow: Display fullscreen mode on Tkinter"""
        self.__root.attributes('-fullscreen', True)
        
    def __end_fullscreen(self, event):
        """Beenden des Vollbildmodus

           Quelle: Stack Overflow: Display fullscreen mode on Tkinter"""
        self.__root.attributes('-fullscreen', False)
    
    def __clear_tk(self):
        """Löschen der mit '.place()' platzierten Widgets aus dem Interface

           Quelle: Stack Overflow: How to delete Tkinter widgets from a window?"""
        for __widget in self.__root.place_slaves():
            __widget.destroy()

    def __select_sport(self):
        """Erzeugen der Widgets im Startmenü zum Auswählrn einer Sportart"""
        self.__button_fb = Button(self.__root, text='Fußball', command=self.__select_fb)
        self.__button_bb = Button(self.__root, text='Basketball', command=self.__select_bb)
        self.__button_hb = Button(self.__root, text='Handball', command=self.__select_hb)
        self.__button_vb = Button(self.__root, text='Volleyball', command=self.__select_vb)
        self.__button_bm = Button(self.__root, text='Badminton', command=self.__select_bm)
        self.__button_tt = Button(self.__root, text='Tischtennis', command=self.__select_tt)
        self.__button_fb.place(relx=0, rely=0, relwidth=1/2, relheight=1/3)
        self.__button_bb.place(relx=0, rely=1/3, relwidth=1/2, relheight=1/3)
        self.__button_hb.place(relx=0, rely=2/3, relwidth=1/2, relheight=1/3)
        self.__button_vb.place(relx=1/2, rely=0, relwidth=1/2, relheight=1/3)
        self.__button_bm.place(relx=1/2, rely=1/3, relwidth=1/2, relheight=1/3)
        self.__button_tt.place(relx=1/2, rely=2/3, relwidth=1/2, relheight=1/3)
        for __widget in self.__root.place_slaves():
            __widget.config(bg='white', font=('Times', int(0.04*self.__scr_w)), relief='groove')
     
    def __games_sel_up(self):
        """Erhöhen der ausgewählten Sätze um den Wert 1"""
        if self.__games_sel < 9:
            self.__games_sel += 1
            self.__games.config(text='Sätze zum Sieg: ' + str(self.__games_sel))
        
    def __games_sel_down(self):
        """Erniedrigen der ausgewählten Sätze um den Wert 1"""
        if self.__games_sel > 1:
            self.__games_sel -= 1
            self.__games.config(text='Sätze zum Sieg: ' + str(self.__games_sel))
        
    def __points_sel_up(self):
        """Erhöhen der ausgewählten Punkte um den Wert 1"""
        if self.__points_sel < 99:
            self.__points_sel += 1
            self.__points.config(text='Punkte zum Satz: ' + str(self.__points_sel))
        
    def __points_sel_down(self):
        """Erniedrigen der ausgewählten Punkte um den Wert 1"""
        if self.__points_sel > 5:
            self.__points_sel -= 1
            self.__points.config(text='Punkte zum Satz: ' + str(self.__points_sel))
            
    def __points_sel_ten_up(self):
        """Erhöhen der ausgewählten Punkte um den Wert 10"""
        if self.__points_sel < 90:
            self.__points_sel += 10
        else:
            self.__points_sel = 99
        self.__points.config(text='Punkte zum Satz: ' + str(self.__points_sel))
       
    def __points_sel_ten_down(self):
        """Erniedrigen der ausgewählten Punkte um den Wert 10"""
        if self.__points_sel > 14:
            self.__points_sel -= 10
        else:
            self.__points_sel = 5
        self.__points.config(text='Punkte zum Satz: ' + str(self.__points_sel))
    
    def __time_sel_up(self):
        """Erhöhen der ausgewählten Spielzeit um den Wert 1"""
        if self.__time_sel < 60:
            self.__time_sel += 1
            self.__time.config(text='Zeit pro Abschnitt: ' + str(self.__time_sel) + ' Minuten')
        
    def __time_sel_down(self):
        """Erniedrigen der ausgewählten Spielzeit um den Wert 1"""
        if self.__time_sel > 1:
            self.__time_sel -= 1
            self.__time.config(text='Zeit pro Abschnitt: ' + str(self.__time_sel) + ' Minuten')
                   
    def __time_sel_ten_up(self):
        """Erhöhen der ausgewählten Spielzeit um den Wert 10"""
        if self.__time_sel < 51:
            self.__time_sel += 10
        else:
            self.__time_sel = 60
        self.__time.config(text='Zeit pro Abschnitt: ' + str(self.__time_sel) + ' Minuten')
        
    def __time_sel_ten_down(self):
        """Erniedrigen der ausgewählten Spielzeit um den Wert 10"""
        if self.__time_sel > 10:
            self.__time_sel -= 10
        else:
            self.__time_sel = 1
        self.__time.config(text='Zeit pro Abschnitt: ' + str(self.__time_sel) + ' Minuten')
    
    def __overtime_sel_up(self):
        """Erhöhen der ausgewählten Spielzeit in der Verlängerung um den Wert 1"""
        if self.__overtime_sel < 60:
            self.__overtime_sel += 1
            self.__overtime.config(text='Zeit pro Abschnitt in der Verlängerung: ' + str(self.__overtime_sel) + ' Minuten')
        
    def __overtime_sel_down(self):
        """Erniedrigen der ausgewählten Spielzeit in der Verlängerung um den Wert 1"""
        if self.__overtime_sel > 1:
            self.__overtime_sel -= 1
            self.__overtime.config(text='Zeit pro Abschnitt in der Verlängerung: ' + str(self.__overtime_sel) + ' Minuten')
                   
    def __overtime_sel_ten_up(self):
        """Erhöhen der ausgewählten Spielzeit in der Verlängerung um den Wert 10"""
        if self.__overtime_sel < 51:
            self.__overtime_sel += 10
        else:
            self.__overtime_sel = 60
        self.__overtime.config(text='Zeit pro Abschnitt in der Verlängerung: ' + str(self.__overtime_sel) + ' Minuten')
        
    def __overtime_sel_ten_down(self):
        """Erniedrigen der ausgewählten Spielzeit in der Verlängerung um den Wert 10"""
        if self.__overtime_sel > 10:
            self.__overtime_sel -= 10
        else:
            self.__overtime_sel = 1
        self.__overtime.config(text='Zeit pro Abschnitt in der Verlängerung: ' + str(self.__overtime_sel) + ' Minuten')
        
    def __change_is_timeouts(self):
        """Auswahl, ob man mit oder ohne Timeouts spielen möchte"""
        if self.__is_timeouts == False:
            self.__is_timeouts = True
            self.__ask_timeouts.config(text='Timeouts: an', bg='yellowgreen')
        else:
            self.__is_timeouts = False
            self.__ask_timeouts.config(text='Timeouts: aus', bg='orangered')
            
    def __change_is_teamfouls(self):
        """Auswahl, ob man mit oder ohne Teamfouls spielen möchte"""
        if self.__is_teamfouls == False:
            self.__is_teamfouls = True
            self.__ask_teamfouls.config(text='Teamfouls: an', bg='yellowgreen')
        else:
            self.__is_teamfouls = False
            self.__ask_teamfouls.config(text='Teamfouls: aus', bg='orangered')
               
    def __select_fb(self):
        """Starten eines Menüs für den Sport Fußball, um Teamnamen und Spielzeiten festzulegen""" 
        self.__clear_tk()
        self.__root.title('Auswahl - Fußball')
        self.__sport = 'fb'
        self.__time_sel = 45
        self.__overtime_sel = 15
        self.__ready = Button(self.__root, text='go', fg='white', bg='black', font=('Times', int(0.015*self.__scr_w)), relief='groove', command=self.__start_fb)
        self.__sel_fb_bb_hb()
        self.__root.bind('<Return>', self.__start_fb)
        
    def __select_bb(self):
        """Starten eines Menüs für den Sport Basketball, um Teamnamen, Spielzeiten, Timeouts und Teamfouls festzulegen"""
        self.__clear_tk()
        self.__root.title('Auswahl - Basketball')
        self.__sport = 'bb'
        self.__time_sel = 10
        self.__overtime_sel = 5
        self.__ready = Button(self.__root, text='go', fg='white', bg='black', font=('Times', int(0.015*self.__scr_w)), relief='groove', command=self.__start_bb)
        self.__ask_timeouts = Button(self.__root, text='Timeouts: an', bg='yellowgreen', justify='center', font=('Times', int(0.025*self.__scr_w)), relief='groove', command=self.__change_is_timeouts)
        self.__ask_teamfouls = Button(self.__root, text='Teamfouls: an', bg='yellowgreen', justify='center', font=('Times', int(0.025*self.__scr_w)), relief='groove', command=self.__change_is_teamfouls)
        self.__sel_fb_bb_hb()
        self.__ask_timeouts.place(relx=3/20, rely=3/4, relwidth=7/20, relheight=1/8)
        self.__ask_teamfouls.place(relx=1/2, rely=3/4, relwidth=7/20, relheight=1/8)
        self.__root.bind('<Return>', self.__start_bb)
        
    def __select_hb(self):
        """Starten eines Menüs für den Sport Basketball, um Teamnamen, Spielzeiten und Timeouts festzulegen"""
        self.__clear_tk()
        self.__root.title('Auswahl - Handball')
        self.__sport = 'hb'
        self.__time_sel = 30
        self.__overtime_sel = 5
        self.__ready = Button(self.__root, text='go', fg='white', bg='black', font=('Times', int(0.015*self.__scr_w)), relief='groove', command=self.__start_hb)
        self.__ask_timeouts = Button(self.__root, text='Timeouts: an', bg='yellowgreen', justify='center', font=('Times', int(0.025*self.__scr_w)), relief='groove', command=self.__change_is_timeouts)
        self.__sel_fb_bb_hb()
        self.__ask_timeouts.place(relx=3/20, rely=3/4, relwidth=7/10, relheight=1/8)
        self.__root.bind('<Return>', self.__start_hb)
        
    def __sel_fb_bb_hb(self):
        """Erzeugen und Platzieren der Widgets für das Auswahlmenü, die im Fußball, Basketball und Handball identisch sind"""
        self.__time = Message(self.__root, text='Zeit pro Abschnitt: '+str(self.__time_sel)+' Minuten', bg='light gray', justify='center', font=('Times', int(0.02*self.__scr_w)), relief='groove')
        self.__time_down = Button(self.__root, text='-1', bg='orangered', font=('Times', int(0.025*self.__scr_w)), relief='groove', command=self.__time_sel_down)
        self.__time_up = Button(self.__root, text='+1', bg='yellowgreen', font=('Times', int(0.025*self.__scr_w)), relief='groove', command=self.__time_sel_up)
        self.__time_ten_down = Button(self.__root, text='-10', bg='orangered', font=('Times', int(0.025*self.__scr_w)), relief='groove', command=self.__time_sel_ten_down)
        self.__time_ten_up = Button(self.__root, text='+10', bg='yellowgreen', font=('Times', int(0.025*self.__scr_w)), relief='groove', command=self.__time_sel_ten_up)
        self.__overtime = Message(self.__root, text='Zeit pro Abschnitt in der Verlängerung: '+str(self.__overtime_sel)+' Minuten', bg='light gray', justify='center', font=('Times', int(0.02*self.__scr_w)), relief='groove')
        self.__overtime_down = Button(self.__root, text='-1', bg='orangered', font=('Times', int(0.025*self.__scr_w)), relief='groove', command=self.__overtime_sel_down)
        self.__overtime_up = Button(self.__root, text='+1', bg='yellowgreen', font=('Times', int(0.025*self.__scr_w)), relief='groove', command=self.__overtime_sel_up)
        self.__overtime_ten_down = Button(self.__root, text='-10', bg='orangered', font=('Times', int(0.025*self.__scr_w)), relief='groove', command=self.__overtime_sel_ten_down)
        self.__overtime_ten_up = Button(self.__root, text='+10', bg='yellowgreen', font=('Times', int(0.025*self.__scr_w)), relief='groove', command=self.__overtime_sel_ten_up)
        self.__home = Entry(self.__root, justify='center', font=('Times', int(0.025*self.__scr_w)))
        self.__guest = Entry(self.__root, justify='center', font=('Times', int(0.025*self.__scr_w)))
        self.__home.insert(0, 'Heim')
        self.__guest.insert(0, 'Gast')
        self.__time.place(relx=1/4, rely=1/4, relwidth=1/2, relheight=1/4)
        self.__time_down.place(relx=3/20, rely=1/4, relwidth=1/10, relheight=1/8)
        self.__time_up.place(relx=3/4, rely=1/4, relwidth=1/10, relheight=1/8)
        self.__time_ten_down.place(relx=3/20, rely=3/8, relwidth=1/10, relheight=1/8)
        self.__time_ten_up.place(relx=3/4, rely=3/8, relwidth=1/10, relheight=1/8)
        self.__overtime.place(relx=1/4, rely=1/2, relwidth=1/2, relheight=1/4)
        self.__overtime_down.place(relx=3/20, rely=1/2, relwidth=1/10, relheight=1/8)
        self.__overtime_up.place(relx=3/4, rely=1/2, relwidth=1/10, relheight=1/8)
        self.__overtime_ten_down.place(relx=3/20, rely=5/8, relwidth=1/10, relheight=1/8)
        self.__overtime_ten_up.place(relx=3/4, rely=5/8, relwidth=1/10, relheight=1/8)
        self.__ready.place(x=11/12*self.__scr_w-10, y=9/10*self.__scr_h-10, width=1/12*self.__scr_w, height=1/10*self.__scr_h)
        self.__home.place(relx=3/20, rely=1/8, relwidth=7/20, relheight=1/8)
        self.__guest.place(relx=1/2, rely=1/8, relwidth=7/20, relheight=1/8)
    
    def __select_vb(self):
        """Starten eines Menüs für den Sport Volleyball, um Teamnamen, Sätze, Punkte und Timeouts festzulegen"""
        self.__clear_tk()
        self.__root.title('Auswahl - Volleyball')
        self.__sport = 'vb'
        self.__games_sel = 3
        self.__points_sel = 25
        self.__ready = Button(self.__root, text='go', fg='white', bg='black', font=('Times', int(0.015*self.__scr_w)), relief='groove', command=self.__start_vb)
        self.__ask_timeouts = Button(self.__root, text='Timeouts: an', bg='yellowgreen', justify='center', font=('Times', int(0.025*self.__scr_w)), relief='groove', command=self.__change_is_timeouts)
        self.__sel_vb_bm_tt()
        self.__ask_timeouts.place(relx=3/20, rely=3/4, relwidth=7/10, relheight=1/8)
        self.__root.bind('<Return>', self.__start_vb)
        
    def __select_bm(self):
        """Starten eines Menüs für den Sport Badminton, um Teamnamen, Sätze und Punkte festzulegen"""
        self.__clear_tk()
        self.__root.title('Auswahl - Badminton')
        self.__sport = 'bm'
        self.__games_sel = 2
        self.__points_sel = 21
        self.__ready = Button(self.__root, text='go', fg='white', bg='black', font=('Times', int(0.015*self.__scr_w)), relief='groove', command=self.__start_bm)
        self.__sel_vb_bm_tt()
        self.__root.bind('<Return>', self.__start_bm)
        
    def __select_tt(self):
        """Starten eines Menüs für den Sport Tischtennis, um Teamnamen, Sätze und Punkte festzulegen"""
        self.__clear_tk()
        self.__root.title('Auswahl - Tischtennis')
        self.__sport = 'tt'
        self.__games_sel = 2
        self.__points_sel = 11
        self.__ready = Button(self.__root, text='go', fg='white', bg='black', font=('Times', int(0.015*self.__scr_w)), relief='groove', command=self.__start_tt)
        self.__sel_vb_bm_tt()
        self.__root.bind('<Return>', self.__start_tt)
        
    def __sel_vb_bm_tt(self):
        """Erzeugen und Platzieren der Widgets für das Auswahlmenü, die im Volleyball, Badminton und Tischtennis identisch sind"""
        self.__games = Message(self.__root, text=('Sätze zum Sieg: ' + str(self.__games_sel)), bg='light gray', justify='center', font=('Times', int(0.025*self.__scr_w)), relief='groove')
        self.__games_down = Button(self.__root, text='-1', bg='orangered', font=('Times', int(0.025*self.__scr_w)), relief='groove', command=self.__games_sel_down)
        self.__games_up = Button(self.__root, text='+1', bg='yellowgreen', font=('Times', int(0.025*self.__scr_w)), relief='groove', command=self.__games_sel_up)
        self.__points = Message(self.__root, text=('Punkte zum Satz: ' + str(self.__points_sel)), bg='light gray', justify='center', font=('Times', int(0.025*self.__scr_w)), relief='groove')
        self.__points_down = Button(self.__root, text='-1', bg='orangered', font=('Times', int(0.025*self.__scr_w)), relief='groove', command=self.__points_sel_down)
        self.__points_up = Button(self.__root, text='+1', bg='yellowgreen', font=('Times', int(0.025*self.__scr_w)), relief='groove', command=self.__points_sel_up)
        self.__points_ten_down = Button(self.__root, text='-10', bg='orangered', font=('Times', int(0.025*self.__scr_w)), relief='groove', command=self.__points_sel_ten_down)
        self.__points_ten_up = Button(self.__root, text='+10', bg='yellowgreen', font=('Times', int(0.025*self.__scr_w)), relief='groove', command=self.__points_sel_ten_up)
        self.__home = Entry(self.__root, justify='center', font=('Times', int(0.025*self.__scr_w)))
        self.__guest = Entry(self.__root, justify='center', font=('Times', int(0.025*self.__scr_w)))
        self.__home.insert(0, 'Heim')
        self.__guest.insert(0, 'Gast')
        self.__games.place(relx=1/4, rely=1/4, relwidth=1/2, relheight=1/4)
        self.__games_down.place(relx=3/20, rely=1/4, relwidth=1/10, relheight=1/4)
        self.__games_up.place(relx=3/4, rely=1/4, relwidth=1/10, relheight=1/4)
        self.__points.place(relx=1/4, rely=1/2, relwidth=1/2, relheight=1/4)
        self.__points_down.place(relx=3/20, rely=1/2, relwidth=1/10, relheight=1/8)
        self.__points_up.place(relx=3/4, rely=1/2, relwidth=1/10, relheight=1/8)
        self.__points_ten_down.place(relx=3/20, rely=5/8, relwidth=1/10, relheight=1/8)
        self.__points_ten_up.place(relx=3/4, rely=5/8, relwidth=1/10, relheight=1/8)
        self.__home.place(relx=3/20, rely=1/8, relwidth=7/20, relheight=1/8)
        self.__guest.place(relx=1/2, rely=1/8, relwidth=7/20, relheight=1/8)
        self.__ready.place(x=11/12*self.__scr_w-10, y=9/10*self.__scr_h-10, width=1/12*self.__scr_w, height=1/10*self.__scr_h)
        
    def __start_fb(self, *event):
        """Starten der Anzeige für den Sport Fußball"""
        self.__team_left = self.__home.get()
        self.__team_right = self.__guest.get()
        self.__clear_tk()
        self.__root.title('Anzeige - Fußball')
        self.__is_timeouts = False
        self.__is_teamfouls = False
        self.__phases = 2
        self.__start_fb_bb_hb()
        self.__cache = [[0, 0]]

    def __start_bb(self, *event):
        """Starten der Anzeige für den Sport Basketball"""
        self.__team_left = self.__home.get()
        self.__team_right = self.__guest.get()
        self.__clear_tk()
        self.__root.title('Anzeige - Basketball')
        self.__phases = 4
        self.__time_1_layout = str(self.__time_sel) + ':00'
        self.__start_fb_bb_hb()
        if self.__is_teamfouls == True:
            self.__tf_l = 0
            self.__tf_r = 0
            self.__show_tf_left = Button(self.__root, text=('Fouls: ' + str(self.__tf_l)), fg='dark blue', bg ='white', font=('Times', int(0.03*self.__scr_w)),relief='flat', highlightthickness=0, command=self.__tf_l_up)
            self.__show_tf_right = Button(self.__root, text=('Fouls: ' + str(self.__tf_r)), fg='dark red', bg ='white', font=('Times', int(0.03*self.__scr_w)), relief='flat', highlightthickness=0, command=self.__tf_r_up)
            self.__show_tf_left.place(relx=7/120, rely=5/8, relwidth=1/6, relheight=1/8)
            self.__show_tf_right.place(relx=31/40, rely=5/8, relwidth=1/6, relheight=1/8)
        if self.__is_timeouts == True:
            self.__tol_l = 2
            self.__tol_r = 2
            self.__show_tol_left = Button(self.__root, text=('TOL: ' + str(self.__tol_l)), fg='dark blue', bg ='white', font=('Times', int(0.03*self.__scr_w)),relief='flat', highlightthickness=0, command=self.__tol_l_down)
            self.__show_tol_right = Button(self.__root, text=('TOL: ' + str(self.__tol_r)), fg='dark red', bg ='white', font=('Times', int(0.03*self.__scr_w)), relief='flat', highlightthickness=0, command=self.__tol_r_down)
            self.__show_tol_left.place(relx=7/120, rely=3/4, relwidth=1/6, relheight=1/8)
            self.__show_tol_right.place(relx=31/40, rely=3/4, relwidth=1/6, relheight=1/8)
        if self.__is_teamfouls == True and self.__is_timeouts == True:
            self.__cache = [[0, 0, 2, 2, 0, 0]]
        elif self.__is_teamfouls == True and self.__is_timeouts == False:
            self.__cache = [[0, 0, 0, 0]]
        elif self.__is_teamfouls == False and self.__is_timeouts == True:
            self.__cache = [[0, 0, 2, 2]]
        else:
            self.__cache = [[0, 0]]

    def __start_hb(self, *event):
        """Starten der Anzeige für den Sport Handball"""
        self.__team_left = self.__home.get()
        self.__team_right = self.__guest.get()
        self.__clear_tk()
        self.__root.title('Anzeige - Handball')
        self.__is_teamfouls = False
        self.__phases = 2
        self.__start_fb_bb_hb()
        if self.__is_timeouts == True:
            self.__tol_l = 3
            self.__tol_r = 3
            self.__show_tol_left = Button(self.__root, text=('TOL: ' + str(self.__tol_l)), fg='dark blue', bg ='white', font=('Times', int(0.03*self.__scr_w)),relief='flat', highlightthickness=0, command=self.__tol_l_down)
            self.__show_tol_right = Button(self.__root, text=('TOL: ' + str(self.__tol_r)), fg='dark red', bg ='white', font=('Times', int(0.03*self.__scr_w)), relief='flat', highlightthickness=0, command=self.__tol_r_down)
            self.__show_tol_left.place(relx=7/120, rely=11/16, relwidth=1/6, relheight=1/8)
            self.__show_tol_right.place(relx=31/40, rely=11/16, relwidth=1/6, relheight=1/8)
            self.__cache = [[0, 0, 3, 3]]
        else:
            self.__cache = [[0, 0]]

    def __start_fb_bb_hb(self):
        """Starten der Anzeige für die Sportarten Fußball, Basketball und Handball"""
        self.__root.bind('<Return>', self.__do_nothing)
        self.__phase = 1
        self.__last_deleted = []
        self.__last_action = '-'
        if self.__sport == 'fb' or self.__sport == 'hb':
            self.__time_1_layout = '0:00'
        elif self.__sport == 'bb':
            self.__time_1_layout = str(self.__time_sel) + ':00'
        self.__is_paused = True
        self.__is_break = True
        self.__show_points_left = Button(self.__root, text=str(self.__points_l), fg='dark blue', bg='white', anchor=E, font=('Times', int(0.115*self.__scr_w)), relief='flat', highlightthickness=0, command=self.__add_point_fb_bb_hb_left)
        self.__show_points_right = Button(self.__root, text=str(self.__points_r), fg='dark red', bg='white', anchor=W, font=('Times', int(0.115*self.__scr_w)), relief='flat', highlightthickness=0, command=self.__add_point_fb_bb_hb_right)
        self.__root.bind('l', self.__add_point_fb_bb_hb_left)
        self.__root.bind('r', self.__add_point_fb_bb_hb_right)
        self.__colon = Label(self.__root, text=':', bg='white', font=('Times', int(0.115*self.__scr_w)))
        self.__show_phase = Label(self.__root, text='1', bg='white', font=('Times', int(0.025*self.__scr_w)), relief='groove')
        self.__show_time = Label(self.__root, text=self.__time_1_layout, bg='white', font=('Times', int(0.075*self.__scr_w)), relief='groove')
        self.__show_home = Label(self.__root, text=self.__team_left, fg='dark blue', bg='white', anchor=E, font=('Times', int(0.04*self.__scr_w)))
        self.__show_guest = Label(self.__root, text=self.__team_right, fg='dark red', bg='white', anchor=W, font=('Times', int(0.04*self.__scr_w)))
        self.__hyphen = Label(self.__root, text='-', bg='white', font=('Times', int(0.05*self.__scr_w)))
        self.__show_points_left.place(relx=9/40, rely=7/12, relwidth=1/4, relheight=5/16)
        self.__show_points_right.place(relx=21/40, rely=7/12, relwidth=1/4, relheight=5/16)
        self.__colon.place(relx=19/40, rely=7/12, relwidth=1/20, relheight=9/32)
        self.__show_phase.place(relx=14/30, rely=1/16, relwidth=1/15, relheight=1/15)
        self.__show_time.place(relx=3/8, rely=1/8, relwidth=1/4, relheight=1/6)
        self.__show_home.place(relx=1/64, rely=5/12, relwidth=147/320, relheight=1/8)
        self.__show_guest.place(relx=21/40, rely=5/12, relwidth=147/320, relheight=1/8)
        self.__hyphen.place(relx=19/40, rely=5/12, relwidth=1/20, relheight=1/10)
        self.__time_0 = time()
        self.__time_1 = 0
        self.__time_p = 0
        self.__last_time = ''
        self.__in_overtime = False
        self.__in_penalty = False
        self.__count()
        self.__root.bind('<space>', self.__start_match)
        self.__root.bind('z', self.__step_back_fb_bb_hb)
        
    def __start_vb(self, *event):
        """Starten der Anzeige für den Sport Volleyball"""
        self.__team_left = self.__home.get()
        self.__team_right = self.__guest.get()
        self.__clear_tk()
        self.__root.title('Anzeige - Volleyball')
        self.__max_break = int(3/5*self.__points_sel)
        self.__show_points_left = Button(self.__root, text=str(self.__points_l), fg='dark blue', bg='white', anchor=E, font=('Times', int(0.15*self.__scr_w)), relief='flat', highlightthickness=0, command=self.__service_vb_left)
        self.__show_points_right = Button(self.__root, text=str(self.__points_r), fg='dark red', bg='white', anchor=W, font=('Times', int(0.15*self.__scr_w)), relief='flat', highlightthickness=0, command=self.__service_vb_right)
        self.__root.bind('l', self.__service_vb_left)
        self.__root.bind('r', self.__service_vb_right)
        self.__start_vb_bm_tt()
        if self.__is_timeouts == True:
            self.__tol_l = 2
            self.__tol_r = 2
            self.__show_tol_left = Button(self.__root, text=('TOL: ' + str(self.__tol_l)), fg='dark blue', bg ='white', font=('Times', int(0.03*self.__scr_w)),relief='flat', highlightthickness=0, command=self.__tol_l_down)
            self.__show_tol_right = Button(self.__root, text=('TOL: ' + str(self.__tol_r)), fg='dark red', bg ='white', font=('Times', int(0.03*self.__scr_w)), relief='flat', highlightthickness=0, command=self.__tol_r_down)
            self.__show_tol_left.place(relx=3/80, rely=23/32, relwidth=4/15, relheight=1/8)
            self.__show_tol_right.place(relx=167/240, rely=23/32, relwidth=4/15, relheight=1/8)
            self.__cache = [[0, 0, 0, 0, 2, 2, 'none']]
        else:
            self.__cache = [[0, 0, 0, 0, 'none']]
            
    def __start_bm(self, *event):
        """Starten der Anzeige für den Sport Badminton"""
        self.__team_left = self.__home.get()
        self.__team_right = self.__guest.get()
        self.__clear_tk()
        self.__root.title('Anzeige - Badminton')
        self.__is_timeouts = False
        self.__highest_points = int((10/7)*self.__points_sel)
        self.__show_points_left = Button(self.__root, text=str(self.__points_l), fg='dark blue', bg='white', anchor=E, font=('Times', int(0.15*self.__scr_w)), relief='flat', highlightthickness=0, command=self.__service_bm_left)
        self.__show_points_right = Button(self.__root, text=str(self.__points_r), fg='dark red', bg='white', anchor=W, font=('Times', int(0.15*self.__scr_w)), relief='flat', highlightthickness=0, command=self.__service_bm_right)
        self.__root.bind('l', self.__service_bm_left)
        self.__root.bind('r', self.__service_bm_right)
        self.__start_vb_bm_tt()
        self.__cache = [[0, 0, 0, 0, 'none']]
        
    def __start_tt(self, *event):
        """Starten der Anzeige für den Sport Tischtennis"""
        self.__team_left = self.__home.get()
        self.__team_right = self.__guest.get()
        if self.__points_sel < 21:
            self.__number_services = int(self.__points_sel/5)
        else:
            self.__number_services = int(self.__points_sel/4)
        self.__services = 0
        self.__clear_tk()
        self.__root.title('Anzeige - Tischtennis')
        self.__is_timeouts = False
        self.__show_points_left = Button(self.__root, text=str(self.__points_l), fg='dark blue', bg='white', anchor=E, font=('Times', int(0.15*self.__scr_w)), relief='flat', highlightthickness=0, command=self.__service_tt_left)
        self.__show_points_right = Button(self.__root, text=str(self.__points_r), fg='dark red', bg='white', anchor=W, font=('Times', int(0.15*self.__scr_w)), relief='flat', highlightthickness=0, command=self.__service_tt_right)
        self.__root.bind('l', self.__service_tt_left)
        self.__root.bind('r', self.__service_tt_right)
        self.__start_vb_bm_tt()
        self.__cache = [[0, 0, 0, 0, 'none']]

    def __start_vb_bm_tt(self):
        """Starten der Anzeige für die Sportarten Volleyball, Badminton und Tischtennis"""
        self.__root.bind('<Return>', self.__do_nothing)
        self.__games_l = 0
        self.__games_r = 0
        self.__service = 'none'
        self.__last_deleted = []
        self.__last_action = '-'
        self.__show_home = Label(self.__root, text=self.__team_left, fg='dark blue', bg='white', anchor=E, font=('Times', int(0.04*self.__scr_w)))
        self.__show_guest = Label(self.__root, text=self.__team_right, fg='dark red', bg='white', anchor=W, font=('Times', int(0.04*self.__scr_w)))
        self.__hyphen = Label(self.__root, text='-', bg='white', font=('Times', int(0.05*self.__scr_w)))
        self.__show_games_left = Message(self.__root, text=str(self.__games_l), fg='dark blue', bg='white', font=('Times', int(0.08*self.__scr_w)), relief='groove')
        self.__show_games_right = Message(self.__root, text=str(self.__games_r), fg='dark red', bg='white', font=('Times', int(0.08*self.__scr_w)), relief='groove')
        self.__colon = Label(self.__root, text=':', bg='white', font=('Times', int(0.15*self.__scr_w)), relief='flat')
        self.__show_service_left = Label(self.__root, text='', fg='dark blue', bg='white', font=('Times', int(0.1*self.__scr_w), 'bold'))
        self.__show_service_right = Label(self.__root, text='', fg='dark red', bg='white', font=('Times', int(0.1*self.__scr_w), 'bold'))
        self.__show_home.place(relx=1/64, rely=1/8, relwidth=147/320, relheight=1/8)
        self.__show_guest.place(relx=8/15, rely=1/8, relwidth=147/320, relheight=1/8)
        self.__hyphen.place(relx=19/40, rely=1/8, relwidth=1/20, relheight=1/10)
        self.__show_games_left.place(relx=41/120, rely=11/16, relwidth=1/8, relheight=3/16)
        self.__show_points_left.place(relx=13/60, rely=5/16, relwidth=1/4, relheight=5/16)
        self.__show_points_right.place(relx=8/15, rely=5/16, relwidth=1/4, relheight=5/16)
        self.__show_games_right.place(relx=8/15, rely=11/16, relwidth=1/8, relheight=3/16)
        self.__colon.place(relx=7/15, rely=5/16, relwidth=1/15, relheight=9/32)
        self.__show_service_left.place(relx=1/15, rely=5/16, relwidth=3/20, relheight=5/16)
        self.__show_service_right.place(relx=47/60, rely=5/16, relwidth=3/20, relheight=5/16)
        self.__root.bind('z', self.__step_back_vb_bm_tt)

    def __start_match(self, *event):
        """Starten der Spielzeit"""
        self.__pause()
        self.__pause()
        self.__root.bind('<space>', self.__pause)
        
    def __count(self):
        """Zählen der Spielzeit"""
        if self.__is_paused == False and self.__is_break == False and (self.__time_1 < self.__time_sel*60 or self.__sport == 'fb'):
            self.__time_1 = int(time() - self.__time_0 - self.__time_p)
            self.__time_passed()
            self.__show_time.after(50, self.__count)
        else:
            self.__phase_over()

    def __phase_over(self, *event):
        """Beenden eines Spielabschnitts"""
        if self.__time_1 >= self.__time_sel*60:
            if self.__sport == 'fb':
                self.__is_break = True
                self.__is_paused = True
                if self.__in_overtime == False:
                    __minutes = self.__time_sel * self.__phase
                else:
                    __minutes = self.__time_sel * self.__phase + self.__regular_time
                self.__time_1_layout = str(__minutes) + ':00'
            if self.__phase < self.__phases:
                self.__phase += 1
                if self.__in_overtime == False:
                    self.__show_phase.config(text=str(self.__phase))
                elif self.__in_second_overtime == False:
                    self.__show_phase.config(text='V' + str(self.__phase))
                else:
                    self.__show_phase.config(text='V' + str(self.__phase+2))
                if self.__sport == 'bb':
                    self.__time_1_layout = str(self.__time_sel) + ':00'
                    self.__tf_l = 0
                    self.__tf_r = 0
                    self.__show_tf_left.config(text='Fouls: ' + str(self.__tf_l))
                    self.__show_tf_right.config(text='Fouls: ' + str(self.__tf_r))
                    if self.__phase == 3:
                        self.__tol_l = 3
                        self.__tol_r = 3
                        self.__show_tol_left.config(text='TOL: ' + str(self.__tol_l))
                        self.__show_tol_right.config(text='TOL: ' + str(self.__tol_r))
                elif self.__sport == 'hb':
                    self.__time_1_layout = '0:00'
                self.__is_break = True
                self.__show_time.config(text=self.__time_1_layout)
                self.__pause()
            elif self.__in_overtime == False or (self.__sport == 'hb' and self.__in_second_overtime  == False):
                self.__root.bind('<space>', self.__do_nothing)
                self.__root.bind('v', self.__start_overtime)
            elif self.__in_penalty == False and (self.__sport == 'fb' or self.__sport == 'hb'):
                self.__root.bind('v', self.__start_penalty)
    
    def __pause(self, *event):
        """Pausieren oder Starten der Spielzeit"""
        if self.__is_break == True:
            self.__is_break = False
            self.__is_paused = True
            self.__time_p = -time()
            self.__time_0 = time()
            self.__time_1 = 0
            self.__root.bind('<space>', self.__pause)
        elif (self.__sport == 'bb' or self.__sport == 'hb'):
            if self.__is_paused == False:
                self.__is_paused = True
                self.__time_p -= time()
            else:
                self.__is_paused = False
                self.__time_p += time()
                self.__count()
        elif self.__is_paused == True:
            self.__is_paused = False
            self.__time_p += time()
            self.__count()
        
    def __time_passed(self):
        """Umrechnung des Wertes, der die vergangene Spielzeit anzeigt, in Minuten und Sekunden"""
        __minutes, __seconds = 0, self.__time_1
        while __seconds >= 60:
            __minutes += 1
            __seconds -= 60
        if self.__sport == 'fb':
            __minutes += (self.__phase-1)*self.__time_sel
            if self.__in_overtime == True:
                __minutes += self.__regular_time
        elif self.__sport == 'bb':
            __minutes = self.__time_sel - __minutes - 1
            __seconds = 60 - __seconds
            if __seconds == 60:
                __minutes += 1
                __seconds -= 60
        if ((self.__sport == 'hb' or self.__sport == 'bb') and __minutes <= self.__time_sel) or (self.__sport == 'fb' and ((self.__in_overtime == False and __minutes < self.__time_sel*self.__phase) or (self.__in_overtime == True and __minutes < (self.__time_sel*self.__phase+self.__regular_time)))):
            if __seconds >= 10:
                self.__time_1_layout = str(__minutes) + ':' + str(__seconds)
            else:
                self.__time_1_layout = str(__minutes) + ':0' + str(__seconds)
        elif self.__sport == 'fb' and self.__in_overtime == False:
            self.__root.bind('<space>', self.__phase_over)
            if __seconds >= 10:
                self.__time_1_layout = '+' + str(__minutes - (self.__time_sel*self.__phase)) + ':' + str(__seconds)
            else:
                self.__time_1_layout = '+' + str(__minutes - (self.__time_sel*self.__phase)) + ':0' + str(__seconds)
        elif self.__sport == 'fb' and self.__in_overtime == True:
            self.__root.bind('<space>', self.__phase_over)
            if __seconds >= 10:
                self.__time_1_layout = '+' + str(__minutes - self.__time_sel*self.__phase - self.__regular_time) + ':' + str(__seconds)
            else:
                self.__time_1_layout = '+' + str(__minutes - self.__time_sel*self.__phase - self.__regular_time) + ':0' + str(__seconds)
        if self.__last_time != self.__time_1_layout:
            self.__show_time.config(text=self.__time_1_layout)
        self.__last_time = self.__time_1_layout

    def __start_overtime(self, *event):
        """Starten einer Verlängerung"""
        self.__root.bind('<space>', self.__pause)
        self.__root.bind('v', self.__do_nothing)
        if self.__in_overtime == False:
            self.__in_overtime = True
            self.__in_second_overtime = False
        else:
            self.__in_second_overtime = True
        self.__phase = 0
        self.__regular_time = 2*self.__time_sel
        self.__time_sel = self.__overtime_sel
        if self.__sport == 'fb' or self.__sport == 'hb':
            self.__phases = 2
        else:
            self.__phases = 9
        self.__phase_over()
        self.__pause()

    def __start_penalty(self, *event):
        """Starten eines Elfmeterschießens / Siebenmeterwerfens"""
        self.__root.bind('v', self.__do_nothing)
        self.__in_penalty = True
        self.__time_1_layout = '0:00'
        self.__show_time.config(text=self.__time_1_layout)
        if self.__sport == 'fb':
            self.__show_phase.config(text='i.E.')
        elif self.__sport == 'hb':
            self.__show_phase.config(text='i.S.')
        self.__points_penalty_l = 0
        self.__points_penalty_r = 0
        self.__cache = [[0, 0]]
        self.__update_widgets_fb_bb_hb()
    
    def __add_point_fb_bb_hb_left(self, *event):
        """Hinzufügen eines Punktes / Tores im Fußball, Basketball oder Handball auf der linken Seite"""
        if self.__points_l < 999 and self.__in_penalty == False:
            self.__deleted_to_cache()
            self.__points_l += 1
            self.__update_widgets_fb_bb_hb()
            self.__add_to_cache_fb_bb_hb()
        elif self.__points_penalty_l < 99 and self.__in_penalty == True:
            self.__deleted_to_cache()
            self.__points_penalty_l += 1
            self.__update_widgets_fb_bb_hb()
            self.__add_to_cache_fb_bb_hb()
        
    def __add_point_fb_bb_hb_right(self, *event):
        """Hinzufügen eines Punktes / Tores im Fußball, Basketball oder Handball auf der rechten Seite"""
        if self.__points_r < 1000 and self.__in_penalty == False:
            self.__deleted_to_cache()
            self.__points_r += 1
            self.__show_points_right.config(text=str(self.__points_r))
            self.__add_to_cache_fb_bb_hb()
        elif self.__points_penalty_r < 99 and self.__in_penalty == True:
            self.__deleted_to_cache()
            self.__points_penalty_r += 1
            self.__update_widgets_fb_bb_hb()
            self.__add_to_cache_fb_bb_hb()
    
    def __add_point_vb_left(self):
        """Hinzufügen eines Punktes im Volleyball auf der linken Seite"""
        if (self.__games_l+self.__games_r) < (2*self.__games_sel-2):
            if self.__points_l >= (self.__points_sel-1) and self.__points_l > self.__points_r:
                self.__games_l += 1
                self.__points_l = 0
                self.__points_r = 0
                self.__service_vb_after_game()
                if self.__is_timeouts == True and self.__games_l < self.__games_sel and self.__games_r < self.__games_sel:
                    self.__tol_l = 2
                    self.__tol_r = 2
                    self.__show_tol_left.config(text=('TOL: ' + str(self.__tol_l)))
                    self.__show_tol_right.config(text=('TOL: ' + str(self.__tol_r)))
            else:
                self.__points_l += 1
        elif self.__points_l >= (self.__max_break-1) and self.__points_l > self.__points_r:
            self.__games_l += 1
            self.__points_l = 0
            self.__points_r = 0
            self.__service_vb_after_game()
        else:
            self.__points_l += 1
        self.__update_widgets_vb_bm_tt()
        
    def __add_point_vb_right(self):
        """Hinzufügen eines Punktes im Volleyball auf der rechten Seite"""
        if (self.__games_l+self.__games_r) < (2*self.__games_sel-2):
            if self.__points_r >= (self.__points_sel-1) and self.__points_r > self.__points_l:
                self.__games_r += 1
                self.__points_l = 0
                self.__points_r = 0
                self.__service_vb_after_game()
                if self.__is_timeouts == True and self.__games_l < self.__games_sel and self.__games_r < self.__games_sel:
                    self.__tol_l = 2
                    self.__tol_r = 2
                    self.__show_tol_left.config(text=('TOL: ' + str(self.__tol_l)))
                    self.__show_tol_right.config(text=('TOL: ' + str(self.__tol_r)))
            else:
                self.__points_r += 1
        elif self.__points_r >= (self.__max_break-1) and self.__points_r > self.__points_l:
            self.__games_r += 1
            self.__points_l = 0
            self.__points_r = 0
            self.__service_vb_after_game()
        else:
            self.__points_r += 1
        self.__update_widgets_vb_bm_tt()
        
    def __add_point_bm_left(self):
        """Hinzufügen eines Punktes im Badminton auf der linken Seite"""
        if self.__points_l >= (self.__points_sel-1) and (self.__points_l > self.__points_r or self.__points_l == (self.__highest_points-1)):
            self.__games_l += 1
            self.__points_l = 0
            self.__points_r = 0
            self.__service = 'left'
            if self.__games_l == self.__games_sel:
                self.__service = 'none'
        else:
            self.__points_l += 1
            self.__service = 'left'
        self.__update_widgets_vb_bm_tt()
                    
    def __add_point_bm_right(self):
        """Hinzufügen eines Punktes im Badminton auf der rechten Seite"""
        if self.__points_r >= (self.__points_sel-1) and (self.__points_r > self.__points_l or self.__points_r == (self.__highest_points-1)):
            self.__games_r += 1
            self.__points_l = 0
            self.__points_r = 0
            self.__service = 'right'
            if self.__games_r == self.__games_sel:
                self.__service = 'none'
        else:
            self.__points_r += 1
            self.__service = 'right'
        self.__update_widgets_vb_bm_tt()
        
    def __add_point_tt_left(self):
        """Hinzufügen eines Punktes im Tischtennis auf der linken Seite"""
        if self.__points_l >= (self.__points_sel-1) and self.__points_l > self.__points_r:
            self.__games_l += 1
            self.__points_l = 0
            self.__points_r = 0
        else:
            self.__points_l += 1
        self.__update_widgets_vb_bm_tt()
                    
    def __add_point_tt_right(self):
        """Hinzufügen eines Punktes im Tischtennis auf der rechten Seite"""
        if self.__points_r >= (self.__points_sel-1) and self.__points_r > self.__points_l:
            self.__games_r += 1
            self.__points_l = 0
            self.__points_r = 0
        else:
            self.__points_r += 1
        self.__update_widgets_vb_bm_tt()
        
    def __tol_l_down(self):
        """Abziehen eines übrigen Timeouts auf der linken Seite"""
        self.__deleted_to_cache()
        if self.__tol_l > 0:
            self.__tol_l -= 1
            self.__show_tol_left.config(text=('TOL: ' + str(self.__tol_l)))
            if self.__sport == 'vb':
                self.__add_to_cache_vb_bm_tt()
            else:
                self.__add_to_cache_fb_bb_hb()
        
    def __tol_r_down(self):
        """Abziehen eines übrigen Timeouts auf der rechten Seite"""
        self.__deleted_to_cache()
        if self.__tol_r > 0:
            self.__tol_r -= 1
            self.__show_tol_right.config(text=('TOL: ' + str(self.__tol_r)))
            if self.__sport == 'vb':
                self.__add_to_cache_vb_bm_tt()
            else:
                self.__add_to_cache_fb_bb_hb()

    def __tf_l_up(self):
        """Hinzufügen eines Teamfouls auf der linken Seite"""
        self.__deleted_to_cache()
        if self.__tf_l < 99:
            self.__tf_l += 1
            self.__show_tf_left.config(text=('Fouls: ' + str(self.__tf_l)))
            self.__add_to_cache_fb_bb_hb()
        
    def __tf_r_up(self):
        """Hinzufügen eines Teamfouls auf der rechten Seite"""
        self.__deleted_to_cache()
        if self.__tf_r < 99:
            self.__tf_r += 1
            self.__show_tf_right.config(text=('Fouls: ' + str(self.__tf_r)))
            self.__add_to_cache_fb_bb_hb()

    def __service_vb_left(self, *event):
        """Ändern des Aufschlagrechts im Volleyball auf links"""
        self.__deleted_to_cache()
        if self.__games_l < self.__games_sel and self.__games_r < self.__games_sel:
            if self.__service == 'none':
                self.__service_0 = 'left'
                self.__service = 'left'
            else:
                self.__service = 'left'
                self.__add_point_vb_left()
            self.__add_to_cache_vb_bm_tt()
            self.__update_show_service()

    def __service_vb_right(self, *event):
        """Ändern des Aufschlagrechts im Volleyball auf rechts"""
        self.__deleted_to_cache()
        if self.__games_l < self.__games_sel and self.__games_r < self.__games_sel:
            if self.__service == 'none':
                self.__service_0 = 'right'
                self.__service = 'right'
            else:
                self.__service = 'right'
                self.__add_point_vb_right()
            self.__add_to_cache_vb_bm_tt()
            self.__update_show_service()
    
    def __service_vb_after_game(self):
        """Ändern des Aufschlagrechts im Volleyball nach einem Satzgewinn"""
        if self.__games_l == self.__games_sel or self.__games_r == self.__games_sel:
            self.__service = 'none'
        elif (self.__games_l+self.__games_r) == (2*self.__games_sel-2):
            self.__service = 'none'
        elif self.__service_0 == 'left':
            self.__service_0 = 'right'
            self.__service = 'right'
        elif self.__service_0 == 'right':
            self.__service_0 = 'left'
            self.__service = 'left'
        self.__update_show_service()

    def __service_bm_left(self, *event):
        """Ändern des Aufschlagrechts im Badminton auf links"""
        self.__deleted_to_cache()
        if self.__games_l < self.__games_sel and self.__games_r < self.__games_sel:
            if self.__service == 'none':
                self.__service_0 = 'left'
                self.__service = 'left'
            else:
                self.__add_point_bm_left()
            self.__add_to_cache_vb_bm_tt()
            self.__update_show_service()

    def __service_bm_right(self, *event):
        """Ändern des Aufschlagrechts im Badminton auf rechts"""
        self.__deleted_to_cache()
        if self.__games_l < self.__games_sel and self.__games_r < self.__games_sel:
            if self.__service == 'none':
                self.__service_0 = 'right'
                self.__service = 'right'
            else:
                self.__add_point_bm_right()
            self.__add_to_cache_vb_bm_tt()
            self.__update_show_service()

    def __service_tt_left(self, *event):
        """Ändern des Aufschlagrechts im Tischtennis, wenn die linke Seite punktet"""
        self.__deleted_to_cache()
        if self.__games_l < self.__games_sel and self.__games_r < self.__games_sel:
            if self.__service == 'none':
                self.__service_0 = 'left'
                self.__service = 'left'
            else:
                self.__add_point_tt_left()
                self.__service_tt()
            self.__add_to_cache_vb_bm_tt()
            self.__update_show_service()

    def __service_tt_right(self, *event):
        """Ändern des Aufschlagrechts im Tischtennis, wenn die rechte Seite punktet"""
        self.__deleted_to_cache()
        if self.__games_l < self.__games_sel and self.__games_r < self.__games_sel:
            if self.__service == 'none':
                self.__service_0 = 'right'
                self.__service = 'right'
            else:
                self.__add_point_tt_right()
                self.__service_tt()
            self.__add_to_cache_vb_bm_tt()
            self.__update_show_service()

    def __service_tt(self):
        """Ändern des Aufschlagrechts im Tischtennis"""
        if (self.__points_l+self.__points_r) > 0:
            if (self.__points_l+self.__points_r) < (2*self.__points_sel-2):
                if self.__services < self.__number_services-1:
                    self.__services += 1
                elif self.__service == 'left':
                    self.__service = 'right'
                    self.__services = 0
                else:
                    self.__service = 'left'
                    self.__services = 0
            elif self.__service == 'left':
                self.__service = 'right'
            else:
                self.__service = 'left'
        elif self.__service_0 == 'left':
            self.__service_0 = 'right'
            self.__service = 'right'
        else:
            self.__service_0 = 'left'
            self.__service = 'left'
        if self.__games_l == self.__games_sel or self.__games_r == self.__games_sel:
            self.__service = 'none'

    def __update_show_service(self):
        """Aktualisieren der Anzeigen für das Aufschlagrecht"""
        if self.__service == 'none':
            self.__show_service_left.config(text='')
            self.__show_service_right.config(text='')
        elif self.__service == 'left':
            self.__show_service_left.config(text='<')
            self.__show_service_right.config(text='')
        elif self.__service == 'right':
            self.__show_service_left.config(text='')
            self.__show_service_right.config(text='>')
        
    def __add_to_cache_fb_bb_hb(self):
        """Hinzufügen der aktuellen Spielwerte (außer Spielzeit) in eine Liste im Fußball, Basketball und Handball"""
        if self.__in_penalty == False:
            if self.__is_teamfouls == True and self.__is_timeouts == True:
                self.__cache.append([self.__points_l, self.__points_r, self.__tol_l, self.__tol_r, self.__tf_l, self.__tf_r])
            elif self.__is_teamfouls == True and self.__is_timeouts == False:
                self.__cache.append([self.__points_l, self.__points_r, self.__tf_l, self.__tf_r])
            elif self.__is_teamfouls == False and self.__is_timeouts == True:
                self.__cache.append([self.__points_l, self.__points_r, self.__tol_l, self.__tol_r])
            else:
                self.__cache.append([self.__points_l, self.__points_r])
        else:
            self.__cache.append([self.__points_l, self.__points_r, self.__points_penalty_l, self.__points_penalty_r])
            
    def __add_to_cache_vb_bm_tt(self):
        """Hinzufügen der aktuellen Spielwerte in eine Liste im Volleyball, Badminton und Tischtennis"""
        if self.__is_timeouts == True:
            self.__cache.append([self.__points_l, self.__points_r, self.__games_l, self.__games_r, self.__tol_l, self.__tol_r, self.__service])
        else:
            self.__cache.append([self.__points_l, self.__points_r, self.__games_l, self.__games_r, self.__service])
            
    def __step_back_fb_bb_hb(self, *event):
        """Rückgängigmachen des letzten Schrittes während Laufens der Anzeigetafel im Fußball, Basketball und Handball"""
        def __step_back():
            if len(self.__cache) > 0:
                __last_stats = self.__cache.pop()
                self.__last_deleted = __last_stats[:]
                if self.__in_penalty == False:
                    if self.__is_teamfouls == True and self.__is_timeouts == True:
                        self.__tf_r = __last_stats.pop()
                        self.__tf_l = __last_stats.pop()
                        self.__tol_r = __last_stats.pop()
                        self.__tol_l = __last_stats.pop()
                        self.__points_r = __last_stats.pop()
                        self.__points_l = __last_stats.pop()
                    elif self.__is_teamfouls == True and self.__is_timeouts == False:
                        self.__tf_r = __last_stats.pop()
                        self.__tf_l = __last_stats.pop()
                        self.__points_r = __last_stats.pop()
                        self.__points_l = __last_stats.pop()
                    elif self.__is_teamfouls == False and self.__is_timeouts == True:
                        self.__tol_r = __last_stats.pop()
                        self.__tol_l = __last_stats.pop()
                        self.__points_r = __last_stats.pop()
                        self.__points_l = __last_stats.pop()
                    else:
                        self.__points_r = __last_stats.pop()
                        self.__points_l = __last_stats.pop()
                else:
                    self.__points_penalty_r = __last_stats.pop()
                    self.__points_penalty_l = __last_stats.pop()
                self.__update_widgets_fb_bb_hb()
        if self.__last_action == '+':
            __step_back()
            __step_back()
        else:
            __step_back()
        self.__last_action = '-'
            
    def __step_back_vb_bm_tt(self, *event):
        """Rückgängigmachen des letzten Schrittes während Laufens der Anzeigetafel im Volleyball, Badminton und Tischtennis"""
        def __step_back():
            if len(self.__cache) > 0:
                __last_stats = self.__cache.pop()
                self.__last_deleted = __last_stats[:]
                if self.__is_timeouts == True:
                    self.__service = __last_stats.pop()
                    self.__tol_r = __last_stats.pop()
                    self.__tol_l = __last_stats.pop()
                    self.__games_r = __last_stats.pop()
                    self.__games_l = __last_stats.pop()
                    self.__points_r = __last_stats.pop()
                    self.__points_l = __last_stats.pop()
                else:
                    self.__service = __last_stats.pop()
                    self.__games_r = __last_stats.pop()
                    self.__games_l = __last_stats.pop()
                    self.__points_r = __last_stats.pop()
                    self.__points_l = __last_stats.pop()
                self.__update_widgets_vb_bm_tt()
        if self.__last_action == '+':
            __step_back()
            __step_back()
        else:
            __step_back()
        self.__last_action = '-'

    def __deleted_to_cache(self):
        """Hinzufügen des zuletzt gelöschten Wertes zur Liste der gelöschten Werte"""
        if len(self.__last_deleted) > 0:
            self.__cache.append(self.__last_deleted)
            self.__last_deleted = []
        self.__last_action = '+'
        
    def __update_widgets_fb_bb_hb(self):
        """Aktualisieren der Anzeige im Fußball, Basketball und Handball"""
        if self.__in_penalty == False:
            self.__show_points_left.config(text=str(self.__points_l))
            self.__show_points_right.config(text=str(self.__points_r))
        else:
            self.__show_points_left.config(text=str(self.__points_penalty_l))
            self.__show_points_right.config(text=str(self.__points_penalty_r))
        if self.__is_timeouts == True:
            self.__show_tol_left.config(text='TOL: ' + str(self.__tol_l))
            self.__show_tol_right.config(text='TOL: ' + str(self.__tol_r))
        if self.__is_teamfouls == True:
            self.__show_tf_left.config(text='Fouls: ' + str(self.__tf_l))
            self.__show_tf_right.config(text='Fouls: ' + str(self.__tf_r))
        
    def __update_widgets_vb_bm_tt(self):
        """Aktualisieren der Anzeige im Volleyball, Badminton und Tischtennis"""
        self.__show_points_left.config(text=str(self.__points_l))
        self.__show_points_right.config(text=str(self.__points_r))
        self.__show_games_left.config(text=str(self.__games_l))
        self.__show_games_right.config(text=str(self.__games_r))
        if self.__is_timeouts == True:
            self.__show_tol_left.config(text='TOL: ' + str(self.__tol_l))
            self.__show_tol_right.config(text='TOL: ' + str(self.__tol_r))
        if self.__service == 'none':
            self.__show_service_left.config(text='')
            self.__show_service_right.config(text='')
        elif self.__service == 'left':
            self.__show_service_left.config(text='<')
            self.__show_service_right.config(text='')
        elif self.__service == 'right':
            self.__show_service_left.config(text='')
            self.__show_service_right.config(text='>')
        
__anzeige = __Anzeige()