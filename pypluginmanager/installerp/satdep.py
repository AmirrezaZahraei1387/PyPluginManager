"""
satisfying the dependencies of the plugin requested
for install.
"""
import sys
import subprocess
import Vmanager


INSTALL_STATE = [sys.executable, '-m', 'pip', 'install', 'name']


def install_package(package_name: str):

    INSTALL_STATE[4] = package_name
    result = subprocess.run(INSTALL_STATE, stdout=subprocess.PIPE)
    return result.stdout, result.returncode


def check_python_version(version: Vmanager.PyVersion):

    python_current_version = Vmanager.PyVersion(sys.version_info[0], sys.version_info[1], sys.version_info[2])
