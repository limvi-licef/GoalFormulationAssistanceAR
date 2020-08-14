# coding: utf-8


import Ontology as onto


def test():

    goalOnto = onto.GoalOnto("Ontology/GoalOntoV1.owl")

    print("_______GoalList________")
    print("{:12s} | {:10s} | {:10s}".format("GOAL", "ROOM", "DAYTIME"))
    print("{:12s} | {:10s} | {:10s}".format("", "", ""))
    for goal in goalOnto._onto.Goal.subclasses():
        goalname = goal.name
        room = goal.todoWhere[0].name
        daytime = goal.todoWhen[0].name
        print("{:12s} | {:10s} | {:10s}".format(goalname, room, daytime))
    print()

    print("_______Daytime________")
    for h in range(24):
        print(f"{h}h:", goalOnto.getDaytime(h).name)
    print()

    print("_______GoalByDaytime________")
    for h in range(5,15):
        daytime = goalOnto.getDaytime(h)
        print(f"{h}h:", goalOnto.getGoalByDaytime(daytime))
    print()

    print("_______GoalByRoom________")
    for room in goalOnto._onto.Room.subclasses():
        print(room.name, goalOnto.getGoalByRoom(room))
    print()

    print("_______GoalByRoom&Daytime________")
    for room in goalOnto._onto.Room.subclasses():
        print(room.name)
        for h in range(5,15):
            daytime = goalOnto.getDaytime(h)
            print("{:6d}h:".format(h), goalOnto.getGoal(daytime=daytime, room=room))
        print()
    print()