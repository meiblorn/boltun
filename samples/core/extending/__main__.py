from boltun.engine import Engine
from boltun.engine.environment import Extension

class FilterDef(object):
    pass

class FunctionDef(object):
    pass

class CustomExtension(Extension):

    def __namespaces__(self):
        return []

    def __functions__(self):
        return [
            FunctionDef(names=['env'], callable=self.env_func)
        ]

    def __filters__(self):
        return [
            FilterDef(names=['lower'], callable=self.env_func)
        ]

    def env_func(self):
        pass

if __name__ == '__main__':
    engine = Engine()
    environment = engine.get_default_environment()
    environment.add_extension(CustomExtension())