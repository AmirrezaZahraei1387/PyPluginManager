"""
creating the different sort interfaces with their special
access specifier.
"""

from pypluginmanager.interface.inter_core import CoreInterface
from pypluginmanager.interface.types import InterfaceTypes


# full access
class FullAccessRM(CoreInterface):

    def __init__(self, path):
        super().__init__(path, InterfaceTypes.FULL_ACCESS)


# locked
class LockedRM(CoreInterface):

    def __init__(self, path):
        super().__init__(path, InterfaceTypes.LOCKED)

    def install(self, path):
        raise AttributeError

    def uninstall(self, name: str):
        raise AttributeError

    def get_db(self):
        raise AttributeError

    def load(self, name):
        raise AttributeError


# no delete
class NoDeleteRM(CoreInterface):

    def __init__(self, path):
        super().__init__(path, InterfaceTypes.NO_DELETE)

    def uninstall(self, name: str):
        raise AttributeError

    def install(self, path):
        raise AttributeError


# no read
class NoReadRM(CoreInterface):

    def __init__(self, path):
        super().__init__(path, InterfaceTypes.NO_READ)

    def load(self, name):
        raise AttributeError

    def get_db(self):
        raise AttributeError





