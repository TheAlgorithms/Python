from __future__ import absolute_import, division, unicode_literals

from . import base


class Filter(base.Filter):
    """Removes optional tags from the token stream"""
    def slider(self):
        previous1 = previous2 = None
        for token in self.source:
            if previous1 is not None:
                yield previous2, previous1, token
            previous2 = previous1
            previous1 = token
        if previous1 is not None:
            yield previous2, previous1, None

    def __iter__(self):
        for previous, token, next in self.slider():
            type = token["type"]
            if type == "StartTag":
                if (token["data"] or
                        not self.is_optional_start(token["name"], previous, next)):
                    yield token
            elif type == "EndTag":
                if not self.is_optional_end(token["name"], next):
                    yield token
            else:
                yield token

    def is_optional_start(self, tagname, previous, next):
        type = next and next["type"] or None
        if tagname in 'html':
            # An html element's start tag may be omitted if the first thing
            # inside the html element is not a space character or a comment.
            return type not in ("Comment", "SpaceCharacters")
        elif tagname == 'head':
            # A head element's start tag may be omitted if the first thing
            # inside the head element is an element.
            # XXX: we also omit the start tag if the head element is empty
            if type in ("StartTag", "EmptyTag"):
                return True
            elif type == "EndTag":
                return next["name"] == "head"
        elif tagname == 'body':
            # A body element's start tag may be omitted if the first thing
            # inside the body element is not a space character or a comment,
            # except if the first thing inside the body element is a script
            # or style element and the node immediately preceding the body
            # element is a head element whose end tag has been omitted.
            if type in ("Comment", "SpaceCharacters"):
                return False
            elif type == "StartTag":
                # XXX: we do not look at the preceding event, so we never omit
                # the body element's start tag if it's followed by a script or
                # a style element.
                return next["name"] not in ('script', 'style')
            else:
                return True
        elif tagname == 'colgroup':
            # A colgroup element's start tag may be omitted if the first thing
            # inside the colgroup element is a col element, and if the element
            # is not immediately preceded by another colgroup element whose
            # end tag has been omitted.
            if type in ("StartTag", "EmptyTag"):
                # XXX: we do not look at the preceding event, so instead we never
                # omit the colgroup element's end tag when it is immediately
                # followed by another colgroup element. See is_optional_end.
                return next["name"] == "col"
            else:
                return False
        elif tagname == 'tbody':
            # A tbody element's start tag may be omitted if the first thing
            # inside the tbody element is a tr element, and if the element is
            # not immediately preceded by a tbody, thead, or tfoot element
            # whose end tag has been omitted.
            if type == "StartTag":
                # omit the thead and tfoot elements' end tag when they are
                # immediately followed by a tbody element. See is_optional_end.
                if previous and previous['type'] == 'EndTag' and \
                        previous['name'] in ('tbody', 'thead', 'tfoot'):
                    return False
                return next["name"] == 'tr'
            else:
                return False
        return False

    def is_optional_end(self, tagname, next):
        type = next and next["type"] or None
        if tagname in ('html', 'head', 'body'):
            # An html element's end tag may be omitted if the html element
            # is not immediately followed by a space character or a comment.
            return type not in ("Comment", "SpaceCharacters")
        elif tagname in ('li', 'optgroup', 'tr'):
            # A li element's end tag may be omitted if the li element is
            # immediately followed by another li element or if there is
            # no more content in the parent element.
            # An optgroup element's end tag may be omitted if the optgroup
            # element is immediately followed by another optgroup element,
            # or if there is no more content in the parent element.
            # A tr element's end tag may be omitted if the tr element is
            # immediately followed by another tr element, or if there is
            # no more content in the parent element.
            if type == "StartTag":
                return next["name"] == tagname
            else:
                return type == "EndTag" or type is None
        elif tagname in ('dt', 'dd'):
            # A dt element's end tag may be omitted if the dt element is
            # immediately followed by another dt element or a dd element.
            # A dd element's end tag may be omitted if the dd element is
            # immediately followed by another dd element or a dt element,
            # or if there is no more content in the parent element.
            if type == "StartTag":
                return next["name"] in ('dt', 'dd')
            elif tagname == 'dd':
                return type == "EndTag" or type is None
            else:
                return False
        elif tagname == 'p':
            # A p element's end tag may be omitted if the p element is
            # immediately followed by an address, article, aside,
            # blockquote, datagrid, dialog, dir, div, dl, fieldset,
            # footer, form, h1, h2, h3, h4, h5, h6, header, hr, menu,
            # nav, ol, p, pre, section, table, or ul, element, or if
            # there is no more content in the parent element.
            if type in ("StartTag", "EmptyTag"):
                return next["name"] in ('address', 'article', 'aside',
                                        'blockquote', 'datagrid', 'dialog',
                                        'dir', 'div', 'dl', 'fieldset', 'footer',
                                        'form', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6',
                                        'header', 'hr', 'menu', 'nav', 'ol',
                                        'p', 'pre', 'section', 'table', 'ul')
            else:
                return type == "EndTag" or type is None
        elif tagname == 'option':
            # An option element's end tag may be omitted if the option
            # element is immediately followed by another option element,
            # or if it is immediately followed by an <code>optgroup</code>
            # element, or if there is no more content in the parent
            # element.
            if type == "StartTag":
                return next["name"] in ('option', 'optgroup')
            else:
                return type == "EndTag" or type is None
        elif tagname in ('rt', 'rp'):
            # An rt element's end tag may be omitted if the rt element is
            # immediately followed by an rt or rp element, or if there is
            # no more content in the parent element.
            # An rp element's end tag may be omitted if the rp element is
            # immediately followed by an rt or rp element, or if there is
            # no more content in the parent element.
            if type == "StartTag":
                return next["name"] in ('rt', 'rp')
            else:
                return type == "EndTag" or type is None
        elif tagname == 'colgroup':
            # A colgroup element's end tag may be omitted if the colgroup
            # element is not immediately followed by a space character or
            # a comment.
            if type in ("Comment", "SpaceCharacters"):
                return False
            elif type == "StartTag":
                # XXX: we also look for an immediately following colgroup
                # element. See is_optional_start.
                return next["name"] != 'colgroup'
            else:
                return True
        elif tagname in ('thead', 'tbody'):
            # A thead element's end tag may be omitted if the thead element
            # is immediately followed by a tbody or tfoot element.
            # A tbody element's end tag may be omitted if the tbody element
            # is immediately followed by a tbody or tfoot element, or if
            # there is no more content in the parent element.
            # A tfoot element's end tag may be omitted if the tfoot element
            # is immediately followed by a tbody element, or if there is no
            # more content in the parent element.
            # XXX: we never omit the end tag when the following element is
            # a tbody. See is_optional_start.
            if type == "StartTag":
                return next["name"] in ['tbody', 'tfoot']
            elif tagname == 'tbody':
                return type == "EndTag" or type is None
            else:
                return False
        elif tagname == 'tfoot':
            # A tfoot element's end tag may be omitted if the tfoot element
            # is immediately followed by a tbody element, or if there is no
            # more content in the parent element.
            # XXX: we never omit the end tag when the following element is
            # a tbody. See is_optional_start.
            if type == "StartTag":
                return next["name"] == 'tbody'
            else:
                return type == "EndTag" or type is None
        elif tagname in ('td', 'th'):
            # A td element's end tag may be omitted if the td element is
            # immediately followed by a td or th element, or if there is
            # no more content in the parent element.
            # A th element's end tag may be omitted if the th element is
            # immediately followed by a td or th element, or if there is
            # no more content in the parent element.
            if type == "StartTag":
                return next["name"] in ('td', 'th')
            else:
                return type == "EndTag" or type is None
        return False
