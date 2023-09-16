import json
import os
import sys
import warnings

import pypluginmanager
from pypluginmanager.interface.types import InterfaceTypes
from pypluginmanager.interface import checker


class CoreInterface:

    __type: InterfaceTypes

    def __init__(self, path_repo: str, interface_type: InterfaceTypes):

        self.__type = interface_type

        # saving the paths needed
        self.__plugins_db = os.path.join(path_repo, "config/plugins.json")
        self.__plugins_dir = os.path.join(path_repo, "plugins")

        config_path = os.path.join(path_repo, "config/config.json")
        checker.interTypeW(config_path, sys.argv[0], self.__type)

        is_ok_v, v = checker.checkVersion(config_path)
        if not is_ok_v:
            warnings.warn("the repository in path " + path_repo + " needs version " +
                          v + " but is being opened with version " + pypluginmanager.__version__)
        checker.checkExistence(config_path)

    def install(self, plugin_path):

        with open(os.path.join(plugin_path, "plugin_config.json"), mode='r') as file:
            data = json.load(file)



