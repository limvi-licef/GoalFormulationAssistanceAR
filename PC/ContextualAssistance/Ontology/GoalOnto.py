# coding: utf-8


import time
import numpy as np

from Ontology.BaseOnto import BaseOnto


#######################################################################################
class GoalOnto(BaseOnto):

    """
    Goal formulation ontology based on context.
    """

    _criterions = ["daytime", "room"]

    ###################################################################################
    def ontoDaytime(self, daytime):

        """
        Convert str daytime to ontology daytime and ensure that daytime is valid.
        """

        if type(daytime) == str:
            assert self._onto[daytime] != None, f"{daytime} does not exist in the ontology"
            daytime = self._onto[daytime]

        assert self._onto.Daytime in daytime.is_a, "daytime argument is not valid"
        
        return daytime


    ###################################################################################
    def ontoRoom(self, room):

        """
        Convert str room to ontology room and ensure that room is valid.
        """

        if type(room) == str:
            assert self._onto[room] != None, f"{room} does not exist in the ontology"
            room = self._onto[room]

        assert self._onto.Room in room.is_a, "room argument is not valid"
        
        return room


    ###################################################################################
    def getDaytime(self, h=-1):

        """
        Parser of daytime.

        h: int from -1 to 23, time in hour to parse. Get current hour number by default.
        """
    
        # parse t
        assert type(h) == int, "h argument should be type int"
        assert -2 < h < 24
        if h == -1: h = getHour()
        
        for daytime in self._onto.Daytime.subclasses():
            if h >= daytime.start_at[0] and h < daytime.end_at[0]:
                return daytime
        
        return self._onto.Night

    
    ###################################################################################
    def getGoal(self, **kwargs):


        goals = []
        for goal in self._onto.Goal.subclasses(): goals.append(goal)

        for kw, arg in kwargs.items():

            if len(goals) == 0:
                break

            elif kw in GoalOnto._criterions:

                goal_to_keep = []
                get_goal_method = getattr(self, "getGoalBy"+kw.capitalize())

                for goal in get_goal_method(arg):
                    if goal in goals: goal_to_keep.append(goal)
                goals = goal_to_keep

        return goals


    ###################################################################################
    def getGoalByDaytime(self, daytime):

        """
        Return a list that contains goal compatible with daytime.

        daytime: str or ontology daytime class.
        """
        
        daytime = self.ontoDaytime(daytime)
        goals = []
        
        for goal in self._onto.Goal.subclasses():
            if daytime in goal.todoWhen:
                goals.append(goal)
        
        return goals


    ###################################################################################
    def getGoalByRoom(self, room):

        """
        Return a list that contains goal compatible with room.

        room: str or ontology room class.
        """
    
        room = self.ontoRoom(room)
        goals = []
        
        for goal in self._onto.Goal.subclasses():
            if room in goal.todoWhere:
                goals.append(goal)
        
        return goals


#######################################################################################
def getHour():

    """
    Return hour number of current time.
    """
    
    return time.localtime()[3]

