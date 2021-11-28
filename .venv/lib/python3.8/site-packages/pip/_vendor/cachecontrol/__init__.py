"""CacheControl import Interface.

Make it easy to import from cachecontrol without long namespaces.
"""
__author__ = "Eric Larson"
__email__ = "eric@ionrock.org"
__version__ = "0.12.6"

from .wrapper import CacheControl
from .adapter import CacheControlAdapter
from .controller import CacheController
