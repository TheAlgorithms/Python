"""A collection of modules for iterating through different kinds of
tree, generating tokens identical to those produced by the tokenizer
module.

To create a tree walker for a new type of tree, you need to
implement a tree walker object (called TreeWalker by convention) that
implements a 'serialize' method which takes a tree as sole argument and
returns an iterator which generates tokens.
"""

from __future__ import absolute_import, division, unicode_literals

from .. import constants
from .._utils import default_etree

__all__ = ["getTreeWalker", "pprint"]

treeWalkerCache = {}


def getTreeWalker(treeType, implementation=None, **kwargs):
    """Get a TreeWalker class for various types of tree with built-in support

    :arg str treeType: the name of the tree type required (case-insensitive).
        Supported values are:

        * "dom": The xml.dom.minidom DOM implementation
        * "etree": A generic walker for tree implementations exposing an
          elementtree-like interface (known to work with ElementTree,
          cElementTree and lxml.etree).
        * "lxml": Optimized walker for lxml.etree
        * "genshi": a Genshi stream

    :arg implementation: A module implementing the tree type e.g.
        xml.etree.ElementTree or cElementTree (Currently applies to the "etree"
        tree type only).

    :arg kwargs: keyword arguments passed to the etree walker--for other
        walkers, this has no effect

    :returns: a TreeWalker class

    """

    treeType = treeType.lower()
    if treeType not in treeWalkerCache:
        if treeType == "dom":
            from . import dom
            treeWalkerCache[treeType] = dom.TreeWalker
        elif treeType == "genshi":
            from . import genshi
            treeWalkerCache[treeType] = genshi.TreeWalker
        elif treeType == "lxml":
            from . import etree_lxml
            treeWalkerCache[treeType] = etree_lxml.TreeWalker
        elif treeType == "etree":
            from . import etree
            if implementation is None:
                implementation = default_etree
            # XXX: NEVER cache here, caching is done in the etree submodule
            return etree.getETreeModule(implementation, **kwargs).TreeWalker
    return treeWalkerCache.get(treeType)


def concatenateCharacterTokens(tokens):
    pendingCharacters = []
    for token in tokens:
        type = token["type"]
        if type in ("Characters", "SpaceCharacters"):
            pendingCharacters.append(token["data"])
        else:
            if pendingCharacters:
                yield {"type": "Characters", "data": "".join(pendingCharacters)}
                pendingCharacters = []
            yield token
    if pendingCharacters:
        yield {"type": "Characters", "data": "".join(pendingCharacters)}


def pprint(walker):
    """Pretty printer for tree walkers

    Takes a TreeWalker instance and pretty prints the output of walking the tree.

    :arg walker: a TreeWalker instance

    """
    output = []
    indent = 0
    for token in concatenateCharacterTokens(walker):
        type = token["type"]
        if type in ("StartTag", "EmptyTag"):
            # tag name
            if token["namespace"] and token["namespace"] != constants.namespaces["html"]:
                if token["namespace"] in constants.prefixes:
                    ns = constants.prefixes[token["namespace"]]
                else:
                    ns = token["namespace"]
                name = "%s %s" % (ns, token["name"])
            else:
                name = token["name"]
            output.append("%s<%s>" % (" " * indent, name))
            indent += 2
            # attributes (sorted for consistent ordering)
            attrs = token["data"]
            for (namespace, localname), value in sorted(attrs.items()):
                if namespace:
                    if namespace in constants.prefixes:
                        ns = constants.prefixes[namespace]
                    else:
                        ns = namespace
                    name = "%s %s" % (ns, localname)
                else:
                    name = localname
                output.append("%s%s=\"%s\"" % (" " * indent, name, value))
            # self-closing
            if type == "EmptyTag":
                indent -= 2

        elif type == "EndTag":
            indent -= 2

        elif type == "Comment":
            output.append("%s<!-- %s -->" % (" " * indent, token["data"]))

        elif type == "Doctype":
            if token["name"]:
                if token["publicId"]:
                    output.append("""%s<!DOCTYPE %s "%s" "%s">""" %
                                  (" " * indent,
                                   token["name"],
                                   token["publicId"],
                                   token["systemId"] if token["systemId"] else ""))
                elif token["systemId"]:
                    output.append("""%s<!DOCTYPE %s "" "%s">""" %
                                  (" " * indent,
                                   token["name"],
                                   token["systemId"]))
                else:
                    output.append("%s<!DOCTYPE %s>" % (" " * indent,
                                                       token["name"]))
            else:
                output.append("%s<!DOCTYPE >" % (" " * indent,))

        elif type == "Characters":
            output.append("%s\"%s\"" % (" " * indent, token["data"]))

        elif type == "SpaceCharacters":
            assert False, "concatenateCharacterTokens should have got rid of all Space tokens"

        else:
            raise ValueError("Unknown token type, %s" % type)

    return "\n".join(output)
