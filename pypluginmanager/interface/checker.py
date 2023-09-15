import json
import os

import pypluginmanager
from pypluginmanager.interface.types import InterfaceTypes


def interTypeW(path_config: str, path_repo: str, interface_type: InterfaceTypes):

    with open(path_config, mode='r') as config_file:
        data = json.load(config_file)
        data["interfaces"].update({path_repo: interface_type.name})

    with open(path_config, mode='w') as file:
        json.dump(data, file, indent=4)


def checkVersion(path_config: str):

    with open(path_config, mode='r') as config_file:
        data = json.load(config_file)
        return data["PyPluginManagerVersion"] == pypluginmanager.__version__, data["PyPluginManagerVersion"]


def checkExistence(path_config: str):
    with open(path_config, mode='r') as config_file:
        data = json.load(config_file)

        for interface_path in data["interfaces"]:
            if not os.path.exists(interface_path):
                data.pop(interface_path)

    with open(path_config, mode='w') as file:
        json.dump(data, file, indent=4)
