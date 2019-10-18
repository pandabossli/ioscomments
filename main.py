#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from mylib import ioscomments,ioswindow
import time
import _thread

def printComments(comments,textarea,star):
    while True:
        item = comments.get()
        if item == -1:
            break
        elif item != 0:
            if star == -1:
                textarea.insert('end', item['title']+"\t"+item['content']+"\n")
            elif star == item['star']:
                textarea.insert('end', item['title'] + "\t" + item['content'] + "\n")
            print(item)

def  runComments(comments):
    comments.run()

def start():
    country = countryEntry.get()
    appid = appidEntry.get()
    star = startEntry.get()
    comments = ioscomments.ioscomments(country,appid,star)
    _thread.start_new_thread(runComments, (comments,))
    _thread.start_new_thread(printComments, (comments,textArea,star))


if __name__ == '__main__':


    ioswindow = ioswindow.ioswindow("IOS好评采集器","500x300")
    tk = ioswindow.getTk()
    window = ioswindow.getWindow()

    countryLabel = tk.Label(window,text="国家简码（如：CN）").place(anchor='nw')
    countryEntry = tk.Entry(window,show=None)
    countryEntry.place(anchor='nw',x=200)

    appidLabel   = tk.Label(window,text="APPID").place(anchor='nw',x=0,y=20)
    appidEntry   = tk.Entry(window,show=None)
    appidEntry.place(anchor='nw',x=200,y=20)

    starLabel    = tk.Label(window,text="评分").place(anchor='nw',x=0,y=40)
    startEntry   = tk.Entry(window,show=None)
    startEntry.place(anchor='nw',x=200,y=40)

    b = tk.Button(window, text="开始采集", font=('Arial', 12), width=10, height=1, command=start)
    b.place(anchor='nw',x=0,y=60)

    textArea = tk.Text(window, height=10)
    textArea.place(anchor='nw',x=0,y=90)

    ioswindow.openWindow()