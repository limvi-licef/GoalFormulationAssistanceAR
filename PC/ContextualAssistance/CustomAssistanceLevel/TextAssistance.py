# coding: utf-8


from CustomAssistanceLevel.AssistanceLevel import AssistanceLevel
from CustomAssistanceLevel.constant import ANNOTATION_TYPE_TEXT, REMINDING_TIME_30SEC


#################################################################################################
class TextAssistance(AssistanceLevel):

    """
    Text oriented assistance.
    """

    #############################################################################################
    def __init__(self):

        """
        Initialize assistance parameters for text.
        """

        AssistanceLevel.__init__(self, ANNOTATION_TYPE_TEXT, REMINDING_TIME_30SEC)
        