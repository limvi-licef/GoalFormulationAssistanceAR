# coding: utf-8


############################################################################
class Output:

    """
    Base class for output to Hololens.
    """
    
    ########################################################################
    def __init__(self, attrib):

        """
        Initialize object with attrib.

        attrib: string, main information of the output.
        """

        assert type(attrib)==str, "attrib should be type str"
        
        self.attrib = attrib
    
    
    ########################################################################
    def compile(self):

        """
        Default representation is : (class_name, attrib).
        """
        
        return (type(self).__name__, self.attrib)
    
    
    ########################################################################
    def __str__(self):

        return str.join(" ", self.compile())
    
