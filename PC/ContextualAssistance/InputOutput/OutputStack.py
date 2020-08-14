# coding: utf-8


import Tools as tools
from Lib.AnnotationSocket import AnnotationSocket


############################################################################
@tools.Singleton
class OutputStack:

    """
    Stack of outputs to Hololens with FIFO Behavior.
    
    Warning: Singleton.
    """
    
    ########################################################################
    def __init__(self, host="127.0.0.1", port=9999):

        """
        Initialize a list as stack of outputs and await connction from Hololens.
        """
        
        self.clear()

        self.socket = AnnotationSocket().Bind(host, port)
        self.connected = self.socket.WaitConnection()


    ########################################################################
    def clear(self):

        """
        Clear the stack.
        Called at the end of sendings.
        """
        
        self.outputs = []

    
    ########################################################################
    def add(self, output):

        """
        Add output to the stack.
        """
        
        self.outputs.append(output)
        
    
    ########################################################################
    def send(self):

        """
        Send all outputs to Hololens.
        """
        
        self.socket.Draw("del")

        if self.connected:
            for output in self.outputs:
                self.socket.Draw(*output.compile())
                print(output)

        self.clear()