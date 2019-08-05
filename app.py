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

        self.btn = Button(self, text="ㄱ", width=10, height=10, takefocus=0)
        self.btn.bind('<Button-1>', self.press_key)
        self.btn.bind('<B1-Motion>', self.swipe_key)
        # self.btn.grid(row=1, column=1)
        self.btn.pack(padx=50, pady=20)

        self.btn2 = Button(self, text="ㅜ", width=10, height=10, takefocus=0, command=self.press_key2)
        # self.btn.grid(row=1, column=1)
        self.btn2.pack(padx=50, pady=20)

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
