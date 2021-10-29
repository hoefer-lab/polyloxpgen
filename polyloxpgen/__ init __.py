
"""polyloxpgen - Barcode purging and pgen (probability of generation) calculation for Polylox data."""

__version__ = '0.1.1'
__author__ = 'Maurice Langhinrichs <m.langhinrichs@icloud.com>'

# __all__ applies to importing with "from polyloxpgen import *"
__all__ = ['merge', 'pgen']

# to be able to use "import polyloxpgen" and "polyloxpgen.polylox_merge()":
# NOTE: this does not seem to work currently...
# but using separate imports works: import polyloxpgen.merge, etc.
from .merge import polylox_merge
from .pgen import polylox_pgen
# import merge
# import pgen
# import merge.polylox_merge
# import pgen.polylox_pgen
