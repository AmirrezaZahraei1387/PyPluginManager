

class PluginNotFoundError(Exception):
    """raised when a plugin attempted to be installed deleted or do
    any other operation does not exist."""
    def __init__(self, msg):
        super().__init__(msg)


class PluginFoundError(Exception):
    """raised when a plugin exist in the repository under
    some special operations"""
    def __init__(self, msg):
        super().__init__(msg)

