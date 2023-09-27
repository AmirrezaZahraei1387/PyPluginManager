__version__ = "0.1"

import pypluginmanager.exceptions.errors as exps

import pypluginmanager.installerp.satdep as inp

from pypluginmanager.interface.types import InterfaceTypes

from pypluginmanager.interface.checker import interTypeW
from pypluginmanager.interface.checker import checkVersion
from pypluginmanager.interface.checker import checkExistence
from pypluginmanager.interface.checker import check_existance_l

from pypluginmanager.interface.inter_core import CoreInterface

import pypluginmanager.interface.interfaces as minterfaces


from pypluginmanager.samplefiles.interface import INTERFACE
from pypluginmanager.samplefiles.interface import PLUGIN_SAMPLE
from pypluginmanager.samplefiles.interface import DEPENDENCIES

