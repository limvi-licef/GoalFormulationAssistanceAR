# coding: utf-8


import tkinter as tk
from time import localtime

from Context.Indicator import Indicator
from GUI import GUI



##########################################################################
class ClockTimeGui(tk.Frame):

    def __init__(self):

        gui = GUI()
        tk.Frame.__init__(self, )

        self.title = tk.Label(self, text="Clock indicator", font=('Arial', 16))
        self.title.pack(anchor=tk.W)

        self.time = tk.Label(self, text="", font=('Arial', 12))
        self.time.pack(anchor=tk.W)

        if GUI().debug:
            self.debug_time = 0

            self.selector = tk.Scale(self, from_=0, to=23, orient=tk.HORIZONTAL)
            self.selector.pack(anchor=tk.W)

        self.pack(anchor=tk.W)
        gui.update()



##########################################################################
class ClockTime(Indicator):

    """
    Context indicator of current time.
    """

    ######################################################################
    def __init__(self):

        """
        Setup the indicator.
        """

        self.gui = ClockTimeGui()
        Indicator.__init__(self)
    

    ######################################################################
    def run(self):

        """
        Return updated indicator.
        """

        if GUI().debug:
            t = self.gui.selector.get()
        else:
            t = localtime()[3]

        self.gui.time['text'] = str(t)
        return t

