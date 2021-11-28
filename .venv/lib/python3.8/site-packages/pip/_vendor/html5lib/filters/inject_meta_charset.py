from __future__ import absolute_import, division, unicode_literals

from . import base


class Filter(base.Filter):
    """Injects ``<meta charset=ENCODING>`` tag into head of document"""
    def __init__(self, source, encoding):
        """Creates a Filter

        :arg source: the source token stream

        :arg encoding: the encoding to set

        """
        base.Filter.__init__(self, source)
        self.encoding = encoding

    def __iter__(self):
        state = "pre_head"
        meta_found = (self.encoding is None)
        pending = []

        for token in base.Filter.__iter__(self):
            type = token["type"]
            if type == "StartTag":
                if token["name"].lower() == "head":
                    state = "in_head"

            elif type == "EmptyTag":
                if token["name"].lower() == "meta":
                    # replace charset with actual encoding
                    has_http_equiv_content_type = False
                    for (namespace, name), value in token["data"].items():
                        if namespace is not None:
                            continue
                        elif name.lower() == 'charset':
                            token["data"][(namespace, name)] = self.encoding
                            meta_found = True
                            break
                        elif name == 'http-equiv' and value.lower() == 'content-type':
                            has_http_equiv_content_type = True
                    else:
                        if has_http_equiv_content_type and (None, "content") in token["data"]:
                            token["data"][(None, "content")] = 'text/html; charset=%s' % self.encoding
                            meta_found = True

                elif token["name"].lower() == "head" and not meta_found:
                    # insert meta into empty head
                    yield {"type": "StartTag", "name": "head",
                           "data": token["data"]}
                    yield {"type": "EmptyTag", "name": "meta",
                           "data": {(None, "charset"): self.encoding}}
                    yield {"type": "EndTag", "name": "head"}
                    meta_found = True
                    continue

            elif type == "EndTag":
                if token["name"].lower() == "head" and pending:
                    # insert meta into head (if necessary) and flush pending queue
                    yield pending.pop(0)
                    if not meta_found:
                        yield {"type": "EmptyTag", "name": "meta",
                               "data": {(None, "charset"): self.encoding}}
                    while pending:
                        yield pending.pop(0)
                    meta_found = True
                    state = "post_head"

            if state == "in_head":
                pending.append(token)
            else:
                yield token
