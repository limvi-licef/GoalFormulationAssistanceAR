# coding: utf-8


import InputOutput as io
import Ontology as onto
import Context as ctx
import CustomAssistanceLevel as cal


########################################################################
class BaseDecisionKernel:

    """
    Base class of decision kernel.
    """

    ####################################################################
    def __init__(self, decision_onto, assistance_level):

        """
        Bind output stack to kernel and initialize indicator list.

        output_stack: OutputStack object, stack of outputs defined in InputOutput package.
        decision_onto: BaseOnto child class, ontology for make decision.
        """

        assert type(decision_onto).__base__ == onto.BaseOnto, "decision_onto is not an object that inherits from BaseOnto class"
        assert type(assistance_level).__base__ == cal.AssistanceLevel, "assistance_level is not an object that inherits from AssistanceLevel class"

        self._indicators = {}
        self._decision_onto = decision_onto
        self._assistance_level = assistance_level


    ####################################################################
    def get(self, indicator):

        """
        Quick access to get method of Indicator.
        """
        
        return self._indicators[indicator].get()


    ####################################################################
    def add(self, *indicators):

        """
        Public method of _add that could be overriden.
        """
        
        self._add(*indicators)


    ####################################################################
    def _add(self, *indicators):

        """
        Add Indicator object to indicator dict.
        """

        for indicator in indicators:
            if type(indicator) not in self._indicators:
                self._indicators[type(indicator)] = indicator


    ####################################################################
    def update(self, **kwargs):

        """
        Update each indicator. Indicator will call make decision if change occurs.
        """

        for indicator_type, indicator in self._indicators.items():
            indicator.update(self)


    ####################################################################
    def notifByOutput(self, notification):

        """
        Put annotation in output stack.
        """

        if self._assistance_level.annotation_type == cal.ANNOTATION_TYPE_TEXT:
            annotation = io.Text(notification, (0,0,2))

        elif self._assistance_level.annotation_type == cal.ANNOTATION_TYPE_SPEAK:
            annotation = io.Speak(notification)

        else:
            annotation = None

        annotation and io.OutputStack().add(annotation)
        io.OutputStack().send()


    ####################################################################
    def make_decision(self):

        """
        Method where decision of output is made.
        """

        pass