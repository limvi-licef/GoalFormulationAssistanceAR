# coding: utf-8


############################################################################
class BaseOnto:

    """
    Base class for ontology use.
    Contains only loading part.
    """

    ########################################################################
    def __init__(self, onto_filename):

        """
        Load ontology from file.

        onto_filename: str,
        """

        import owlready2 as owl
        
        self._onto = owl.get_ontology(onto_filename).load()
