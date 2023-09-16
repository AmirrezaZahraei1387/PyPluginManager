"""
satisfying the dependencies of the plugin requested
for install.
"""
import sys
import subprocess
import re
import warnings

from Vmanager import PyVersion


INSTALL_STATE = [sys.executable, '-m', 'pip', 'install', 'name']
python_current_version = PyVersion(sys.version_info[0], sys.version_info[1], sys.version_info[2])


def install_package(package_name: str):
    INSTALL_STATE[4] = package_name
    result = subprocess.run(INSTALL_STATE, stdout=subprocess.PIPE)
    return  {package_name:[result.returncode, result.stdout]}


def satisfy_dep(package_names: list):
    dependencies = {}
    for package in package_names:
        result = install_package(package)
        if result[package][0] != 0:
            warnings.warn(result[package][0])
        dependencies.update(install_package(package))
    return dependencies


def check_python_version(version_expr: str):
    tokens = re.search(r"\s*([\d.]+)", version_expr)
    try:
        # it means we have passed a version_expr with a python version
        # domain or exact
        v = tokens.group()

        v_expected = PyVersion().fromstr(v)

        version_expr = version_expr.replace(v, v_expected.__repr__(), 1)

        version_expr = python_current_version.__repr__() + version_expr
        return eval(version_expr)

    except AttributeError:
        return True