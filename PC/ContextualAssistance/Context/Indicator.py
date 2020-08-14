# coding: utf-8


##########################################################################
class Indicator:

    """
    Base class for context indication.
    """

    ######################################################################
    def __init__(self):

        """
        Setup indicator attributes.
        """

        self._indicator = None

    
    ######################################################################
    def get(self):

        return self._indicator

    
    ######################################################################
    def update(self, decision_kernel):

        """
        Check indicator and notify kernel if it changes.

        decision_kernel: the decision kernel where send indicator.
        """

        indicator = self.run()

        if self._indicator != indicator:
            self._indicator = indicator
            decision_kernel.make_decision()

    
    ######################################################################
    def run(self):

        """
        Method to override.
        
        Return updated indicator.
        """

        return None
