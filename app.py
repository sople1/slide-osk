from tkinter import *
import win32api
import win32con
import pywintypes
import keyboard


class App(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)

        self.btn = Button(self, text="ㄱ", width=10, takefocus=0, command=self.press_key)
        # self.btn.grid(row=1, column=1)
        self.btn.pack(padx=50, pady=50)

        self.title('keyboard')
        self.focusmodel(model=None)
        self.attributes("-toolwindow", True)
        self.attributes("-topmost", True)

        self.bind("<FocusIn>", self.app_got_focus)
        self.bind("<FocusOut>", self.app_lost_focus)

    def app_got_focus(self, event):
        self.config(background="red")

    def app_lost_focus(self, event):
        self.config(background="grey")

    def press_key(self):
        keyboard.send("a,b")


if __name__ == '__main__':
    root = App()
    root.lift()

    hWindow = pywintypes.HANDLE(int(root.frame(), 16))
    exStyle = win32con.WS_EX_COMPOSITED | win32con.WS_EX_LAYERED | win32con.WS_EX_NOACTIVATE
    win32api.SetWindowLong(hWindow, win32con.GWL_EXSTYLE, exStyle)

    root.mainloop()
