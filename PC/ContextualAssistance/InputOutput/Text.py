# coding: utf-8


import InputOutput as io


############################################################################
class Text(io.Output):

    """
    Text output that inherits from Output class.
    """
    
    ########################################################################
    def __init__(self, attrib, pos3d):

        """
        attrib: str, text to send.
        pos3d: tuple of size 3, space coordinates in Hololens world.
        """
        
        io.Output.__init__(self, attrib)
        self.pos3d = pos3d
    
    
    ########################################################################
    def compile(self):

        """
        Return inherited str representation and pos3d attribute.
        """
        
        return (
            *io.Output.compile(self),
            str(self.pos3d[0]),
            str(self.pos3d[1]),
            str(self.pos3d[2])
            )
