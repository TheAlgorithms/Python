from __future__ import absolute_import, division, unicode_literals

from xml.sax.xmlreader import AttributesNSImpl

from ..constants import adjustForeignAttributes, unadjustForeignAttributes

prefix_mapping = {}
for prefix, localName, namespace in adjustForeignAttributes.values():
    if prefix is not None:
        prefix_mapping[prefix] = namespace


def to_sax(walker, handler):
    """Call SAX-like content handler based on treewalker walker

    :arg walker: the treewalker to use to walk the tree to convert it

    :arg handler: SAX handler to use

    """
    handler.startDocument()
    for prefix, namespace in prefix_mapping.items():
        handler.startPrefixMapping(prefix, namespace)

    for token in walker:
        type = token["type"]
        if type == "Doctype":
            continue
        elif type in ("StartTag", "EmptyTag"):
            attrs = AttributesNSImpl(token["data"],
                                     unadjustForeignAttributes)
            handler.startElementNS((token["namespace"], token["name"]),
                                   token["name"],
                                   attrs)
            if type == "EmptyTag":
                handler.endElementNS((token["namespace"], token["name"]),
                                     token["name"])
        elif type == "EndTag":
            handler.endElementNS((token["namespace"], token["name"]),
                                 token["name"])
        elif type in ("Characters", "SpaceCharacters"):
            handler.characters(token["data"])
        elif type == "Comment":
            pass
        else:
            assert False, "Unknown token type"

    for prefix, namespace in prefix_mapping.items():
        handler.endPrefixMapping(prefix)
    handler.endDocument()
