# coding: utf-8


############################################################################
def Singleton(cls):

    """
    Class wrapper for singleton behavior.
    """
    
    ########################################################################
    class SingletonPatern(cls):
                
        """
        Wrapper of constructor.
        Call class constructor if the class is not already instanciated else return instance.
        """

        instance = None # reference to class instanciation

        ####################################################################
        def __new__(cls, *args, **kwargs):

            if not SingletonPatern.instance:
                return super(SingletonPatern, cls).__new__(cls)
            else:
                return SingletonPatern.instance
        
        ####################################################################
        def __init__(self, *args, **kwargs):

            """
            Wrapper of initiation.
            """
            
            if not SingletonPatern.instance:
                cls.__init__(self, *args, **kwargs)
                SingletonPatern.instance = self
    
    return SingletonPatern