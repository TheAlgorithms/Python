from __future__ import absolute_import, division, unicode_literals

from xml.dom import Node

from . import base


class TreeWalker(base.NonRecursiveTreeWalker):
    def getNodeDetails(self, node):
        if node.nodeType == Node.DOCUMENT_TYPE_NODE:
            return base.DOCTYPE, node.name, node.publicId, node.systemId

        elif node.nodeType in (Node.TEXT_NODE, Node.CDATA_SECTION_NODE):
            return base.TEXT, node.nodeValue

        elif node.nodeType == Node.ELEMENT_NODE:
            attrs = {}
            for attr in list(node.attributes.keys()):
                attr = node.getAttributeNode(attr)
                if attr.namespaceURI:
                    attrs[(attr.namespaceURI, attr.localName)] = attr.value
                else:
                    attrs[(None, attr.name)] = attr.value
            return (base.ELEMENT, node.namespaceURI, node.nodeName,
                    attrs, node.hasChildNodes())

        elif node.nodeType == Node.COMMENT_NODE:
            return base.COMMENT, node.nodeValue

        elif node.nodeType in (Node.DOCUMENT_NODE, Node.DOCUMENT_FRAGMENT_NODE):
            return (base.DOCUMENT,)

        else:
            return base.UNKNOWN, node.nodeType

    def getFirstChild(self, node):
        return node.firstChild

    def getNextSibling(self, node):
        return node.nextSibling

    def getParentNode(self, node):
        return node.parentNode
