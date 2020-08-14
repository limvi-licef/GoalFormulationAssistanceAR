# coding: utf-8


import InputOutput as io


############################################################################
class Icon(io.Output):

    """
    Image output that inherits from Output class.
    """
    
    ########################################################################
    def __init__(self, attrib, pos3d, size):

        """
        attrib: str, image name.
        pos3d: tuple of size 3, space coordinates in Hololens world (x,y,z).
        dim: tuple of size 2, size of image (width,height).
        """
        
        Output.__init__(self, attrib)
        self.pos3d = pos3d
        self.size = size
    
    
    ########################################################################
    def compile(self):
        
        """
        Return inherited representation and pos3d & size attributes.
        """
        
        return (
            *io.Output.__str__(self),
            str(self.pos3d[0]),
            str(self.pos3d[1]),
            str(self.pos3d[2]),
            str(self.size)
            )
