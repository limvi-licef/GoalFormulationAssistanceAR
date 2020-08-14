# coding: utf-8


import CustomAssistanceLevel as cal

#################################################################################################
class AssistanceLevel:

    """
    Class that contains information for efficient assistance.
    """

    #############################################################################################
    def __init__(self, annotation_type=None, reminding_time=None):

        """
        Initialize assistance parameters.

        annotation_type: ANNOTATION_TYPE class, preferred type of annotation to send.
        reminding_time: REMINDING_TIME class, time of remind.
        """

        assert annotation_type.__base__ == cal.ANNOTATION_TYPE, "annotation_type should be type ANNOTATION_TYPE"
        assert reminding_time.__base__ == cal.REMINDING_TIME, "reminding_time should be type REMINDING_TIME"

        self.annotation_type = annotation_type
        self.reminding_time = reminding_time
