import sys
from types import ModuleType


class module(ModuleType):
    def __getattr__(self, name):
        from .tags import tag
        return lambda *a, **kw: tag(name, *a, **kw)


# keep a reference to this module so that it's not garbage collected
old_module = sys.modules['htmler.fun']

# setup the new module and patch it into the dict of loaded modules
new_module = sys.modules['htmler.fun'] = module('htmler.fun')
