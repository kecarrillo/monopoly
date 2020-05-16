from Monopoly.ClassManager.MetaSingleton import MetaSingleton


class Singleton(metaclass=MetaSingleton):
    """Class used to decorate Singletons.
    """
    def __init__(self, decorated):
        """This method is the constructor of the class.
        """
        self._decorated = decorated

    def Instance(self):
        """This method try to access to the instance or create it.

        :return: instance of the decorated class.
        """
        try:  # exist.
            return self._instance
        except AttributeError:  # doesn't exist.
            self._instance = self._decorated()
            return self._instance

    def __call__(self):
        """This method forbid the creation of instance without Instance().

        :return: Error sentence.
        :rtype: string
        """
        raise TypeError('Pour récupérer l\'intance du Singleton, utiliser '
                        'Instance().')
