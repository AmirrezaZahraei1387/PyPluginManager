"""
defining the different types of interfaces can be
created to interact with a repo.
"""
import enum


class InterfaceTypes(enum.Enum):

    FULL_ACCESS = 0
    NO_DELETE = 1
    LOCKED = 2
    NO_READ = 3
