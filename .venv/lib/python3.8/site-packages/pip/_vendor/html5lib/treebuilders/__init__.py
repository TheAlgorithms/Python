"""A collection of modules for building different kinds of trees from HTML
documents.

To create a treebuilder for a new type of tree, you need to do
implement several things:

1. A set of classes for various types of elements: Document, Doctype, Comment,
   Element. These must implement the interface of ``base.treebuilders.Node``
   (although comment nodes have a different signature for their constructor,
   see ``treebuilders.etree.Comment``) Textual content may also be implemented
   as another node type, or not, as your tree implementation requires.

2. A treebuilder object (called ``TreeBuilder`` by convention) that inherits
   from ``treebuilders.base.TreeBuilder``. This has 4 required attributes:

   * ``documentClass`` - the class to use for the bottommost node of a document
   * ``elementClass`` - the class to use for HTML Elements
   * ``commentClass`` - the class to use for comments
   * ``doctypeClass`` - the class to use for doctypes

   It also has one required method:

   * ``getDocument`` - Returns the root node of the complete document tree

3. If you wish to run the unit tests, you must also create a ``testSerializer``
   method on your treebuilder which accepts a node and returns a string
   containing Node and its children serialized according to the format used in
   the unittests

"""

from __future__ import absolute_import, division, unicode_literals

from .._utils import default_etree

treeBuilderCache = {}


def getTreeBuilder(treeType, implementation=None, **kwargs):
    """Get a TreeBuilder class for various types of trees with built-in support

    :arg treeType: the name of the tree type required (case-insensitive). Supported
        values are:

        * "dom" - A generic builder for DOM implementations, defaulting to a
          xml.dom.minidom based implementation.
        * "etree" - A generic builder for tree implementations exposing an
          ElementTree-like interface, defaulting to xml.etree.cElementTree if
          available and xml.etree.ElementTree if not.
        * "lxml" - A etree-based builder for lxml.etree, handling limitations
          of lxml's implementation.

    :arg implementation: (Currently applies to the "etree" and "dom" tree
        types). A module implementing the tree type e.g. xml.etree.ElementTree
        or xml.etree.cElementTree.

    :arg kwargs: Any additional options to pass to the TreeBuilder when
        creating it.

    Example:

    >>> from html5lib.treebuilders import getTreeBuilder
    >>> builder = getTreeBuilder('etree')

    """

    treeType = treeType.lower()
    if treeType not in treeBuilderCache:
        if treeType == "dom":
            from . import dom
            # Come up with a sane default (pref. from the stdlib)
            if implementation is None:
                from xml.dom import minidom
                implementation = minidom
            # NEVER cache here, caching is done in the dom submodule
            return dom.getDomModule(implementation, **kwargs).TreeBuilder
        elif treeType == "lxml":
            from . import etree_lxml
            treeBuilderCache[treeType] = etree_lxml.TreeBuilder
        elif treeType == "etree":
            from . import etree
            if implementation is None:
                implementation = default_etree
            # NEVER cache here, caching is done in the etree submodule
            return etree.getETreeModule(implementation, **kwargs).TreeBuilder
        else:
            raise ValueError("""Unrecognised treebuilder "%s" """ % treeType)
    return treeBuilderCache.get(treeType)
