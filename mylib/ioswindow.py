#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import tkinter as tk

class ioswindow():
    def __init__(self,windowtitle,windowsize):
        self.windowtitle = windowtitle
        self.windowsize  = windowsize
        self.tk          = tk
        self.window      = tk.Tk()

        self.window.title(self.windowtitle)
        self.window.geometry(windowsize)

    def getWindow(self):
        return self.window

    def getTk(self):
        return self.tk

    def openWindow(self):
        self.window.mainloop()