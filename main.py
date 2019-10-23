#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from mylib import ioscomments,ioswindow
import time
import _thread
from tkinter import messagebox
from openpyxl import workbook
def printComments(comments,textarea,star):
    global resultList
    while True:

        item = comments.get()
        if item == -1:
            messagebox.showinfo(title='已完成', message='已完成')

            break
        elif item != 0:
            if star == -1:
                try:
                    resultList.append(item)
                    textarea.insert('end', item['title']+"\t"+item['content']+"\n")

                except Exception as e:
                    print(e)
            elif star == item['star']:
                try:
                    resultList.append(item)
                    textarea.insert('end', item['title']+"\t"+item['content']+"\n")

                except Exception as e:
                    print(e)
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

def exportExcel():
    global resultList

    wb = workbook.Workbook()

    sheet = wb.active
    sheet.title = "好评统计"
    sheet['A1'] = 'title'
    sheet['B1'] = 'content'
    i = 2
    for index in resultList:
        keyA =  "A" + str(i)
        keyB = "B" + str(i)
        sheet[keyA] = index['title']
        sheet[keyB] = index['content']
        i = i + 1

    wb.save('./result1.xlsx')
    messagebox.showinfo(title='导出完成', message='导出完成')


if __name__ == '__main__':

    resultList = []
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

    b1 = tk.Button(window, text="导出excel", font=('Arial', 12), width=10, height=1, command=exportExcel)
    b1.place(anchor='nw', x=120, y=60)

    textArea = tk.Text(window, height=30,width=200)
    textArea.place(anchor='nw',x=0,y=90)

    ioswindow.openWindow()