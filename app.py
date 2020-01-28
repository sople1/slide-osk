#!/usr/bin/env python
# encoding: utf-8
"""
app.py

app root file for Slide-OSK

(c) 2019 SnooeyNET
"""

from tkinter import *
import keyboard

from core import windowing
from core.ui_extender import *


class App(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)

        self.btn = KeyButton(self, text="ㄱ", width=10, height=10, takefocus=0)
        self.btn.pack(padx=20, pady=20)

        self.btn2 = KeyButton(self, text="ㅜ", width=10, height=10, takefocus=0)
        self.btn2.pack(padx=20, pady=20)

        self.set_event()
        self.set_window()
        self.set_window_size()
        self.set_window_position()

    def app_got_focus(self, event):
        self.config(background="yellow")

    def app_lost_focus(self, event):
        self.config(background="grey")

    def handle_return(self, event):
        print(f"return: event.widget is {event.widget}")
        print(f"focus is {self.focus_get()}")

    def set_event(self):
        self.bind("<FocusIn>", self.app_got_focus)
        self.bind("<FocusOut>", self.app_lost_focus)
        self.bind("<Return>", self.handle_return)

    def set_window(self):
        self.title('keyboard')
        self.focusmodel(model=None)
        self.attributes("-toolwindow", True)
        self.attributes("-topmost", True)

    def set_window_size(self):
        width = self.winfo_screenwidth()
        height = self.winfo_screenheight()
        self.geometry('%sx%s' % (int(width/2), int(height/2)))

    def set_window_position(self):
        self.geometry('-%s-%s' % (5, 5))


if __name__ == '__main__':
    windowing.run(App())
