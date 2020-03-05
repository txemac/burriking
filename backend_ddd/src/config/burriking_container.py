class BurrikingContainer:
    # Here will be the instance stored.
    __instance = None
    dependencies = {}

    @staticmethod
    def get_instance():
        """ Static access method. """
        if BurrikingContainer.__instance is None:
            BurrikingContainer()
        return BurrikingContainer.__instance

    def __init__(self):
        """ Virtually private constructor. """
        if BurrikingContainer.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            BurrikingContainer.__instance = self

    @classmethod
    def get(cls, name):
        if name in cls.dependencies:
            return cls.dependencies[name]
        else:
            return None

    def bind(self, key, instance):
        self.dependencies[key] = instance


def inject(**dependencies):
    def decorator(func):
        def func_wrapper(**params):
            container = BurrikingContainer.get_instance()
            for key, item in dependencies.items():
                params[key] = container.get(item)
            return func(**params)

        return func_wrapper

    return decorator
