# !/usr/bin/env python
# encoding: utf-8
"""
app.py

launcher file for Slide-OSK

(c) 2019 SnooeyNET
"""

from tkinter import *
import win32api
import win32con
import pywintypes
import keyboard


class App(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)

        self.btn = Button(self, text="ㄱ", width=10, takefocus=0)
        self.btn.bind('<Button-1>', self.press_key)
        self.btn.bind('<B1-Motion>', self.swipe_key)
        # self.btn.grid(row=1, column=1)
        self.btn.pack(padx=50, pady=20)

        self.btn2 = Button(self, text="ㅜ", width=10, takefocus=0, command=self.press_key2)
        # self.btn.grid(row=1, column=1)
        self.btn2.pack(padx=50, pady=20)

        self.title('keyboard')
        self.focusmodel(model=None)
        self.attributes("-toolwindow", True)
        self.attributes("-topmost", True)

        self.bind("<FocusIn>", self.app_got_focus)
        self.bind("<FocusOut>", self.app_lost_focus)
        self.bind("<Return>", self.handle_return)

    def app_got_focus(self, event):
        self.config(background="yellow")

    def app_lost_focus(self, event):
        self.config(background="grey")

    def handle_return(self, event):
        print(f"return: event.widget is {event.widget}")
        print(f"focus is {self.focus_get()}")

    def press_key(self, event):
        keyboard.write("ㄱ")

    def press_key2(self):
        keyboard.write("ㅜ")

    def swipe_key(self, event):
        print(f"position: {{{event.x}, {event.y}}}")


if __name__ == '__main__':
    root = App()
    root.lift()

    hWindow = pywintypes.HANDLE(int(root.frame(), 16))
    exStyle = win32con.WS_EX_COMPOSITED | win32con.WS_EX_LAYERED | win32con.WS_EX_NOACTIVATE
    win32api.SetWindowLong(hWindow, win32con.GWL_EXSTYLE, exStyle)

    root.mainloop()
