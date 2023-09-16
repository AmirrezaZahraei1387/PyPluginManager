"""
satisfying the dependencies of the plugin requested
for install.
"""
import sys
import subprocess
from Vmanager import PyVersion
import re


INSTALL_STATE = [sys.executable, '-m', 'pip', 'install', 'name']
python_current_version = PyVersion(sys.version_info[0], sys.version_info[1], sys.version_info[2])


def install_package(package_name: str):
    INSTALL_STATE[4] = package_name
    result = subprocess.run(INSTALL_STATE, stdout=subprocess.PIPE)
    return result.stdout, result.returncode


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
