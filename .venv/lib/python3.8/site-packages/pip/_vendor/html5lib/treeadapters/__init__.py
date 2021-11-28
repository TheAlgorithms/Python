"""Tree adapters let you convert from one tree structure to another

Example:

.. code-block:: python

   from pip._vendor import html5lib
   from pip._vendor.html5lib.treeadapters import genshi

   doc = '<html><body>Hi!</body></html>'
   treebuilder = html5lib.getTreeBuilder('etree')
   parser = html5lib.HTMLParser(tree=treebuilder)
   tree = parser.parse(doc)
   TreeWalker = html5lib.getTreeWalker('etree')

   genshi_tree = genshi.to_genshi(TreeWalker(tree))

"""
from __future__ import absolute_import, division, unicode_literals

from . import sax

__all__ = ["sax"]

try:
    from . import genshi  # noqa
except ImportError:
    pass
else:
    __all__.append("genshi")
