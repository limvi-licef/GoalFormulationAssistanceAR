# coding: utf-8


from InputOutput import *


############################################################################
def io_test():
    
    print("________Outputs__________")
    outStack = OutputStack()
    outStack_copy = OutputStack()

    t = Text("Annotation", (0,1,2))
    outStack.add(t)

    i = Icon("icon.png", (3,4,5), (6,6))
    outStack.add(i)

    so = Sound("sound.mp3")
    outStack.add(so)

    sp = Speak("Hello")
    outStack.add(sp)

    outStack_copy.send()
    print()

    
    print("________Inputs__________")
    
    cam = Camera()

    print("updateFrame >> ", end=''), cam.updateFrame()
    print("getFrame >> ", end=''), cam.getFrame()
    print("disconnect >> ", end=''), cam.disconnect()
    print("isConnected:", cam.isConnected())
    print()

    print("connection >> ", end=''), cam.connection("localhost", 9999)
    print("updateFrame >> ", end=''), cam.updateFrame()
    print("getFrame >> ", end=''), cam.getFrame()
    print()