import json

import pypluginmanager
from pypluginmanager.interface.types import InterfaceTypes


def interTypeW(path_config: str, path_repo: str, interface_type: InterfaceTypes):

    with open(path_config, mode='r+', newline='') as config_file:
        data = json.load(config_file)
        data["interfaces"].update({path_repo: interface_type.name})
        json.dump(config_file, data)


def checkVersion(path_config: str):

    with open(path_config, mode='r') as config_file:
        data = json.load(config_file)
        return data["PyPluginManagerVersion"] == pypluginmanager.__version__

