import json
import os
import shutil
import sys
import warnings

import pypluginmanager
from pypluginmanager.interface.types import InterfaceTypes
from pypluginmanager.interface import checker
import pypluginmanager.installerp as installerp
import pypluginmanager.exceptions as exps


class CoreInterface:
    __type: InterfaceTypes

    def __init__(self, path_repo: str, interface_type: InterfaceTypes):

        self.__type = interface_type

        # saving the paths needed
        self.__plugins_db = os.path.join(path_repo, "Config\\plugins.json")
        self.__plugins_dir = os.path.join(path_repo, "Plugins")

        config_path = os.path.join(path_repo, "Config\\config.json")
        checker.interTypeW(config_path, sys.argv[0], self.__type)

        is_ok_v, v = checker.checkVersion(config_path)
        if not is_ok_v:
            warnings.warn("the repository in path " + path_repo + " needs version " +
                          v + " but is being opened with version " + pypluginmanager.__version__)
        checker.checkExistence(config_path)

    def install(self, path):

        with open(os.path.join(path, "plugin_config.json"), mode='r') as file:
            data = json.load(file)
            checker.check_existance(data, checker.MANDATORY_PARA)

            if self.plugin_exist(data["name"]):
                raise exps.PluginFoundError("the plugin requested to be installed already"
                                            "exist")

            installerp.check_python_version(data["python-version"])
            result_dep_install = installerp.satisfy_dep(data["dependencies"])
            data["dependencies"] = result_dep_install
            full_installation_path = os.path.join(self.__plugins_dir, data["install-path"])

            shutil.copytree(path, full_installation_path)

            with open(self.__plugins_db, mode='r') as file_r:
                d = json.load(file_r)
                name = data["name"]
                d.update({name: data})

                with open(self.__plugins_db, mode='w') as file_w:
                    json.dump(d, file_w, indent=6)

    def plugin_exist(self, name: str):
        with open(self.__plugins_db, mode='r') as file_r:
            plugins = json.load(file_r)

            for name_ in plugins:
                if name == name_:
                    return True
        return False

    def uninstall(self, name: str):
        with open(self.__plugins_db, mode='r') as file_r:
            plugins = json.load(file_r)

            if not self.plugin_exist(name):
                raise exps.PluginNotFoundError("the plugin specified to be deleted does not exist.")

            path = os.path.join(self.__plugins_dir, plugins[name]["install-path"])
            del plugins[name]
            shutil.rmtree(path)

            with open(self.__plugins_db, mode='w') as file_w:
                json.dump(plugins, file_w, indent=6)


m = CoreInterface("Sample-Repo", InterfaceTypes.FULL_ACCESS)
m.install("plugin")
m.uninstall("Ali")






