from __future__ import absolute_import, division, unicode_literals
from pip._vendor.six import text_type

from collections import OrderedDict

from lxml import etree
from ..treebuilders.etree import tag_regexp

from . import base

from .. import _ihatexml


def ensure_str(s):
    if s is None:
        return None
    elif isinstance(s, text_type):
        return s
    else:
        return s.decode("ascii", "strict")


class Root(object):
    def __init__(self, et):
        self.elementtree = et
        self.children = []

        try:
            if et.docinfo.internalDTD:
                self.children.append(Doctype(self,
                                             ensure_str(et.docinfo.root_name),
                                             ensure_str(et.docinfo.public_id),
                                             ensure_str(et.docinfo.system_url)))
        except AttributeError:
            pass

        try:
            node = et.getroot()
        except AttributeError:
            node = et

        while node.getprevious() is not None:
            node = node.getprevious()
        while node is not None:
            self.children.append(node)
            node = node.getnext()

        self.text = None
        self.tail = None

    def __getitem__(self, key):
        return self.children[key]

    def getnext(self):
        return None

    def __len__(self):
        return 1


class Doctype(object):
    def __init__(self, root_node, name, public_id, system_id):
        self.root_node = root_node
        self.name = name
        self.public_id = public_id
        self.system_id = system_id

        self.text = None
        self.tail = None

    def getnext(self):
        return self.root_node.children[1]


class FragmentRoot(Root):
    def __init__(self, children):
        self.children = [FragmentWrapper(self, child) for child in children]
        self.text = self.tail = None

    def getnext(self):
        return None


class FragmentWrapper(object):
    def __init__(self, fragment_root, obj):
        self.root_node = fragment_root
        self.obj = obj
        if hasattr(self.obj, 'text'):
            self.text = ensure_str(self.obj.text)
        else:
            self.text = None
        if hasattr(self.obj, 'tail'):
            self.tail = ensure_str(self.obj.tail)
        else:
            self.tail = None

    def __getattr__(self, name):
        return getattr(self.obj, name)

    def getnext(self):
        siblings = self.root_node.children
        idx = siblings.index(self)
        if idx < len(siblings) - 1:
            return siblings[idx + 1]
        else:
            return None

    def __getitem__(self, key):
        return self.obj[key]

    def __bool__(self):
        return bool(self.obj)

    def getparent(self):
        return None

    def __str__(self):
        return str(self.obj)

    def __unicode__(self):
        return str(self.obj)

    def __len__(self):
        return len(self.obj)


class TreeWalker(base.NonRecursiveTreeWalker):
    def __init__(self, tree):
        # pylint:disable=redefined-variable-type
        if isinstance(tree, list):
            self.fragmentChildren = set(tree)
            tree = FragmentRoot(tree)
        else:
            self.fragmentChildren = set()
            tree = Root(tree)
        base.NonRecursiveTreeWalker.__init__(self, tree)
        self.filter = _ihatexml.InfosetFilter()

    def getNodeDetails(self, node):
        if isinstance(node, tuple):  # Text node
            node, key = node
            assert key in ("text", "tail"), "Text nodes are text or tail, found %s" % key
            return base.TEXT, ensure_str(getattr(node, key))

        elif isinstance(node, Root):
            return (base.DOCUMENT,)

        elif isinstance(node, Doctype):
            return base.DOCTYPE, node.name, node.public_id, node.system_id

        elif isinstance(node, FragmentWrapper) and not hasattr(node, "tag"):
            return base.TEXT, ensure_str(node.obj)

        elif node.tag == etree.Comment:
            return base.COMMENT, ensure_str(node.text)

        elif node.tag == etree.Entity:
            return base.ENTITY, ensure_str(node.text)[1:-1]  # strip &;

        else:
            # This is assumed to be an ordinary element
            match = tag_regexp.match(ensure_str(node.tag))
            if match:
                namespace, tag = match.groups()
            else:
                namespace = None
                tag = ensure_str(node.tag)
            attrs = OrderedDict()
            for name, value in list(node.attrib.items()):
                name = ensure_str(name)
                value = ensure_str(value)
                match = tag_regexp.match(name)
                if match:
                    attrs[(match.group(1), match.group(2))] = value
                else:
                    attrs[(None, name)] = value
            return (base.ELEMENT, namespace, self.filter.fromXmlName(tag),
                    attrs, len(node) > 0 or node.text)

    def getFirstChild(self, node):
        assert not isinstance(node, tuple), "Text nodes have no children"

        assert len(node) or node.text, "Node has no children"
        if node.text:
            return (node, "text")
        else:
            return node[0]

    def getNextSibling(self, node):
        if isinstance(node, tuple):  # Text node
            node, key = node
            assert key in ("text", "tail"), "Text nodes are text or tail, found %s" % key
            if key == "text":
                # XXX: we cannot use a "bool(node) and node[0] or None" construct here
                # because node[0] might evaluate to False if it has no child element
                if len(node):
                    return node[0]
                else:
                    return None
            else:  # tail
                return node.getnext()

        return (node, "tail") if node.tail else node.getnext()

    def getParentNode(self, node):
        if isinstance(node, tuple):  # Text node
            node, key = node
            assert key in ("text", "tail"), "Text nodes are text or tail, found %s" % key
            if key == "text":
                return node
            # else: fallback to "normal" processing
        elif node in self.fragmentChildren:
            return None

        return node.getparent()
