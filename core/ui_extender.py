#!/usr/bin/env python
# encoding: utf-8
"""
ui_extender.py

Tkinter UI extender file for Slide-OSK

(c) 2019 SnooeyNET
"""
from tkinter import *

import keyboard


class KeyButton(Button):
    text = ''
    key = ''

    def __init__(self, master=None, cnf={}, **kw):
        self.text = kw["text"]
        if "key" in kw:
            self.key = kw["key"]
        else:
            self.key = self.text

        super(KeyButton, self).__init__(master, cnf, **kw)
        self.bind('<Button-1>', self.press)
        self.bind('<B1-Motion>', self.swipe)

    def press(self, event=None):
        keyboard.write(self.key)

    def swipe(self, event=None):
        print(f"position: {{{event.x}, {event.y}}}")

