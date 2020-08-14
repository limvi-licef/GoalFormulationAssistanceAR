# coding: utf-8


import tkinter as tk
import InputOutput as io
import Ontology as onto
import Context as ctx
import CustomAssistanceLevel as cal

from DecisionKernel.BaseDecisionKernel import BaseDecisionKernel
from GUI import GUI



class GoalDecisionKernelGui(tk.Frame):

    def __init__(self):

        gui = GUI()
        tk.Frame.__init__(self, )

        self.title = tk.Label(self, text="Decision kernel", font=('Arial', 16))
        self.title.pack(anchor=tk.W)

        self.decision = tk.Label(self, text="", font=('Arial', 12))
        self.decision.pack(anchor=tk.W)

        self.pack(anchor=tk.W)
        gui.update()





########################################################################
class GoalDecisionKernel(BaseDecisionKernel):

    """
    Base class of decision kernel.
    """

    ####################################################################
    def __init__(self, decision_onto, assistance_level):

        BaseDecisionKernel.__init__(self, decision_onto, assistance_level)
        self.gui = GoalDecisionKernelGui()


    ####################################################################
    def add(self, room_classifier, clock):

        """
        Add override.

        room_classifier: RoomClassification object.
        clock: ClockTime object.
        """

        assert type(room_classifier) == ctx.RoomClassification, "room_classifier should be RoomClassification object"
        assert type(clock) == ctx.ClockTime, "clock should be ClockTime object"

        BaseDecisionKernel.add(self, room_classifier, clock)
        self.goal = None


    ####################################################################
    def parseGoal(self):

        h = self.get(ctx.ClockTime)
        output = io.Text(str(h), (0,0,0))

        r = self.get(ctx.RoomClassification)
        output = io.Text(str(r), (0,0,0))

        daytime = self._decision_onto.getDaytime(h)
        goals = self._decision_onto.getGoal(daytime=daytime, room=str(r))
        if len(goals) > 0:
            self.goal = str(goals[0].name)
        else:
            self.goal = str(None)

        self.gui.decision['text'] = str(self.goal)


    ####################################################################
    def make_decision(self):

        self.parseGoal()

        self.notifByOutput(self.goal)