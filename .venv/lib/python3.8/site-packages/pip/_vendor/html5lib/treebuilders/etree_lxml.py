"""Module for supporting the lxml.etree library. The idea here is to use as much
of the native library as possible, without using fragile hacks like custom element
names that break between releases. The downside of this is that we cannot represent
all possible trees; specifically the following are known to cause problems:

Text or comments as siblings of the root element
Docypes with no name

When any of these things occur, we emit a DataLossWarning
"""

from __future__ import absolute_import, division, unicode_literals
# pylint:disable=protected-access

import warnings
import re
import sys

try:
    from collections.abc import MutableMapping
except ImportError:
    from collections import MutableMapping

from . import base
from ..constants import DataLossWarning
from .. import constants
from . import etree as etree_builders
from .. import _ihatexml

import lxml.etree as etree
from pip._vendor.six import PY3, binary_type


fullTree = True
tag_regexp = re.compile("{([^}]*)}(.*)")

comment_type = etree.Comment("asd").tag


class DocumentType(object):
    def __init__(self, name, publicId, systemId):
        self.name = name
        self.publicId = publicId
        self.systemId = systemId


class Document(object):
    def __init__(self):
        self._elementTree = None
        self._childNodes = []

    def appendChild(self, element):
        last = self._elementTree.getroot()
        for last in self._elementTree.getroot().itersiblings():
            pass

        last.addnext(element._element)

    def _getChildNodes(self):
        return self._childNodes

    childNodes = property(_getChildNodes)


def testSerializer(element):
    rv = []
    infosetFilter = _ihatexml.InfosetFilter(preventDoubleDashComments=True)

    def serializeElement(element, indent=0):
        if not hasattr(element, "tag"):
            if hasattr(element, "getroot"):
                # Full tree case
                rv.append("#document")
                if element.docinfo.internalDTD:
                    if not (element.docinfo.public_id or
                            element.docinfo.system_url):
                        dtd_str = "<!DOCTYPE %s>" % element.docinfo.root_name
                    else:
                        dtd_str = """<!DOCTYPE %s "%s" "%s">""" % (
                            element.docinfo.root_name,
                            element.docinfo.public_id,
                            element.docinfo.system_url)
                    rv.append("|%s%s" % (' ' * (indent + 2), dtd_str))
                next_element = element.getroot()
                while next_element.getprevious() is not None:
                    next_element = next_element.getprevious()
                while next_element is not None:
                    serializeElement(next_element, indent + 2)
                    next_element = next_element.getnext()
            elif isinstance(element, str) or isinstance(element, bytes):
                # Text in a fragment
                assert isinstance(element, str) or sys.version_info[0] == 2
                rv.append("|%s\"%s\"" % (' ' * indent, element))
            else:
                # Fragment case
                rv.append("#document-fragment")
                for next_element in element:
                    serializeElement(next_element, indent + 2)
        elif element.tag == comment_type:
            rv.append("|%s<!-- %s -->" % (' ' * indent, element.text))
            if hasattr(element, "tail") and element.tail:
                rv.append("|%s\"%s\"" % (' ' * indent, element.tail))
        else:
            assert isinstance(element, etree._Element)
            nsmatch = etree_builders.tag_regexp.match(element.tag)
            if nsmatch is not None:
                ns = nsmatch.group(1)
                tag = nsmatch.group(2)
                prefix = constants.prefixes[ns]
                rv.append("|%s<%s %s>" % (' ' * indent, prefix,
                                          infosetFilter.fromXmlName(tag)))
            else:
                rv.append("|%s<%s>" % (' ' * indent,
                                       infosetFilter.fromXmlName(element.tag)))

            if hasattr(element, "attrib"):
                attributes = []
                for name, value in element.attrib.items():
                    nsmatch = tag_regexp.match(name)
                    if nsmatch is not None:
                        ns, name = nsmatch.groups()
                        name = infosetFilter.fromXmlName(name)
                        prefix = constants.prefixes[ns]
                        attr_string = "%s %s" % (prefix, name)
                    else:
                        attr_string = infosetFilter.fromXmlName(name)
                    attributes.append((attr_string, value))

                for name, value in sorted(attributes):
                    rv.append('|%s%s="%s"' % (' ' * (indent + 2), name, value))

            if element.text:
                rv.append("|%s\"%s\"" % (' ' * (indent + 2), element.text))
            indent += 2
            for child in element:
                serializeElement(child, indent)
            if hasattr(element, "tail") and element.tail:
                rv.append("|%s\"%s\"" % (' ' * (indent - 2), element.tail))
    serializeElement(element, 0)

    return "\n".join(rv)


def tostring(element):
    """Serialize an element and its child nodes to a string"""
    rv = []

    def serializeElement(element):
        if not hasattr(element, "tag"):
            if element.docinfo.internalDTD:
                if element.docinfo.doctype:
                    dtd_str = element.docinfo.doctype
                else:
                    dtd_str = "<!DOCTYPE %s>" % element.docinfo.root_name
                rv.append(dtd_str)
            serializeElement(element.getroot())

        elif element.tag == comment_type:
            rv.append("<!--%s-->" % (element.text,))

        else:
            # This is assumed to be an ordinary element
            if not element.attrib:
                rv.append("<%s>" % (element.tag,))
            else:
                attr = " ".join(["%s=\"%s\"" % (name, value)
                                 for name, value in element.attrib.items()])
                rv.append("<%s %s>" % (element.tag, attr))
            if element.text:
                rv.append(element.text)

            for child in element:
                serializeElement(child)

            rv.append("</%s>" % (element.tag,))

        if hasattr(element, "tail") and element.tail:
            rv.append(element.tail)

    serializeElement(element)

    return "".join(rv)


class TreeBuilder(base.TreeBuilder):
    documentClass = Document
    doctypeClass = DocumentType
    elementClass = None
    commentClass = None
    fragmentClass = Document
    implementation = etree

    def __init__(self, namespaceHTMLElements, fullTree=False):
        builder = etree_builders.getETreeModule(etree, fullTree=fullTree)
        infosetFilter = self.infosetFilter = _ihatexml.InfosetFilter(preventDoubleDashComments=True)
        self.namespaceHTMLElements = namespaceHTMLElements

        class Attributes(MutableMapping):
            def __init__(self, element):
                self._element = element

            def _coerceKey(self, key):
                if isinstance(key, tuple):
                    name = "{%s}%s" % (key[2], infosetFilter.coerceAttribute(key[1]))
                else:
                    name = infosetFilter.coerceAttribute(key)
                return name

            def __getitem__(self, key):
                value = self._element._element.attrib[self._coerceKey(key)]
                if not PY3 and isinstance(value, binary_type):
                    value = value.decode("ascii")
                return value

            def __setitem__(self, key, value):
                self._element._element.attrib[self._coerceKey(key)] = value

            def __delitem__(self, key):
                del self._element._element.attrib[self._coerceKey(key)]

            def __iter__(self):
                return iter(self._element._element.attrib)

            def __len__(self):
                return len(self._element._element.attrib)

            def clear(self):
                return self._element._element.attrib.clear()

        class Element(builder.Element):
            def __init__(self, name, namespace):
                name = infosetFilter.coerceElement(name)
                builder.Element.__init__(self, name, namespace=namespace)
                self._attributes = Attributes(self)

            def _setName(self, name):
                self._name = infosetFilter.coerceElement(name)
                self._element.tag = self._getETreeTag(
                    self._name, self._namespace)

            def _getName(self):
                return infosetFilter.fromXmlName(self._name)

            name = property(_getName, _setName)

            def _getAttributes(self):
                return self._attributes

            def _setAttributes(self, value):
                attributes = self.attributes
                attributes.clear()
                attributes.update(value)

            attributes = property(_getAttributes, _setAttributes)

            def insertText(self, data, insertBefore=None):
                data = infosetFilter.coerceCharacters(data)
                builder.Element.insertText(self, data, insertBefore)

            def cloneNode(self):
                element = type(self)(self.name, self.namespace)
                if self._element.attrib:
                    element._element.attrib.update(self._element.attrib)
                return element

        class Comment(builder.Comment):
            def __init__(self, data):
                data = infosetFilter.coerceComment(data)
                builder.Comment.__init__(self, data)

            def _setData(self, data):
                data = infosetFilter.coerceComment(data)
                self._element.text = data

            def _getData(self):
                return self._element.text

            data = property(_getData, _setData)

        self.elementClass = Element
        self.commentClass = Comment
        # self.fragmentClass = builder.DocumentFragment
        base.TreeBuilder.__init__(self, namespaceHTMLElements)

    def reset(self):
        base.TreeBuilder.reset(self)
        self.insertComment = self.insertCommentInitial
        self.initial_comments = []
        self.doctype = None

    def testSerializer(self, element):
        return testSerializer(element)

    def getDocument(self):
        if fullTree:
            return self.document._elementTree
        else:
            return self.document._elementTree.getroot()

    def getFragment(self):
        fragment = []
        element = self.openElements[0]._element
        if element.text:
            fragment.append(element.text)
        fragment.extend(list(element))
        if element.tail:
            fragment.append(element.tail)
        return fragment

    def insertDoctype(self, token):
        name = token["name"]
        publicId = token["publicId"]
        systemId = token["systemId"]

        if not name:
            warnings.warn("lxml cannot represent empty doctype", DataLossWarning)
            self.doctype = None
        else:
            coercedName = self.infosetFilter.coerceElement(name)
            if coercedName != name:
                warnings.warn("lxml cannot represent non-xml doctype", DataLossWarning)

            doctype = self.doctypeClass(coercedName, publicId, systemId)
            self.doctype = doctype

    def insertCommentInitial(self, data, parent=None):
        assert parent is None or parent is self.document
        assert self.document._elementTree is None
        self.initial_comments.append(data)

    def insertCommentMain(self, data, parent=None):
        if (parent == self.document and
                self.document._elementTree.getroot()[-1].tag == comment_type):
            warnings.warn("lxml cannot represent adjacent comments beyond the root elements", DataLossWarning)
        super(TreeBuilder, self).insertComment(data, parent)

    def insertRoot(self, token):
        # Because of the way libxml2 works, it doesn't seem to be possible to
        # alter information like the doctype after the tree has been parsed.
        # Therefore we need to use the built-in parser to create our initial
        # tree, after which we can add elements like normal
        docStr = ""
        if self.doctype:
            assert self.doctype.name
            docStr += "<!DOCTYPE %s" % self.doctype.name
            if (self.doctype.publicId is not None or
                    self.doctype.systemId is not None):
                docStr += (' PUBLIC "%s" ' %
                           (self.infosetFilter.coercePubid(self.doctype.publicId or "")))
                if self.doctype.systemId:
                    sysid = self.doctype.systemId
                    if sysid.find("'") >= 0 and sysid.find('"') >= 0:
                        warnings.warn("DOCTYPE system cannot contain single and double quotes", DataLossWarning)
                        sysid = sysid.replace("'", 'U00027')
                    if sysid.find("'") >= 0:
                        docStr += '"%s"' % sysid
                    else:
                        docStr += "'%s'" % sysid
                else:
                    docStr += "''"
            docStr += ">"
            if self.doctype.name != token["name"]:
                warnings.warn("lxml cannot represent doctype with a different name to the root element", DataLossWarning)
        docStr += "<THIS_SHOULD_NEVER_APPEAR_PUBLICLY/>"
        root = etree.fromstring(docStr)

        # Append the initial comments:
        for comment_token in self.initial_comments:
            comment = self.commentClass(comment_token["data"])
            root.addprevious(comment._element)

        # Create the root document and add the ElementTree to it
        self.document = self.documentClass()
        self.document._elementTree = root.getroottree()

        # Give the root element the right name
        name = token["name"]
        namespace = token.get("namespace", self.defaultNamespace)
        if namespace is None:
            etree_tag = name
        else:
            etree_tag = "{%s}%s" % (namespace, name)
        root.tag = etree_tag

        # Add the root element to the internal child/open data structures
        root_element = self.elementClass(name, namespace)
        root_element._element = root
        self.document._childNodes.append(root_element)
        self.openElements.append(root_element)

        # Reset to the default insert comment function
        self.insertComment = self.insertCommentMain
