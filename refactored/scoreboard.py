from time import time
from tkinter import *


class Anzeige:

    def __init__(self, root: Tk):
        self.__games_sel = 0
        self.__points_sel = 0
        self.__time_sel = 0
        self.__overtime_sel = 0
        self.__use_timeouts = True
        self.__use_team_fouls = True
        self.__points = {'l': 0, 'r': 0}
        self.__root = root
        self.__root.title('Auswahl der Sportart')
        self.__root.config(bg='white')
        self.__scr_w = self.__root.winfo_screenwidth()
        self.__scr_h = self.__root.winfo_screenheight()
        self.__root.geometry(f'{self.__scr_w}x{self.__scr_h}')
        self.__in_fullscreen = False
        self.__root.bind('<Alt-Return>', lambda _: self.__toggle_fullscreen())
        self.__select_sport()

    def __toggle_fullscreen(self):
        if self.__in_fullscreen:
            self.__root.attributes('-fullscreen', False)
        else:
            self.__root.attributes('-fullscreen', True)
        self.__in_fullscreen = not self.__in_fullscreen

    def __clear_tk(self):
        """Löschen der mit '.place()' platzierten Widgets aus dem Interface"""
        for widget in self.__root.place_slaves():
            widget.destroy()

    def __select_sport(self):
        """Erzeugen der Widgets im Startmenü zum Auswählen einer Sportart"""
        self.__button_fb = Button(self.__root, text='Fußball', command=self.__select_fb)
        self.__button_bb = Button(self.__root, text='Basketball', command=self.__select_bb)
        self.__button_hb = Button(self.__root, text='Handball', command=self.__select_hb)
        self.__button_vb = Button(self.__root, text='Volleyball', command=self.__select_vb)
        self.__button_bm = Button(self.__root, text='Badminton', command=self.__select_bm)
        self.__button_tt = Button(self.__root, text='Tischtennis', command=self.__select_tt)
        self.__button_fb.place(relx=0, rely=0, relwidth=1 / 2, relheight=1 / 3)
        self.__button_bb.place(relx=0, rely=1 / 3, relwidth=1 / 2, relheight=1 / 3)
        self.__button_hb.place(relx=0, rely=2 / 3, relwidth=1 / 2, relheight=1 / 3)
        self.__button_vb.place(relx=1 / 2, rely=0, relwidth=1 / 2, relheight=1 / 3)
        self.__button_bm.place(relx=1 / 2, rely=1 / 3, relwidth=1 / 2, relheight=1 / 3)
        self.__button_tt.place(relx=1 / 2, rely=2 / 3, relwidth=1 / 2, relheight=1 / 3)
        for widget in self.__root.place_slaves():
            widget.config(bg='white', font=('Times', int(0.04 * self.__scr_w)), relief='groove')

    def __change_games_sel(self, x: int):
        """Ändern der ausgewählten Sätze um x"""
        self.__games_sel += x
        self.__games_sel = min(self.__points_sel, 9)
        self.__games_sel = max(self.__points_sel, 1)
        self.__games_msg.config(text=f'Sätze zum Sieg: {self.__games_sel}')

    def __change_points_sel(self, x: int):
        """Ändern der ausgewählten Punkte um x"""
        self.__points_sel += x
        self.__points_sel = min(self.__points_sel, 99)
        self.__points_sel = max(self.__points_sel, 5)
        self.__points_msg.config(text=f'Punkte zum Satz: {self.__points_sel}')

    def __change_time_sel(self, x: int):
        """Ändern der ausgewählten Zeit um x"""
        self.__time_sel += x
        self.__time_sel = min(self.__time_sel, 60)
        self.__time_sel = max(self.__time_sel, 1)
        self.__time_msg.config(text=f'Zeit pro Abschnitt: {self.__time_sel} Minuten')

    def __change_overtime_sel(self, x: int):
        """Ändern der ausgewählten Zeit in der Verlängerung um x"""
        self.__overtime_sel += x
        self.__overtime_sel = min(self.__overtime_sel, 60)
        self.__overtime_sel = max(self.__overtime_sel, 1)
        self.__overtime_msg.config(text=f'Zeit pro Abschnitt in der Verlängerung: {self.__overtime_sel} Minuten')

    def __change_use_timeouts(self):
        """Auswahl, ob man mit oder ohne Timeouts spielen möchte"""
        self.__use_timeouts = not self.__use_timeouts
        if self.__use_timeouts:
            self.__ask_timeouts.config(text='Timeouts: an', bg='yellowgreen')
        else:
            self.__ask_timeouts.config(text='Timeouts: aus', bg='orangered')

    def __change_use_teamfouls(self):
        """Auswahl, ob man mit oder ohne Teamfouls spielen möchte"""
        self.__use_team_fouls = not self.__use_team_fouls
        if self.__use_team_fouls:
            self.__ask_teamfouls.config(text='Teamfouls: an', bg='yellowgreen')
        else:
            self.__ask_teamfouls.config(text='Teamfouls: aus', bg='orangered')

    def __select_fb(self):
        """Starten eines Menüs für den Sport Fußball, um Teamnamen und Spielzeiten festzulegen"""
        self.__clear_tk()
        self.__root.title('Auswahl - Fußball')
        self.__sport = 'fb'
        self.__time_sel = 45
        self.__overtime_sel = 15
        self.__ready = Button(self.__root, text='go', fg='white', bg='black', font=('Times', int(0.015 * self.__scr_w)),
                              relief='groove', command=self.__start_fb)
        self.__sel_fb_bb_hb()
        self.__root.bind('<Return>', lambda _: self.__start_fb())

    def __select_bb(self):
        """Starten eines Menüs für den Sport Basketball, um Teamnamen,
        Spielzeiten, Timeouts und Teamfouls festzulegen"""
        self.__clear_tk()
        self.__root.title('Auswahl - Basketball')
        self.__sport = 'bb'
        self.__time_sel = 10
        self.__overtime_sel = 5
        self.__ready = Button(self.__root, text='go', fg='white', bg='black', font=('Times', int(0.015 * self.__scr_w)),
                              relief='groove', command=self.__start_bb)
        self.__ask_timeouts = Button(self.__root, text='Timeouts: an', bg='yellowgreen', justify='center',
                                     font=('Times', int(0.025 * self.__scr_w)), relief='groove',
                                     command=self.__change_use_timeouts)
        self.__ask_teamfouls = Button(self.__root, text='Teamfouls: an', bg='yellowgreen', justify='center',
                                      font=('Times', int(0.025 * self.__scr_w)), relief='groove',
                                      command=self.__change_use_teamfouls)
        self.__sel_fb_bb_hb()
        self.__ask_timeouts.place(relx=3 / 20, rely=3 / 4, relwidth=7 / 20, relheight=1 / 8)
        self.__ask_teamfouls.place(relx=1 / 2, rely=3 / 4, relwidth=7 / 20, relheight=1 / 8)
        self.__root.bind('<Return>', lambda _: self.__start_bb())

    def __select_hb(self):
        """Starten eines Menüs für den Sport Basketball, um Teamnamen, Spielzeiten und Timeouts festzulegen"""
        self.__clear_tk()
        self.__root.title('Auswahl - Handball')
        self.__sport = 'hb'
        self.__time_sel = 30
        self.__overtime_sel = 5
        self.__ready = Button(self.__root, text='go', fg='white', bg='black', font=('Times', int(0.015 * self.__scr_w)),
                              relief='groove', command=self.__start_hb)
        self.__ask_timeouts = Button(self.__root, text='Timeouts: an', bg='yellowgreen', justify='center',
                                     font=('Times', int(0.025 * self.__scr_w)), relief='groove',
                                     command=self.__change_use_timeouts)
        self.__sel_fb_bb_hb()
        self.__ask_timeouts.place(relx=3 / 20, rely=3 / 4, relwidth=7 / 10, relheight=1 / 8)
        self.__root.bind('<Return>', lambda _: self.__start_hb())

    def __sel_fb_bb_hb(self):
        """Erzeugen und Platzieren der Widgets für das Auswahlmenü, die im Fußball,
        Basketball und Handball identisch sind"""
        self.__time_msg = Message(self.__root, text=f'Zeit pro Abschnitt: {self.__time_sel} Minuten', bg='light gray',
                                  justify='center', font=('Times', int(0.02 * self.__scr_w)), relief='groove')
        self.__time_down = Button(self.__root, text='-1', bg='orangered', font=('Times', int(0.025 * self.__scr_w)),
                                  relief='groove', command=lambda: self.__change_time_sel(-1))
        self.__time_up = Button(self.__root, text='+1', bg='yellowgreen', font=('Times', int(0.025 * self.__scr_w)),
                                relief='groove', command=lambda: self.__change_time_sel(1))
        self.__time_ten_down = Button(self.__root, text='-10', bg='orangered',
                                      font=('Times', int(0.025 * self.__scr_w)), relief='groove',
                                      command=lambda: self.__change_time_sel(-10))
        self.__time_ten_up = Button(self.__root, text='+10', bg='yellowgreen',
                                    font=('Times', int(0.025 * self.__scr_w)), relief='groove',
                                    command=lambda: self.__change_time_sel(10))
        self.__overtime_msg = Message(self.__root,
                                      text=f'Zeit je Abschnitt in der Verlängerung: {self.__overtime_sel} Minuten',
                                      bg='light gray', justify='center',
                                      font=('Times', int(0.02 * self.__scr_w)), relief='groove')
        self.__overtime_down = Button(self.__root, text='-1', bg='orangered', font=('Times', int(0.025 * self.__scr_w)),
                                      relief='groove', command=lambda: self.__change_overtime_sel(-1))
        self.__overtime_up = Button(self.__root, text='+1', bg='yellowgreen', font=('Times', int(0.025 * self.__scr_w)),
                                    relief='groove', command=lambda: self.__change_overtime_sel(1))
        self.__overtime_ten_down = Button(self.__root, text='-10', bg='orangered',
                                          font=('Times', int(0.025 * self.__scr_w)), relief='groove',
                                          command=lambda: self.__change_overtime_sel(-10))
        self.__overtime_ten_up = Button(self.__root, text='+10', bg='yellowgreen',
                                        font=('Times', int(0.025 * self.__scr_w)), relief='groove',
                                        command=lambda: self.__change_overtime_sel(10))
        self.__home = Entry(self.__root, justify='center', font=('Times', int(0.025 * self.__scr_w)))
        self.__guest = Entry(self.__root, justify='center', font=('Times', int(0.025 * self.__scr_w)))
        self.__home.insert(0, 'Heim')
        self.__guest.insert(0, 'Gast')
        self.__time_msg.place(relx=1 / 4, rely=1 / 4, relwidth=1 / 2, relheight=1 / 4)
        self.__time_down.place(relx=3 / 20, rely=1 / 4, relwidth=1 / 10, relheight=1 / 8)
        self.__time_up.place(relx=3 / 4, rely=1 / 4, relwidth=1 / 10, relheight=1 / 8)
        self.__time_ten_down.place(relx=3 / 20, rely=3 / 8, relwidth=1 / 10, relheight=1 / 8)
        self.__time_ten_up.place(relx=3 / 4, rely=3 / 8, relwidth=1 / 10, relheight=1 / 8)
        self.__overtime_msg.place(relx=1 / 4, rely=1 / 2, relwidth=1 / 2, relheight=1 / 4)
        self.__overtime_down.place(relx=3 / 20, rely=1 / 2, relwidth=1 / 10, relheight=1 / 8)
        self.__overtime_up.place(relx=3 / 4, rely=1 / 2, relwidth=1 / 10, relheight=1 / 8)
        self.__overtime_ten_down.place(relx=3 / 20, rely=5 / 8, relwidth=1 / 10, relheight=1 / 8)
        self.__overtime_ten_up.place(relx=3 / 4, rely=5 / 8, relwidth=1 / 10, relheight=1 / 8)
        self.__ready.place(x=11 / 12 * self.__scr_w - 10, y=9 / 10 * self.__scr_h - 10, width=1 / 12 * self.__scr_w,
                           height=1 / 10 * self.__scr_h)
        self.__home.place(relx=3 / 20, rely=1 / 8, relwidth=7 / 20, relheight=1 / 8)
        self.__guest.place(relx=1 / 2, rely=1 / 8, relwidth=7 / 20, relheight=1 / 8)

    def __select_vb(self):
        """Starten eines Menüs für den Sport Volleyball, um Teamnamen, Sätze, Punkte und Timeouts festzulegen"""
        self.__clear_tk()
        self.__root.title('Auswahl - Volleyball')
        self.__sport = 'vb'
        self.__games_sel = 3
        self.__points_sel = 25
        self.__ready = Button(self.__root, text='go', fg='white', bg='black', font=('Times', int(0.015 * self.__scr_w)),
                              relief='groove', command=self.__start_vb)
        self.__ask_timeouts = Button(self.__root, text='Timeouts: an', bg='yellowgreen', justify='center',
                                     font=('Times', int(0.025 * self.__scr_w)), relief='groove',
                                     command=self.__change_use_timeouts)
        self.__sel_vb_bm_tt()
        self.__ask_timeouts.place(relx=3 / 20, rely=3 / 4, relwidth=7 / 10, relheight=1 / 8)
        self.__root.bind('<Return>', lambda _: self.__start_vb())

    def __select_bm(self):
        """Starten eines Menüs für den Sport Badminton, um Teamnamen, Sätze und Punkte festzulegen"""
        self.__clear_tk()
        self.__root.title('Auswahl - Badminton')
        self.__sport = 'bm'
        self.__games_sel = 2
        self.__points_sel = 21
        self.__ready = Button(self.__root, text='go', fg='white', bg='black', font=('Times', int(0.015 * self.__scr_w)),
                              relief='groove', command=self.__start_bm)
        self.__sel_vb_bm_tt()
        self.__root.bind('<Return>', lambda _: self.__start_bm())

    def __select_tt(self):
        """Starten eines Menüs für den Sport Tischtennis, um Teamnamen, Sätze und Punkte festzulegen"""
        self.__clear_tk()
        self.__root.title('Auswahl - Tischtennis')
        self.__sport = 'tt'
        self.__games_sel = 2
        self.__points_sel = 11
        self.__ready = Button(self.__root, text='go', fg='white', bg='black', font=('Times', int(0.015 * self.__scr_w)),
                              relief='groove', command=self.__start_tt)
        self.__sel_vb_bm_tt()
        self.__root.bind('<Return>', lambda _: self.__start_tt())

    def __sel_vb_bm_tt(self):
        """Erzeugen und Platzieren der Widgets für das Auswahlmenü, die im
        Volleyball, Badminton und Tischtennis identisch sind"""
        self.__games_msg = Message(self.__root, text=f'Sätze zum Sieg: {self.__games_sel}', bg='light gray',
                                   justify='center', font=('Times', int(0.025 * self.__scr_w)), relief='groove')
        self.__games_down = Button(self.__root, text='-1', bg='orangered', font=('Times', int(0.025 * self.__scr_w)),
                                   relief='groove', command=lambda: self.__change_games_sel(-1))
        self.__games_up = Button(self.__root, text='+1', bg='yellowgreen', font=('Times', int(0.025 * self.__scr_w)),
                                 relief='groove', command=lambda: self.__change_games_sel(1))
        self.__points_msg = Message(self.__root, text=f'Punkte zum Satz: {self.__points_sel}', bg='light gray',
                                    justify='center', font=('Times', int(0.025 * self.__scr_w)), relief='groove')
        self.__points_down = Button(self.__root, text='-1', bg='orangered', font=('Times', int(0.025 * self.__scr_w)),
                                    relief='groove', command=lambda: self.__change_points_sel(-1))
        self.__points_up = Button(self.__root, text='+1', bg='yellowgreen', font=('Times', int(0.025 * self.__scr_w)),
                                  relief='groove', command=lambda: self.__change_points_sel(1))
        self.__points_ten_down = Button(self.__root, text='-10', bg='orangered',
                                        font=('Times', int(0.025 * self.__scr_w)), relief='groove',
                                        command=lambda: self.__change_points_sel(-10))
        self.__points_ten_up = Button(self.__root, text='+10', bg='yellowgreen',
                                      font=('Times', int(0.025 * self.__scr_w)), relief='groove',
                                      command=lambda: self.__change_points_sel(10))
        self.__home = Entry(self.__root, justify='center', font=('Times', int(0.025 * self.__scr_w)))
        self.__guest = Entry(self.__root, justify='center', font=('Times', int(0.025 * self.__scr_w)))
        self.__home.insert(0, 'Heim')
        self.__guest.insert(0, 'Gast')
        self.__games_msg.place(relx=1 / 4, rely=1 / 4, relwidth=1 / 2, relheight=1 / 4)
        self.__games_down.place(relx=3 / 20, rely=1 / 4, relwidth=1 / 10, relheight=1 / 4)
        self.__games_up.place(relx=3 / 4, rely=1 / 4, relwidth=1 / 10, relheight=1 / 4)
        self.__points_msg.place(relx=1 / 4, rely=1 / 2, relwidth=1 / 2, relheight=1 / 4)
        self.__points_down.place(relx=3 / 20, rely=1 / 2, relwidth=1 / 10, relheight=1 / 8)
        self.__points_up.place(relx=3 / 4, rely=1 / 2, relwidth=1 / 10, relheight=1 / 8)
        self.__points_ten_down.place(relx=3 / 20, rely=5 / 8, relwidth=1 / 10, relheight=1 / 8)
        self.__points_ten_up.place(relx=3 / 4, rely=5 / 8, relwidth=1 / 10, relheight=1 / 8)
        self.__home.place(relx=3 / 20, rely=1 / 8, relwidth=7 / 20, relheight=1 / 8)
        self.__guest.place(relx=1 / 2, rely=1 / 8, relwidth=7 / 20, relheight=1 / 8)
        self.__ready.place(x=11 / 12 * self.__scr_w - 10, y=9 / 10 * self.__scr_h - 10, width=1 / 12 * self.__scr_w,
                           height=1 / 10 * self.__scr_h)

    def __start_fb(self):
        """Starten der Anzeige für den Sport Fußball"""
        self.__team_left = self.__home.get()
        self.__team_right = self.__guest.get()
        self.__clear_tk()
        self.__root.title('Anzeige - Fußball')
        self.__use_timeouts = False
        self.__use_team_fouls = False
        self.__phases = 2
        self.__start_fb_bb_hb()
        self.__history = [[self.__points]]

    def __start_bb(self):
        """Starten der Anzeige für den Sport Basketball"""
        self.__team_left = self.__home.get()
        self.__team_right = self.__guest.get()
        self.__clear_tk()
        self.__root.title('Anzeige - Basketball')
        self.__phases = 4
        self.__time_1_layout = f'{self.__time_sel}:00'
        self.__start_fb_bb_hb()
        if self.__use_team_fouls:
            self.__tf = {'l': 0, 'r': 0}
            show_tf_left = Button(self.__root, text='Fouls: %d' % self.__tf['l'], fg='dark blue', bg='white',
                                  font=('Times', int(0.03 * self.__scr_w)), relief='flat', highlightthickness=0,
                                  command=lambda: self.__tf_up('l'))
            show_tf_right = Button(self.__root, text='Fouls: %d' % self.__tf['r'], fg='dark red', bg='white',
                                   font=('Times', int(0.03 * self.__scr_w)), relief='flat', highlightthickness=0,
                                   command=lambda: self.__tf_up('r'))
            show_tf_left.place(relx=7 / 120, rely=5 / 8, relwidth=1 / 6, relheight=1 / 8)
            show_tf_right.place(relx=31 / 40, rely=5 / 8, relwidth=1 / 6, relheight=1 / 8)
            self.__show_tf = {'l': show_tf_left, 'r': show_tf_right}
        if self.__use_timeouts:
            self.__tol = {'l': 2, 'r': 2}
            show_tol_left = Button(self.__root, text='TOL: %d' % self.__tol['l'], fg='dark blue', bg='white',
                                   font=('Times', int(0.03 * self.__scr_w)), relief='flat', highlightthickness=0,
                                   command=lambda: self.__tol_down('l'))
            show_tol_right = Button(self.__root, text='TOL: %d' % self.__tol['r'], fg='dark red', bg='white',
                                    font=('Times', int(0.03 * self.__scr_w)), relief='flat',
                                    highlightthickness=0, command=lambda: self.__tol_down('r'))
            show_tol_left.place(relx=7 / 120, rely=3 / 4, relwidth=1 / 6, relheight=1 / 8)
            show_tol_right.place(relx=31 / 40, rely=3 / 4, relwidth=1 / 6, relheight=1 / 8)
            self.__show_tol = {'l': show_tol_left, 'r': show_tol_right}
        if self.__use_team_fouls and self.__use_timeouts:
            self.__history = [[self.__points, self.__tol, self.__tf]]
        elif self.__use_team_fouls and not self.__use_timeouts:
            self.__history = [[self.__points, self.__tf]]
        elif not self.__use_team_fouls and self.__use_timeouts:
            self.__history = [[self.__points, self.__tol]]
        else:
            self.__history = [[self.__points]]

    def __start_hb(self):
        """Starten der Anzeige für den Sport Handball"""
        self.__team_left = self.__home.get()
        self.__team_right = self.__guest.get()
        self.__clear_tk()
        self.__root.title('Anzeige - Handball')
        self.__use_team_fouls = False
        self.__phases = 2
        self.__start_fb_bb_hb()
        if self.__use_timeouts:
            self.__tol['l'] = self.__tol['r'] = 3
            self.__show_tol_left = Button(self.__root, text='TOL: %d' % self.__tol['l'], fg='dark blue', bg='white',
                                          font=('Times', int(0.03 * self.__scr_w)), relief='flat', highlightthickness=0,
                                          command=lambda: self.__tol_down('l'))
            self.__show_tol_right = Button(self.__root, text='TOL: %d' % self.__tol['r'], fg='dark red', bg='white',
                                           font=('Times', int(0.03 * self.__scr_w)), relief='flat',
                                           highlightthickness=0, command=lambda: self.__tol_down('r'))
            self.__show_tol_left.place(relx=7 / 120, rely=11 / 16, relwidth=1 / 6, relheight=1 / 8)
            self.__show_tol_right.place(relx=31 / 40, rely=11 / 16, relwidth=1 / 6, relheight=1 / 8)
            self.__history = [[self.__points, self.__tol]]
        else:
            self.__history = [[self.__points]]

    def __start_fb_bb_hb(self):
        """Starten der Anzeige für die Sportarten Fußball, Basketball und Handball"""
        self.__root.unbind('<Return>')
        self.__phase = 1
        self.__last_deleted = []
        self.__last_action = '-'
        if self.__sport in ['fb', 'hb']:
            self.__time_1_layout = '0:00'
        elif self.__sport == 'bb':
            self.__time_1_layout = f'{self.__time_sel}:00'
        self.__is_paused = True
        self.__is_break = True
        self.__show_points_left = Button(self.__root, text=str(self.__points['l']), fg='dark blue', bg='white',
                                         anchor=E,
                                         font=('Times', int(0.115 * self.__scr_w)), relief='flat', highlightthickness=0,
                                         command=lambda: self.__add_point_fb_bb_hb('l'))
        self.__show_points_right = Button(self.__root, text=str(self.__points['r']), fg='dark red', bg='white',
                                          anchor=W,
                                          font=('Times', int(0.115 * self.__scr_w)), relief='flat',
                                          highlightthickness=0, command=lambda: self.__add_point_fb_bb_hb('r'))
        self.__root.bind('l', lambda _: self.__add_point_fb_bb_hb('l'))
        self.__root.bind('r', lambda _: self.__add_point_fb_bb_hb('r'))
        self.__colon = Label(self.__root, text=':', bg='white', font=('Times', int(0.115 * self.__scr_w)))
        self.__show_phase = Label(self.__root, text='1', bg='white', font=('Times', int(0.025 * self.__scr_w)),
                                  relief='groove')
        self.__show_time = Label(self.__root, text=self.__time_1_layout, bg='white',
                                 font=('Times', int(0.075 * self.__scr_w)), relief='groove')
        self.__show_home = Label(self.__root, text=self.__team_left, fg='dark blue', bg='white', anchor=E,
                                 font=('Times', int(0.04 * self.__scr_w)))
        self.__show_guest = Label(self.__root, text=self.__team_right, fg='dark red', bg='white', anchor=W,
                                  font=('Times', int(0.04 * self.__scr_w)))
        self.__hyphen = Label(self.__root, text='-', bg='white', font=('Times', int(0.05 * self.__scr_w)))
        self.__show_points_left.place(relx=9 / 40, rely=7 / 12, relwidth=1 / 4, relheight=5 / 16)
        self.__show_points_right.place(relx=21 / 40, rely=7 / 12, relwidth=1 / 4, relheight=5 / 16)
        self.__colon.place(relx=19 / 40, rely=7 / 12, relwidth=1 / 20, relheight=9 / 32)
        self.__show_phase.place(relx=14 / 30, rely=1 / 16, relwidth=1 / 15, relheight=1 / 15)
        self.__show_time.place(relx=3 / 8, rely=1 / 8, relwidth=1 / 4, relheight=1 / 6)
        self.__show_home.place(relx=1 / 64, rely=5 / 12, relwidth=147 / 320, relheight=1 / 8)
        self.__show_guest.place(relx=21 / 40, rely=5 / 12, relwidth=147 / 320, relheight=1 / 8)
        self.__hyphen.place(relx=19 / 40, rely=5 / 12, relwidth=1 / 20, relheight=1 / 10)
        self.__time_0 = time()
        self.__time_1 = 0
        self.__time_p = 0
        self.__last_time = ''
        self.__in_overtime = False
        self.__in_penalty = False
        self.__count()
        self.__root.bind('<space>', lambda _: self.__start_match())
        self.__root.bind('z', lambda _: self.__step_back_fb_bb_hb())

    def __start_vb(self):
        """Starten der Anzeige für den Sport Volleyball"""
        self.__team_left = self.__home.get()
        self.__team_right = self.__guest.get()
        self.__clear_tk()
        self.__root.title('Anzeige - Volleyball')
        self.__max_break = int(3 / 5 * self.__points_sel)
        self.__show_points_left = Button(self.__root, text=str(self.__points['l']), fg='dark blue', bg='white',
                                         anchor=E,
                                         font=('Times', int(0.15 * self.__scr_w)), relief='flat', highlightthickness=0,
                                         command=lambda: self.__service_vb('l'))
        self.__show_points_right = Button(self.__root, text=str(self.__points['r']), fg='dark red', bg='white',
                                          anchor=W,
                                          font=('Times', int(0.15 * self.__scr_w)), relief='flat', highlightthickness=0,
                                          command=lambda: self.__service_vb('r'))
        self.__root.bind('l', lambda _: self.__service_vb('l'))
        self.__root.bind('r', lambda _: self.__service_vb('r'))
        self.__start_vb_bm_tt()
        if self.__use_timeouts:
            self.__tol['l'] = self.__tol['r'] = 2
            self.__show_tol_left = Button(self.__root, text='TOL: %d' % self.__tol['l'], fg='dark blue', bg='white',
                                          font=('Times', int(0.03 * self.__scr_w)), relief='flat', highlightthickness=0,
                                          command=lambda: self.__tol_down('l'))
            self.__show_tol_right = Button(self.__root, text='TOL: %d' % self.__tol['r'], fg='dark red', bg='white',
                                           font=('Times', int(0.03 * self.__scr_w)), relief='flat',
                                           highlightthickness=0, command=lambda: self.__tol_down('r'))
            self.__show_tol_left.place(relx=3 / 80, rely=23 / 32, relwidth=4 / 15, relheight=1 / 8)
            self.__show_tol_right.place(relx=167 / 240, rely=23 / 32, relwidth=4 / 15, relheight=1 / 8)
            self.__history = [[self.__points, self.__games, self.__tol, None]]
        else:
            self.__history = [[self.__points, self.__games, None]]

    def __start_bm(self):
        """Starten der Anzeige für den Sport Badminton"""
        self.__team_left = self.__home.get()
        self.__team_right = self.__guest.get()
        self.__clear_tk()
        self.__root.title('Anzeige - Badminton')
        self.__use_timeouts = False
        self.__highest_points = int((10 / 7) * self.__points_sel)
        self.__show_points_left = Button(self.__root, text=str(self.__points['l']), fg='dark blue', bg='white',
                                         anchor=E,
                                         font=('Times', int(0.15 * self.__scr_w)), relief='flat', highlightthickness=0,
                                         command=lambda: self.__service_bm('l'))
        self.__show_points_right = Button(self.__root, text=str(self.__points['r']), fg='dark red', bg='white',
                                          anchor=W,
                                          font=('Times', int(0.15 * self.__scr_w)), relief='flat', highlightthickness=0,
                                          command=lambda: self.__service_bm('r'))
        self.__root.bind('l', lambda _: self.__service_bm('l'))
        self.__root.bind('r', lambda _: self.__service_bm('r'))
        self.__start_vb_bm_tt()
        self.__history = [[self.__points, self.__games, None]]

    def __start_tt(self):
        """Starten der Anzeige für den Sport Tischtennis"""
        self.__team_left = self.__home.get()
        self.__team_right = self.__guest.get()
        if self.__points_sel < 21:
            self.__number_services = int(self.__points_sel / 5)
        else:
            self.__number_services = int(self.__points_sel / 4)
        self.__services = 0
        self.__clear_tk()
        self.__root.title('Anzeige - Tischtennis')
        self.__use_timeouts = False
        self.__show_points_left = Button(self.__root, text=str(self.__points['l']), fg='dark blue', bg='white',
                                         anchor=E,
                                         font=('Times', int(0.15 * self.__scr_w)), relief='flat', highlightthickness=0,
                                         command=lambda: self.__service_tt('l'))
        self.__show_points_right = Button(self.__root, text=str(self.__points['r']), fg='dark red', bg='white',
                                          anchor=W,
                                          font=('Times', int(0.15 * self.__scr_w)), relief='flat', highlightthickness=0,
                                          command=lambda: self.__service_tt('r'))
        self.__root.bind('l', lambda _: self.__service_tt('l'))
        self.__root.bind('r', lambda _: self.__service_tt('r'))
        self.__start_vb_bm_tt()
        self.__history = [[self.__points, self.__games, None]]

    def __start_vb_bm_tt(self):
        """Starten der Anzeige für die Sportarten Volleyball, Badminton und Tischtennis"""
        self.__root.unbind('<Return>')
        self.__games = {'l': 0, 'r': 0}
        self.__service = None
        self.__last_deleted = []
        self.__last_action = '-'
        self.__show_home = Label(self.__root, text=self.__team_left, fg='dark blue', bg='white', anchor=E,
                                 font=('Times', int(0.04 * self.__scr_w)))
        self.__show_guest = Label(self.__root, text=self.__team_right, fg='dark red', bg='white', anchor=W,
                                  font=('Times', int(0.04 * self.__scr_w)))
        self.__hyphen = Label(self.__root, text='-', bg='white', font=('Times', int(0.05 * self.__scr_w)))
        self.__show_games_left = Message(self.__root, text=str(self.__games['l']), fg='dark blue', bg='white',
                                         font=('Times', int(0.08 * self.__scr_w)), relief='groove')
        self.__show_games_right = Message(self.__root, text=str(self.__games['r']), fg='dark red', bg='white',
                                          font=('Times', int(0.08 * self.__scr_w)), relief='groove')
        self.__colon = Label(self.__root, text=':', bg='white', font=('Times', int(0.15 * self.__scr_w)), relief='flat')
        self.__show_service_left = Label(self.__root, text='', fg='dark blue', bg='white',
                                         font=('Times', int(0.1 * self.__scr_w), 'bold'))
        self.__show_service_right = Label(self.__root, text='', fg='dark red', bg='white',
                                          font=('Times', int(0.1 * self.__scr_w), 'bold'))
        self.__show_home.place(relx=1 / 64, rely=1 / 8, relwidth=147 / 320, relheight=1 / 8)
        self.__show_guest.place(relx=8 / 15, rely=1 / 8, relwidth=147 / 320, relheight=1 / 8)
        self.__hyphen.place(relx=19 / 40, rely=1 / 8, relwidth=1 / 20, relheight=1 / 10)
        self.__show_games_left.place(relx=41 / 120, rely=11 / 16, relwidth=1 / 8, relheight=3 / 16)
        self.__show_points_left.place(relx=13 / 60, rely=5 / 16, relwidth=1 / 4, relheight=5 / 16)
        self.__show_points_right.place(relx=8 / 15, rely=5 / 16, relwidth=1 / 4, relheight=5 / 16)
        self.__show_games_right.place(relx=8 / 15, rely=11 / 16, relwidth=1 / 8, relheight=3 / 16)
        self.__colon.place(relx=7 / 15, rely=5 / 16, relwidth=1 / 15, relheight=9 / 32)
        self.__show_service_left.place(relx=1 / 15, rely=5 / 16, relwidth=3 / 20, relheight=5 / 16)
        self.__show_service_right.place(relx=47 / 60, rely=5 / 16, relwidth=3 / 20, relheight=5 / 16)
        self.__root.bind('z', lambda _: self.__step_back_vb_bm_tt())

    def __start_match(self):
        """Starten der Spielzeit"""
        self.__pause()
        self.__pause()
        self.__root.bind('<space>', lambda _: self.__pause())

    def __count(self):
        """Zählen der Spielzeit"""
        if not (self.__is_paused or self.__is_break) and (self.__time_1 < self.__time_sel * 60 or self.__sport == 'fb'):
            self.__time_1 = int(time() - self.__time_0 - self.__time_p)
            self.__time_passed()
            self.__show_time.after(50, self.__count)
        else:
            self.__phase_over()

    def __phase_over(self):
        """Beenden eines Spielabschnitts"""
        if self.__time_1 >= self.__time_sel * 60:
            if self.__sport == 'fb':
                self.__is_break = True
                self.__is_paused = True
                if not self.__in_overtime:
                    minutes = self.__time_sel * self.__phase
                else:
                    minutes = self.__time_sel * self.__phase + self.__regular_time
                self.__time_1_layout = str(minutes) + ':00'
            if self.__phase < self.__phases:
                self.__phase += 1
                if not self.__in_overtime:
                    self.__show_phase.config(text=str(self.__phase))
                elif not self.__in_second_overtime:
                    self.__show_phase.config(text=f'V{self.__phase}')
                else:
                    self.__show_phase.config(text=f'V{self.__phase + 2}')
                if self.__sport == 'bb':
                    self.__time_1_layout = f'{self.__time_sel}:00'
                    self.__tf['l'] = self.__tf['r'] = 0
                    self.__show_tf['l'].config(text='Fouls: %d' % self.__tf['l'])
                    self.__show_tf['r'].config(text='Fouls: %d' % self.__tf['r'])
                    if self.__phase == 3:
                        self.__tol['l'] = 3
                        self.__tol['r'] = 3
                        self.__show_tol_left.config(text='TOL: %d' % self.__tol['l'])
                        self.__show_tol_right.config(text='TOL: %d' % self.__tol['r'])
                elif self.__sport == 'hb':
                    self.__time_1_layout = '0:00'
                self.__is_break = True
                self.__show_time.config(text=self.__time_1_layout)
                self.__pause()
            elif not self.__in_overtime or (self.__sport == 'hb' and not self.__in_second_overtime):
                self.__root.unbind('<space>')
                self.__root.bind('v', lambda _: self.__start_overtime())
            elif not self.__in_penalty and self.__sport in ['fb', 'hb']:
                self.__root.bind('v', lambda _: self.__start_penalty())

    def __pause(self):
        """Pausieren oder Starten der Spielzeit"""
        if self.__is_break:
            self.__is_break = False
            self.__is_paused = True
            self.__time_p = -time()
            self.__time_0 = time()
            self.__time_1 = 0
            self.__root.bind('<space>', lambda _: self.__pause())
        elif self.__sport in ['bb', 'hb']:
            if not self.__is_paused:
                self.__is_paused = True
                self.__time_p -= time()
            else:
                self.__is_paused = False
                self.__time_p += time()
                self.__count()
        elif self.__is_paused:
            self.__is_paused = False
            self.__time_p += time()
            self.__count()

    def __time_passed(self):
        """Umrechnung des Wertes, der die vergangene Spielzeit anzeigt, in Minuten und Sekunden"""
        minutes, seconds = 0, self.__time_1
        while seconds >= 60:
            minutes += 1
            seconds -= 60
        if self.__sport == 'fb':
            minutes += (self.__phase - 1) * self.__time_sel
            if self.__in_overtime:
                minutes += self.__regular_time
        elif self.__sport == 'bb':
            minutes = self.__time_sel - minutes - 1
            seconds = 60 - seconds
            if seconds == 60:
                minutes += 1
                seconds -= 60
        if (self.__sport in ['hb', 'bb'] and minutes <= self.__time_sel) or (self.__sport == 'fb' and (
                (not self.__in_overtime and minutes < self.__time_sel * self.__phase) or (
                self.__in_overtime and minutes < (self.__time_sel * self.__phase + self.__regular_time)))):
            self.__time_1_layout = f'{minutes}:{seconds:02d}'
        elif self.__sport == 'fb' and not self.__in_overtime:
            self.__root.bind('<space>', lambda _: self.__phase_over())
            self.__time_1_layout = f'+{minutes - (self.__time_sel * self.__phase)}:{seconds:02d}'
        elif self.__sport == 'fb' and self.__in_overtime:
            self.__root.bind('<space>', lambda _: self.__phase_over)
            self.__time_1_layout = f'+{minutes - self.__time_sel * self.__phase - self.__regular_time}:{seconds:02d}'
        if self.__last_time != self.__time_1_layout:
            self.__show_time.config(text=self.__time_1_layout)
        self.__last_time = self.__time_1_layout

    def __start_overtime(self):
        """Starten einer Verlängerung"""
        self.__root.bind('<space>', lambda _: self.__pause())
        self.__root.unbind('v')
        if not self.__in_overtime:
            self.__in_overtime = True
            self.__in_second_overtime = False
        else:
            self.__in_second_overtime = True
        self.__phase = 0
        self.__regular_time = 2 * self.__time_sel
        self.__time_sel = self.__overtime_sel
        if self.__sport in ['fb', 'hb']:
            self.__phases = 2
        else:
            self.__phases = 9
        self.__phase_over()
        self.__pause()

    def __start_penalty(self):
        """Starten eines Elfmeterschießens / Siebenmeter-Werfens"""
        self.__root.unbind('v')
        self.__in_penalty = True
        self.__time_1_layout = '0:00'
        self.__show_time.config(text=self.__time_1_layout)
        if self.__sport == 'fb':
            self.__show_phase.config(text='i.E.')
        elif self.__sport == 'hb':
            self.__show_phase.config(text='i.S.')
        self.__points_penalty = {'l': 0, 'r': 0}
        self.__history = [[0, 0]]
        self.__update_widgets_fb_bb_hb()

    def __add_point_fb_bb_hb(self, team):
        """Hinzufügen eines Punktes / Tores im Fußball, Basketball oder Handball"""

        if self.__points[team] < 999 and not self.__in_penalty:
            self.__deleted_to_history()
            self.__points[team] += 1
            self.__show_points_right.config(text=str(self.__points[team]))
            self.__add_to_history_fb_bb_hb()
        elif self.__points_penalty[team] < 99 and self.__in_penalty:
            self.__deleted_to_history()
            self.__points_penalty[team] += 1
            self.__update_widgets_fb_bb_hb()
            self.__add_to_history_fb_bb_hb()

    def __add_point_vb(self, team):
        """Hinzufügen eines Punktes im Volleyball"""
        other = 'r' if team == 'l' else 'l'
        if self.__games['l'] + self.__games['r'] < 2 * self.__games_sel - 2:
            if self.__points[team] >= self.__points_sel - 1 and self.__points[team] > self.__points[other]:
                self.__games[team] += 1
                self.__points[team] = self.__points[other] = 0
                self.__service_vb_after_game()
                if self.__use_timeouts and self.__games[team] < self.__games_sel and self.__games[
                    other] < self.__games_sel:
                    self.__tol['l'] = self.__tol['r'] = 2
                    self.__show_tol_left.config(text='TOL: %d' % self.__tol['l'])
                    self.__show_tol_right.config(text='TOL: %d' % self.__tol['r'])
            else:
                self.__points[team] += 1
        elif self.__points[team] >= self.__max_break - 1 and self.__points[team] > self.__points[other]:
            self.__games[team] += 1
            self.__points[team] = self.__points[other] = 0
            self.__service_vb_after_game()
        else:
            self.__points[team] += 1
        self.__update_widgets_vb_bm_tt()

    def __add_point_bm(self, team):
        """Hinzufügen eines Punktes im Badminton"""
        other = 'r' if team == 'l' else 'l'
        if self.__points[team] >= self.__points_sel - 1 and (
                self.__points[team] > self.__points[other] or self.__points[team] == self.__highest_points - 1):
            self.__games[team] += 1
            self.__points[team] = self.__points[other] = 0
            self.__service = team
            if self.__games[team] == self.__games_sel:
                self.__service = None
        else:
            self.__points[team] += 1
            self.__service = team
        self.__update_widgets_vb_bm_tt()

    def __add_point_tt(self, team):
        """Hinzufügen eines Punktes im Tischtennis"""
        other = 'r' if team == 'l' else 'l'
        if self.__points[team] >= self.__points_sel - 1 and self.__points[team] > self.__points[other]:
            self.__games[team] += 1
            self.__points[team] = self.__points[other] = 0
        else:
            self.__points[team] += 1
        self.__update_widgets_vb_bm_tt()

    def __tol_down(self, team):
        """Abziehen eines übrigen Timeouts"""
        self.__deleted_to_history()
        if self.__tol[team] > 0:
            self.__tol[team] -= 1
            self.__show_tol[team].config(text=f'TOL: {self.__tol[team]}')
            if self.__sport == 'vb':
                self.__add_to_history_vb_bm_tt()
            else:
                self.__add_to_history_fb_bb_hb()

    def __tf_up(self, team):
        """Hinzufügen eines Teamfouls"""
        self.__deleted_to_history()
        if self.__tf[team] < 99:
            self.__tf[team] += 1
            self.__show_tf[team].config(text=f'Fouls: {self.__tf[team]}')
            self.__add_to_history_fb_bb_hb()

    def __service_vb(self, team):
        """Ändern des Aufschlagrechts im Volleyball"""
        other = 'r' if team == 'l' else 'l'
        self.__deleted_to_history()
        if self.__games[team] < self.__games_sel and self.__games[other] < self.__games_sel:
            if self.__service is None:
                self.__service_0 = self.__service = team
            else:
                self.__service = team
                self.__add_point_vb(team)
            self.__add_to_history_vb_bm_tt()
            self.__update_show_service()

    def __service_vb_after_game(self):
        """Ändern des Aufschlagrechts im Volleyball nach einem Satzgewinn"""
        if self.__games['l'] == self.__games_sel or self.__games['r'] == self.__games_sel:
            self.__service = None
        elif self.__games['l'] + self.__games['r'] == 2 * self.__games_sel - 2:
            self.__service = None
        elif self.__service_0 == 'l':
            self.__service_0 = self.__service = 'r'
        elif self.__service_0 == 'r':
            self.__service_0 = self.__service = 'l'
        self.__update_show_service()

    def __service_bm(self, team):
        """Ändern des Aufschlagrechts im Badminton"""
        other = 'r' if team == 'l' else 'l'
        self.__deleted_to_history()
        if self.__games[team] < self.__games_sel and self.__games[other] < self.__games_sel:
            if self.__service is None:
                self.__service_0 = self.__service = team
            else:
                self.__add_point_bm(team)
            self.__add_to_history_vb_bm_tt()
            self.__update_show_service()

    def __service_tt(self, team):
        """Ändern des Aufschlagrechts im Tischtennis, wenn eine Seite punktet"""
        other = 'r' if team == 'l' else 'l'
        self.__deleted_to_history()
        if self.__games[team] < self.__games_sel and self.__games[other] < self.__games_sel:
            if self.__service is None:
                self.__service_0 = self.__service = team
            else:
                self.__add_point_tt(team)
                self.__change_service_tt()
            self.__add_to_history_vb_bm_tt()
            self.__update_show_service()

    def __change_service_tt(self):
        """Ändern des Aufschlagrechts im Tischtennis"""
        if self.__points['l'] + self.__points['r'] > 0:
            if self.__points['l'] + self.__points['r'] < 2 * self.__points_sel - 2:
                if self.__services < self.__number_services - 1:
                    self.__services += 1
                self.__services = 0
            self.__service = 'r' if self.__service == 'l' else 'l'
        elif self.__service_0 == 'l':
            self.__service_0 = self.__service = 'r'
        else:
            self.__service_0 = self.__service = 'l'
        if self.__games['l'] == self.__games_sel or self.__games['r'] == self.__games_sel:
            self.__service = None

    def __update_show_service(self):
        """Aktualisieren der Anzeigen für das Aufschlagrecht"""
        if self.__service is None:
            self.__show_service_left.config(text='')
            self.__show_service_right.config(text='')
        elif self.__service == 'left':
            self.__show_service_left.config(text='<')
            self.__show_service_right.config(text='')
        elif self.__service == 'right':
            self.__show_service_left.config(text='')
            self.__show_service_right.config(text='>')

    def __add_to_history_fb_bb_hb(self):
        """Hinzufügen der aktuellen Spielwerte (außer Spielzeit) in eine Liste im Fußball, Basketball und Handball"""
        if not self.__in_penalty:
            if self.__use_team_fouls and self.__use_timeouts:
                self.__history.append([self.__points, self.__tol, self.__tf])
            elif self.__use_team_fouls and not self.__use_timeouts:
                self.__history.append([self.__points, self.__tf])
            elif not self.__use_team_fouls and self.__use_timeouts:
                self.__history.append([self.__points, self.__tol])
            else:
                self.__history.append([self.__points])
        else:
            self.__history.append([self.__points, self.__points_penalty])

    def __add_to_history_vb_bm_tt(self):
        """Hinzufügen der aktuellen Spielwerte in eine Liste im Volleyball, Badminton und Tischtennis"""
        if self.__use_timeouts:
            self.__history.append([self.__points, self.__games, self.__tol, self.__service])
        else:
            self.__history.append([self.__points, self.__games, self.__service])

    def __step_back_fb_bb_hb(self):
        """Rückgängigmachen des letzten Schrittes während Laufens der Anzeigetafel im
        Fußball, Basketball und Handball"""

        def step_back():
            if len(self.__history) > 0:
                last_stats = self.__history.pop()
                self.__last_deleted = last_stats[:]
                if not self.__in_penalty:
                    if self.__use_team_fouls and self.__use_timeouts:
                        self.__tf = last_stats.pop()
                        self.__tol = last_stats.pop()
                        self.__points = last_stats.pop()
                    elif self.__use_team_fouls and not self.__use_timeouts:
                        self.__tf = last_stats.pop()
                        self.__points = last_stats.pop()
                    elif not self.__use_team_fouls and self.__use_timeouts:
                        self.__tol = last_stats.pop()
                        self.__points = last_stats.pop()
                    else:
                        self.__points = last_stats.pop()
                else:
                    self.__points_penalty = last_stats.pop()
                self.__update_widgets_fb_bb_hb()

        if self.__last_action == '+':
            step_back()
            step_back()
        else:
            step_back()
        self.__last_action = '-'

    def __step_back_vb_bm_tt(self):
        """Rückgängigmachen des letzten Schrittes während Laufens der Anzeigetafel im
        Volleyball, Badminton und Tischtennis"""

        def step_back():
            if len(self.__history) > 0:
                last_stats = self.__history.pop()
                self.__last_deleted = last_stats[:]
                if self.__use_timeouts:
                    self.__service = last_stats.pop()
                    self.__tol = last_stats.pop()
                    self.__games = last_stats.pop()
                    self.__points = last_stats.pop()
                else:
                    self.__service = last_stats.pop()
                    self.__games = last_stats.pop()
                    self.__points = last_stats.pop()
                self.__update_widgets_vb_bm_tt()

        if self.__last_action == '+':
            step_back()
            step_back()
        else:
            step_back()
        self.__last_action = '-'

    def __deleted_to_history(self):
        """Hinzufügen des zuletzt gelöschten Wertes zur Liste der gelöschten Werte"""
        if self.__last_deleted:
            self.__history.append(self.__last_deleted)
            self.__last_deleted = []
        self.__last_action = '+'

    def __update_widgets_fb_bb_hb(self):
        """Aktualisieren der Anzeige im Fußball, Basketball und Handball"""
        if not self.__in_penalty:
            self.__show_points_left.config(text=str(self.__points['l']))
            self.__show_points_right.config(text=str(self.__points['r']))
        else:
            self.__show_points_left.config(text=str(self.__points_penalty['l']))
            self.__show_points_right.config(text=str(self.__points_penalty['r']))
        if self.__use_timeouts:
            self.__show_tol_left.config(text='TOL: %d' % self.__tol['l'])
            self.__show_tol_right.config(text='TOL: %d' % self.__tol['r'])
        if self.__use_team_fouls:
            self.__show_tf['l'].config(text='Fouls: %d' % self.__tf['l'])
            self.__show_tf['r'].config(text='Fouls: %d' % self.__tf['r'])

    def __update_widgets_vb_bm_tt(self):
        """Aktualisieren der Anzeige im Volleyball, Badminton und Tischtennis"""
        self.__show_points_left.config(text=str(self.__points['l']))
        self.__show_points_right.config(text=str(self.__points['r']))
        self.__show_games_left.config(text=str(self.__games['l']))
        self.__show_games_right.config(text=str(self.__games['r']))
        if self.__use_timeouts:
            self.__show_tol_left.config(text='TOL: %d' % self.__tol['l'])
            self.__show_tol_right.config(text='TOL: %d' % self.__tol['r'])
        serv_l = serv_r = ''
        if self.__service == 'l':
            serv_l = '<'
        elif self.__service == 'r':
            serv_r, = '>'
        self.__show_service_left.config(text=serv_l)
        self.__show_service_right.config(text=serv_r)


if __name__ == '__main__':
    tk = Tk()
    Anzeige(tk)
    tk.mainloop()
