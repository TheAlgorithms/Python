from __future__ import absolute_import, division, unicode_literals

from genshi.core import QName, Attrs
from genshi.core import START, END, TEXT, COMMENT, DOCTYPE


def to_genshi(walker):
    """Convert a tree to a genshi tree

    :arg walker: the treewalker to use to walk the tree to convert it

    :returns: generator of genshi nodes

    """
    text = []
    for token in walker:
        type = token["type"]
        if type in ("Characters", "SpaceCharacters"):
            text.append(token["data"])
        elif text:
            yield TEXT, "".join(text), (None, -1, -1)
            text = []

        if type in ("StartTag", "EmptyTag"):
            if token["namespace"]:
                name = "{%s}%s" % (token["namespace"], token["name"])
            else:
                name = token["name"]
            attrs = Attrs([(QName("{%s}%s" % attr if attr[0] is not None else attr[1]), value)
                           for attr, value in token["data"].items()])
            yield (START, (QName(name), attrs), (None, -1, -1))
            if type == "EmptyTag":
                type = "EndTag"

        if type == "EndTag":
            if token["namespace"]:
                name = "{%s}%s" % (token["namespace"], token["name"])
            else:
                name = token["name"]

            yield END, QName(name), (None, -1, -1)

        elif type == "Comment":
            yield COMMENT, token["data"], (None, -1, -1)

        elif type == "Doctype":
            yield DOCTYPE, (token["name"], token["publicId"],
                            token["systemId"]), (None, -1, -1)

        else:
            pass  # FIXME: What to do?

    if text:
        yield TEXT, "".join(text), (None, -1, -1)
