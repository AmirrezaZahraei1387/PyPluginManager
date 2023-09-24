import json
import os

import pypluginmanager
from pypluginmanager.interface import InterfaceTypes


MANDATORY_PARA = ["name", "version", "python-version", "dependencies", "install-path"]


def interTypeW(path_config: str, path_interface: str, interface_type: InterfaceTypes):

    with open(path_config, mode='r') as config_file:
        data = json.load(config_file)
        data["interfaces"].update({path_interface: interface_type.name})

    with open(path_config, mode='w') as file:
        json.dump(data, file, indent=4)


def checkVersion(path_config: str):

    with open(path_config, mode='r') as config_file:
        data = json.load(config_file)
        return data["PyPluginManagerVersion"] == pypluginmanager.__version__, data["PyPluginManagerVersion"]


def has_key(dict_: dict, key):
    if key not in dict_:
        raise KeyError("no "+str(key)+"exist")


def checkExistence(path_config: str):
    with open(path_config, mode='r') as config_file:
        data = json.load(config_file)

        for interface_path in data["interfaces"]:
            if not os.path.exists(interface_path):
                data.pop(interface_path)

    with open(path_config, mode='w') as file:
        json.dump(data, file, indent=4)


def check_existance_l(data: dict, to_check: list):
    for element in to_check:
        has_key(data, element)


