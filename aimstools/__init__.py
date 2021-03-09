"""aimstools"""

import sys
from distutils.version import LooseVersion

if sys.version_info[0] == 2:
    raise ImportError("Requires Python3. This is Python2.")

__version__ = "0.5.8"


from aimstools.structuretools import Structure
from aimstools.bandstructures import BandStructure
from aimstools.density_of_states import DensityOfStates


__all__ = ["Structure", "BandStructure", "DensityOfStates"]
