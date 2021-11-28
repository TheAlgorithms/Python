from __future__ import absolute_import, division, unicode_literals

from xml.dom import Node
from ..constants import namespaces, voidElements, spaceCharacters

__all__ = ["DOCUMENT", "DOCTYPE", "TEXT", "ELEMENT", "COMMENT", "ENTITY", "UNKNOWN",
           "TreeWalker", "NonRecursiveTreeWalker"]

DOCUMENT = Node.DOCUMENT_NODE
DOCTYPE = Node.DOCUMENT_TYPE_NODE
TEXT = Node.TEXT_NODE
ELEMENT = Node.ELEMENT_NODE
COMMENT = Node.COMMENT_NODE
ENTITY = Node.ENTITY_NODE
UNKNOWN = "<#UNKNOWN#>"

spaceCharacters = "".join(spaceCharacters)


class TreeWalker(object):
    """Walks a tree yielding tokens

    Tokens are dicts that all have a ``type`` field specifying the type of the
    token.

    """
    def __init__(self, tree):
        """Creates a TreeWalker

        :arg tree: the tree to walk

        """
        self.tree = tree

    def __iter__(self):
        raise NotImplementedError

    def error(self, msg):
        """Generates an error token with the given message

        :arg msg: the error message

        :returns: SerializeError token

        """
        return {"type": "SerializeError", "data": msg}

    def emptyTag(self, namespace, name, attrs, hasChildren=False):
        """Generates an EmptyTag token

        :arg namespace: the namespace of the token--can be ``None``

        :arg name: the name of the element

        :arg attrs: the attributes of the element as a dict

        :arg hasChildren: whether or not to yield a SerializationError because
            this tag shouldn't have children

        :returns: EmptyTag token

        """
        yield {"type": "EmptyTag", "name": name,
               "namespace": namespace,
               "data": attrs}
        if hasChildren:
            yield self.error("Void element has children")

    def startTag(self, namespace, name, attrs):
        """Generates a StartTag token

        :arg namespace: the namespace of the token--can be ``None``

        :arg name: the name of the element

        :arg attrs: the attributes of the element as a dict

        :returns: StartTag token

        """
        return {"type": "StartTag",
                "name": name,
                "namespace": namespace,
                "data": attrs}

    def endTag(self, namespace, name):
        """Generates an EndTag token

        :arg namespace: the namespace of the token--can be ``None``

        :arg name: the name of the element

        :returns: EndTag token

        """
        return {"type": "EndTag",
                "name": name,
                "namespace": namespace}

    def text(self, data):
        """Generates SpaceCharacters and Characters tokens

        Depending on what's in the data, this generates one or more
        ``SpaceCharacters`` and ``Characters`` tokens.

        For example:

            >>> from html5lib.treewalkers.base import TreeWalker
            >>> # Give it an empty tree just so it instantiates
            >>> walker = TreeWalker([])
            >>> list(walker.text(''))
            []
            >>> list(walker.text('  '))
            [{u'data': '  ', u'type': u'SpaceCharacters'}]
            >>> list(walker.text(' abc '))  # doctest: +NORMALIZE_WHITESPACE
            [{u'data': ' ', u'type': u'SpaceCharacters'},
            {u'data': u'abc', u'type': u'Characters'},
            {u'data': u' ', u'type': u'SpaceCharacters'}]

        :arg data: the text data

        :returns: one or more ``SpaceCharacters`` and ``Characters`` tokens

        """
        data = data
        middle = data.lstrip(spaceCharacters)
        left = data[:len(data) - len(middle)]
        if left:
            yield {"type": "SpaceCharacters", "data": left}
        data = middle
        middle = data.rstrip(spaceCharacters)
        right = data[len(middle):]
        if middle:
            yield {"type": "Characters", "data": middle}
        if right:
            yield {"type": "SpaceCharacters", "data": right}

    def comment(self, data):
        """Generates a Comment token

        :arg data: the comment

        :returns: Comment token

        """
        return {"type": "Comment", "data": data}

    def doctype(self, name, publicId=None, systemId=None):
        """Generates a Doctype token

        :arg name:

        :arg publicId:

        :arg systemId:

        :returns: the Doctype token

        """
        return {"type": "Doctype",
                "name": name,
                "publicId": publicId,
                "systemId": systemId}

    def entity(self, name):
        """Generates an Entity token

        :arg name: the entity name

        :returns: an Entity token

        """
        return {"type": "Entity", "name": name}

    def unknown(self, nodeType):
        """Handles unknown node types"""
        return self.error("Unknown node type: " + nodeType)


class NonRecursiveTreeWalker(TreeWalker):
    def getNodeDetails(self, node):
        raise NotImplementedError

    def getFirstChild(self, node):
        raise NotImplementedError

    def getNextSibling(self, node):
        raise NotImplementedError

    def getParentNode(self, node):
        raise NotImplementedError

    def __iter__(self):
        currentNode = self.tree
        while currentNode is not None:
            details = self.getNodeDetails(currentNode)
            type, details = details[0], details[1:]
            hasChildren = False

            if type == DOCTYPE:
                yield self.doctype(*details)

            elif type == TEXT:
                for token in self.text(*details):
                    yield token

            elif type == ELEMENT:
                namespace, name, attributes, hasChildren = details
                if (not namespace or namespace == namespaces["html"]) and name in voidElements:
                    for token in self.emptyTag(namespace, name, attributes,
                                               hasChildren):
                        yield token
                    hasChildren = False
                else:
                    yield self.startTag(namespace, name, attributes)

            elif type == COMMENT:
                yield self.comment(details[0])

            elif type == ENTITY:
                yield self.entity(details[0])

            elif type == DOCUMENT:
                hasChildren = True

            else:
                yield self.unknown(details[0])

            if hasChildren:
                firstChild = self.getFirstChild(currentNode)
            else:
                firstChild = None

            if firstChild is not None:
                currentNode = firstChild
            else:
                while currentNode is not None:
                    details = self.getNodeDetails(currentNode)
                    type, details = details[0], details[1:]
                    if type == ELEMENT:
                        namespace, name, attributes, hasChildren = details
                        if (namespace and namespace != namespaces["html"]) or name not in voidElements:
                            yield self.endTag(namespace, name)
                    if self.tree is currentNode:
                        currentNode = None
                        break
                    nextSibling = self.getNextSibling(currentNode)
                    if nextSibling is not None:
                        currentNode = nextSibling
                        break
                    else:
                        currentNode = self.getParentNode(currentNode)
