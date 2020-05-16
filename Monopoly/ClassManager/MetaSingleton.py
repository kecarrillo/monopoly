class MetaSingleton(type):
    """Class which inherits from type class (which contains all classes).
    """
    __instance = None

    def __call__(cls):
        """Method invoked when this class is called.

        :param cls: class to instance.
        :return: instance of the class if still not instanced.
        """
        if cls.__instance is None:
            cls.__instance = super(MetaSingleton, cls).__call__()
        return cls.__instance
