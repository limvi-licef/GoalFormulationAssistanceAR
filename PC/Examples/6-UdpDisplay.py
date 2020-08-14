# coding: utf-8


from test_env_setup import *
from Lib.AnnotationSocket import AnnotationSocket

import sys
import tkinter as tk


def connect():

    _host = hostInput.get()
    _port = int(portInput.get())

    win.socket = AnnotationSocket().Bind(_host, _port)
    connected = win.socket.WaitConnection()


    if not connected:
        print("Timeout error: waiting connection from Hololens")
    else:
        print("Connected to {}".format(win.socket.client))
        win.quit()


def new_command():

    win.socket.Draw("new", 0, 0, 2, "azerty")


def del_command():

    win.socket.Draw("del")



win = tk.Tk()

hostText = tk.Label(win, text="Host")
hostText.grid(row=0, column=0)
hostInput = tk.Entry(win)
hostInput.grid(row=0, column=1)

portText = tk.Label(win, text="Port")
portText.grid(row=1, column=0)
portInput= tk.Entry(win)
portInput.grid(row=1, column=1)

startServing = tk.Button(win, text="Serve", command=connect)
startServing.grid(row=2, column=1, columnspan=2)

win.mainloop()


if win.socket:
    for widget in win.grid_slaves(): widget.destroy()
    
    delText = tk.Button(win, text="New azerty", command=new_command)
    delText.grid(row=0, column=0)

    delText = tk.Button(win, text="Del", command=del_command)
    delText.grid(row=0, column=1)

    win.mainloop()

    win.socket.Exit()
    win.socket.close()