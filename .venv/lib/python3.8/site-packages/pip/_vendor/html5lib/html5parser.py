from __future__ import absolute_import, division, unicode_literals
from pip._vendor.six import with_metaclass, viewkeys

import types

from . import _inputstream
from . import _tokenizer

from . import treebuilders
from .treebuilders.base import Marker

from . import _utils
from .constants import (
    spaceCharacters, asciiUpper2Lower,
    specialElements, headingElements, cdataElements, rcdataElements,
    tokenTypes, tagTokenTypes,
    namespaces,
    htmlIntegrationPointElements, mathmlTextIntegrationPointElements,
    adjustForeignAttributes as adjustForeignAttributesMap,
    adjustMathMLAttributes, adjustSVGAttributes,
    E,
    _ReparseException
)


def parse(doc, treebuilder="etree", namespaceHTMLElements=True, **kwargs):
    """Parse an HTML document as a string or file-like object into a tree

    :arg doc: the document to parse as a string or file-like object

    :arg treebuilder: the treebuilder to use when parsing

    :arg namespaceHTMLElements: whether or not to namespace HTML elements

    :returns: parsed tree

    Example:

    >>> from html5lib.html5parser import parse
    >>> parse('<html><body><p>This is a doc</p></body></html>')
    <Element u'{http://www.w3.org/1999/xhtml}html' at 0x7feac4909db0>

    """
    tb = treebuilders.getTreeBuilder(treebuilder)
    p = HTMLParser(tb, namespaceHTMLElements=namespaceHTMLElements)
    return p.parse(doc, **kwargs)


def parseFragment(doc, container="div", treebuilder="etree", namespaceHTMLElements=True, **kwargs):
    """Parse an HTML fragment as a string or file-like object into a tree

    :arg doc: the fragment to parse as a string or file-like object

    :arg container: the container context to parse the fragment in

    :arg treebuilder: the treebuilder to use when parsing

    :arg namespaceHTMLElements: whether or not to namespace HTML elements

    :returns: parsed tree

    Example:

    >>> from html5lib.html5libparser import parseFragment
    >>> parseFragment('<b>this is a fragment</b>')
    <Element u'DOCUMENT_FRAGMENT' at 0x7feac484b090>

    """
    tb = treebuilders.getTreeBuilder(treebuilder)
    p = HTMLParser(tb, namespaceHTMLElements=namespaceHTMLElements)
    return p.parseFragment(doc, container=container, **kwargs)


def method_decorator_metaclass(function):
    class Decorated(type):
        def __new__(meta, classname, bases, classDict):
            for attributeName, attribute in classDict.items():
                if isinstance(attribute, types.FunctionType):
                    attribute = function(attribute)

                classDict[attributeName] = attribute
            return type.__new__(meta, classname, bases, classDict)
    return Decorated


class HTMLParser(object):
    """HTML parser

    Generates a tree structure from a stream of (possibly malformed) HTML.

    """

    def __init__(self, tree=None, strict=False, namespaceHTMLElements=True, debug=False):
        """
        :arg tree: a treebuilder class controlling the type of tree that will be
            returned. Built in treebuilders can be accessed through
            html5lib.treebuilders.getTreeBuilder(treeType)

        :arg strict: raise an exception when a parse error is encountered

        :arg namespaceHTMLElements: whether or not to namespace HTML elements

        :arg debug: whether or not to enable debug mode which logs things

        Example:

        >>> from html5lib.html5parser import HTMLParser
        >>> parser = HTMLParser()                     # generates parser with etree builder
        >>> parser = HTMLParser('lxml', strict=True)  # generates parser with lxml builder which is strict

        """

        # Raise an exception on the first error encountered
        self.strict = strict

        if tree is None:
            tree = treebuilders.getTreeBuilder("etree")
        self.tree = tree(namespaceHTMLElements)
        self.errors = []

        self.phases = {name: cls(self, self.tree) for name, cls in
                       getPhases(debug).items()}

    def _parse(self, stream, innerHTML=False, container="div", scripting=False, **kwargs):

        self.innerHTMLMode = innerHTML
        self.container = container
        self.scripting = scripting
        self.tokenizer = _tokenizer.HTMLTokenizer(stream, parser=self, **kwargs)
        self.reset()

        try:
            self.mainLoop()
        except _ReparseException:
            self.reset()
            self.mainLoop()

    def reset(self):
        self.tree.reset()
        self.firstStartTag = False
        self.errors = []
        self.log = []  # only used with debug mode
        # "quirks" / "limited quirks" / "no quirks"
        self.compatMode = "no quirks"

        if self.innerHTMLMode:
            self.innerHTML = self.container.lower()

            if self.innerHTML in cdataElements:
                self.tokenizer.state = self.tokenizer.rcdataState
            elif self.innerHTML in rcdataElements:
                self.tokenizer.state = self.tokenizer.rawtextState
            elif self.innerHTML == 'plaintext':
                self.tokenizer.state = self.tokenizer.plaintextState
            else:
                # state already is data state
                # self.tokenizer.state = self.tokenizer.dataState
                pass
            self.phase = self.phases["beforeHtml"]
            self.phase.insertHtmlElement()
            self.resetInsertionMode()
        else:
            self.innerHTML = False  # pylint:disable=redefined-variable-type
            self.phase = self.phases["initial"]

        self.lastPhase = None

        self.beforeRCDataPhase = None

        self.framesetOK = True

    @property
    def documentEncoding(self):
        """Name of the character encoding that was used to decode the input stream, or
        :obj:`None` if that is not determined yet

        """
        if not hasattr(self, 'tokenizer'):
            return None
        return self.tokenizer.stream.charEncoding[0].name

    def isHTMLIntegrationPoint(self, element):
        if (element.name == "annotation-xml" and
                element.namespace == namespaces["mathml"]):
            return ("encoding" in element.attributes and
                    element.attributes["encoding"].translate(
                        asciiUpper2Lower) in
                    ("text/html", "application/xhtml+xml"))
        else:
            return (element.namespace, element.name) in htmlIntegrationPointElements

    def isMathMLTextIntegrationPoint(self, element):
        return (element.namespace, element.name) in mathmlTextIntegrationPointElements

    def mainLoop(self):
        CharactersToken = tokenTypes["Characters"]
        SpaceCharactersToken = tokenTypes["SpaceCharacters"]
        StartTagToken = tokenTypes["StartTag"]
        EndTagToken = tokenTypes["EndTag"]
        CommentToken = tokenTypes["Comment"]
        DoctypeToken = tokenTypes["Doctype"]
        ParseErrorToken = tokenTypes["ParseError"]

        for token in self.tokenizer:
            prev_token = None
            new_token = token
            while new_token is not None:
                prev_token = new_token
                currentNode = self.tree.openElements[-1] if self.tree.openElements else None
                currentNodeNamespace = currentNode.namespace if currentNode else None
                currentNodeName = currentNode.name if currentNode else None

                type = new_token["type"]

                if type == ParseErrorToken:
                    self.parseError(new_token["data"], new_token.get("datavars", {}))
                    new_token = None
                else:
                    if (len(self.tree.openElements) == 0 or
                        currentNodeNamespace == self.tree.defaultNamespace or
                        (self.isMathMLTextIntegrationPoint(currentNode) and
                         ((type == StartTagToken and
                           token["name"] not in frozenset(["mglyph", "malignmark"])) or
                          type in (CharactersToken, SpaceCharactersToken))) or
                        (currentNodeNamespace == namespaces["mathml"] and
                         currentNodeName == "annotation-xml" and
                         type == StartTagToken and
                         token["name"] == "svg") or
                        (self.isHTMLIntegrationPoint(currentNode) and
                         type in (StartTagToken, CharactersToken, SpaceCharactersToken))):
                        phase = self.phase
                    else:
                        phase = self.phases["inForeignContent"]

                    if type == CharactersToken:
                        new_token = phase.processCharacters(new_token)
                    elif type == SpaceCharactersToken:
                        new_token = phase.processSpaceCharacters(new_token)
                    elif type == StartTagToken:
                        new_token = phase.processStartTag(new_token)
                    elif type == EndTagToken:
                        new_token = phase.processEndTag(new_token)
                    elif type == CommentToken:
                        new_token = phase.processComment(new_token)
                    elif type == DoctypeToken:
                        new_token = phase.processDoctype(new_token)

            if (type == StartTagToken and prev_token["selfClosing"] and
                    not prev_token["selfClosingAcknowledged"]):
                self.parseError("non-void-element-with-trailing-solidus",
                                {"name": prev_token["name"]})

        # When the loop finishes it's EOF
        reprocess = True
        phases = []
        while reprocess:
            phases.append(self.phase)
            reprocess = self.phase.processEOF()
            if reprocess:
                assert self.phase not in phases

    def parse(self, stream, *args, **kwargs):
        """Parse a HTML document into a well-formed tree

        :arg stream: a file-like object or string containing the HTML to be parsed

            The optional encoding parameter must be a string that indicates
            the encoding.  If specified, that encoding will be used,
            regardless of any BOM or later declaration (such as in a meta
            element).

        :arg scripting: treat noscript elements as if JavaScript was turned on

        :returns: parsed tree

        Example:

        >>> from html5lib.html5parser import HTMLParser
        >>> parser = HTMLParser()
        >>> parser.parse('<html><body><p>This is a doc</p></body></html>')
        <Element u'{http://www.w3.org/1999/xhtml}html' at 0x7feac4909db0>

        """
        self._parse(stream, False, None, *args, **kwargs)
        return self.tree.getDocument()

    def parseFragment(self, stream, *args, **kwargs):
        """Parse a HTML fragment into a well-formed tree fragment

        :arg container: name of the element we're setting the innerHTML
            property if set to None, default to 'div'

        :arg stream: a file-like object or string containing the HTML to be parsed

            The optional encoding parameter must be a string that indicates
            the encoding.  If specified, that encoding will be used,
            regardless of any BOM or later declaration (such as in a meta
            element)

        :arg scripting: treat noscript elements as if JavaScript was turned on

        :returns: parsed tree

        Example:

        >>> from html5lib.html5libparser import HTMLParser
        >>> parser = HTMLParser()
        >>> parser.parseFragment('<b>this is a fragment</b>')
        <Element u'DOCUMENT_FRAGMENT' at 0x7feac484b090>

        """
        self._parse(stream, True, *args, **kwargs)
        return self.tree.getFragment()

    def parseError(self, errorcode="XXX-undefined-error", datavars=None):
        # XXX The idea is to make errorcode mandatory.
        if datavars is None:
            datavars = {}
        self.errors.append((self.tokenizer.stream.position(), errorcode, datavars))
        if self.strict:
            raise ParseError(E[errorcode] % datavars)

    def adjustMathMLAttributes(self, token):
        adjust_attributes(token, adjustMathMLAttributes)

    def adjustSVGAttributes(self, token):
        adjust_attributes(token, adjustSVGAttributes)

    def adjustForeignAttributes(self, token):
        adjust_attributes(token, adjustForeignAttributesMap)

    def reparseTokenNormal(self, token):
        # pylint:disable=unused-argument
        self.parser.phase()

    def resetInsertionMode(self):
        # The name of this method is mostly historical. (It's also used in the
        # specification.)
        last = False
        newModes = {
            "select": "inSelect",
            "td": "inCell",
            "th": "inCell",
            "tr": "inRow",
            "tbody": "inTableBody",
            "thead": "inTableBody",
            "tfoot": "inTableBody",
            "caption": "inCaption",
            "colgroup": "inColumnGroup",
            "table": "inTable",
            "head": "inBody",
            "body": "inBody",
            "frameset": "inFrameset",
            "html": "beforeHead"
        }
        for node in self.tree.openElements[::-1]:
            nodeName = node.name
            new_phase = None
            if node == self.tree.openElements[0]:
                assert self.innerHTML
                last = True
                nodeName = self.innerHTML
            # Check for conditions that should only happen in the innerHTML
            # case
            if nodeName in ("select", "colgroup", "head", "html"):
                assert self.innerHTML

            if not last and node.namespace != self.tree.defaultNamespace:
                continue

            if nodeName in newModes:
                new_phase = self.phases[newModes[nodeName]]
                break
            elif last:
                new_phase = self.phases["inBody"]
                break

        self.phase = new_phase

    def parseRCDataRawtext(self, token, contentType):
        # Generic RCDATA/RAWTEXT Parsing algorithm
        assert contentType in ("RAWTEXT", "RCDATA")

        self.tree.insertElement(token)

        if contentType == "RAWTEXT":
            self.tokenizer.state = self.tokenizer.rawtextState
        else:
            self.tokenizer.state = self.tokenizer.rcdataState

        self.originalPhase = self.phase

        self.phase = self.phases["text"]


@_utils.memoize
def getPhases(debug):
    def log(function):
        """Logger that records which phase processes each token"""
        type_names = {value: key for key, value in tokenTypes.items()}

        def wrapped(self, *args, **kwargs):
            if function.__name__.startswith("process") and len(args) > 0:
                token = args[0]
                info = {"type": type_names[token['type']]}
                if token['type'] in tagTokenTypes:
                    info["name"] = token['name']

                self.parser.log.append((self.parser.tokenizer.state.__name__,
                                        self.parser.phase.__class__.__name__,
                                        self.__class__.__name__,
                                        function.__name__,
                                        info))
                return function(self, *args, **kwargs)
            else:
                return function(self, *args, **kwargs)
        return wrapped

    def getMetaclass(use_metaclass, metaclass_func):
        if use_metaclass:
            return method_decorator_metaclass(metaclass_func)
        else:
            return type

    # pylint:disable=unused-argument
    class Phase(with_metaclass(getMetaclass(debug, log))):
        """Base class for helper object that implements each phase of processing
        """
        __slots__ = ("parser", "tree", "__startTagCache", "__endTagCache")

        def __init__(self, parser, tree):
            self.parser = parser
            self.tree = tree
            self.__startTagCache = {}
            self.__endTagCache = {}

        def processEOF(self):
            raise NotImplementedError

        def processComment(self, token):
            # For most phases the following is correct. Where it's not it will be
            # overridden.
            self.tree.insertComment(token, self.tree.openElements[-1])

        def processDoctype(self, token):
            self.parser.parseError("unexpected-doctype")

        def processCharacters(self, token):
            self.tree.insertText(token["data"])

        def processSpaceCharacters(self, token):
            self.tree.insertText(token["data"])

        def processStartTag(self, token):
            # Note the caching is done here rather than BoundMethodDispatcher as doing it there
            # requires a circular reference to the Phase, and this ends up with a significant
            # (CPython 2.7, 3.8) GC cost when parsing many short inputs
            name = token["name"]
            # In Py2, using `in` is quicker in general than try/except KeyError
            # In Py3, `in` is quicker when there are few cache hits (typically short inputs)
            if name in self.__startTagCache:
                func = self.__startTagCache[name]
            else:
                func = self.__startTagCache[name] = self.startTagHandler[name]
                # bound the cache size in case we get loads of unknown tags
                while len(self.__startTagCache) > len(self.startTagHandler) * 1.1:
                    # this makes the eviction policy random on Py < 3.7 and FIFO >= 3.7
                    self.__startTagCache.pop(next(iter(self.__startTagCache)))
            return func(token)

        def startTagHtml(self, token):
            if not self.parser.firstStartTag and token["name"] == "html":
                self.parser.parseError("non-html-root")
            # XXX Need a check here to see if the first start tag token emitted is
            # this token... If it's not, invoke self.parser.parseError().
            for attr, value in token["data"].items():
                if attr not in self.tree.openElements[0].attributes:
                    self.tree.openElements[0].attributes[attr] = value
            self.parser.firstStartTag = False

        def processEndTag(self, token):
            # Note the caching is done here rather than BoundMethodDispatcher as doing it there
            # requires a circular reference to the Phase, and this ends up with a significant
            # (CPython 2.7, 3.8) GC cost when parsing many short inputs
            name = token["name"]
            # In Py2, using `in` is quicker in general than try/except KeyError
            # In Py3, `in` is quicker when there are few cache hits (typically short inputs)
            if name in self.__endTagCache:
                func = self.__endTagCache[name]
            else:
                func = self.__endTagCache[name] = self.endTagHandler[name]
                # bound the cache size in case we get loads of unknown tags
                while len(self.__endTagCache) > len(self.endTagHandler) * 1.1:
                    # this makes the eviction policy random on Py < 3.7 and FIFO >= 3.7
                    self.__endTagCache.pop(next(iter(self.__endTagCache)))
            return func(token)

    class InitialPhase(Phase):
        __slots__ = tuple()

        def processSpaceCharacters(self, token):
            pass

        def processComment(self, token):
            self.tree.insertComment(token, self.tree.document)

        def processDoctype(self, token):
            name = token["name"]
            publicId = token["publicId"]
            systemId = token["systemId"]
            correct = token["correct"]

            if (name != "html" or publicId is not None or
                    systemId is not None and systemId != "about:legacy-compat"):
                self.parser.parseError("unknown-doctype")

            if publicId is None:
                publicId = ""

            self.tree.insertDoctype(token)

            if publicId != "":
                publicId = publicId.translate(asciiUpper2Lower)

            if (not correct or token["name"] != "html" or
                    publicId.startswith(
                        ("+//silmaril//dtd html pro v0r11 19970101//",
                         "-//advasoft ltd//dtd html 3.0 aswedit + extensions//",
                         "-//as//dtd html 3.0 aswedit + extensions//",
                         "-//ietf//dtd html 2.0 level 1//",
                         "-//ietf//dtd html 2.0 level 2//",
                         "-//ietf//dtd html 2.0 strict level 1//",
                         "-//ietf//dtd html 2.0 strict level 2//",
                         "-//ietf//dtd html 2.0 strict//",
                         "-//ietf//dtd html 2.0//",
                         "-//ietf//dtd html 2.1e//",
                         "-//ietf//dtd html 3.0//",
                         "-//ietf//dtd html 3.2 final//",
                         "-//ietf//dtd html 3.2//",
                         "-//ietf//dtd html 3//",
                         "-//ietf//dtd html level 0//",
                         "-//ietf//dtd html level 1//",
                         "-//ietf//dtd html level 2//",
                         "-//ietf//dtd html level 3//",
                         "-//ietf//dtd html strict level 0//",
                         "-//ietf//dtd html strict level 1//",
                         "-//ietf//dtd html strict level 2//",
                         "-//ietf//dtd html strict level 3//",
                         "-//ietf//dtd html strict//",
                         "-//ietf//dtd html//",
                         "-//metrius//dtd metrius presentational//",
                         "-//microsoft//dtd internet explorer 2.0 html strict//",
                         "-//microsoft//dtd internet explorer 2.0 html//",
                         "-//microsoft//dtd internet explorer 2.0 tables//",
                         "-//microsoft//dtd internet explorer 3.0 html strict//",
                         "-//microsoft//dtd internet explorer 3.0 html//",
                         "-//microsoft//dtd internet explorer 3.0 tables//",
                         "-//netscape comm. corp.//dtd html//",
                         "-//netscape comm. corp.//dtd strict html//",
                         "-//o'reilly and associates//dtd html 2.0//",
                         "-//o'reilly and associates//dtd html extended 1.0//",
                         "-//o'reilly and associates//dtd html extended relaxed 1.0//",
                         "-//softquad software//dtd hotmetal pro 6.0::19990601::extensions to html 4.0//",
                         "-//softquad//dtd hotmetal pro 4.0::19971010::extensions to html 4.0//",
                         "-//spyglass//dtd html 2.0 extended//",
                         "-//sq//dtd html 2.0 hotmetal + extensions//",
                         "-//sun microsystems corp.//dtd hotjava html//",
                         "-//sun microsystems corp.//dtd hotjava strict html//",
                         "-//w3c//dtd html 3 1995-03-24//",
                         "-//w3c//dtd html 3.2 draft//",
                         "-//w3c//dtd html 3.2 final//",
                         "-//w3c//dtd html 3.2//",
                         "-//w3c//dtd html 3.2s draft//",
                         "-//w3c//dtd html 4.0 frameset//",
                         "-//w3c//dtd html 4.0 transitional//",
                         "-//w3c//dtd html experimental 19960712//",
                         "-//w3c//dtd html experimental 970421//",
                         "-//w3c//dtd w3 html//",
                         "-//w3o//dtd w3 html 3.0//",
                         "-//webtechs//dtd mozilla html 2.0//",
                         "-//webtechs//dtd mozilla html//")) or
                    publicId in ("-//w3o//dtd w3 html strict 3.0//en//",
                                 "-/w3c/dtd html 4.0 transitional/en",
                                 "html") or
                    publicId.startswith(
                        ("-//w3c//dtd html 4.01 frameset//",
                         "-//w3c//dtd html 4.01 transitional//")) and
                    systemId is None or
                    systemId and systemId.lower() == "http://www.ibm.com/data/dtd/v11/ibmxhtml1-transitional.dtd"):
                self.parser.compatMode = "quirks"
            elif (publicId.startswith(
                    ("-//w3c//dtd xhtml 1.0 frameset//",
                     "-//w3c//dtd xhtml 1.0 transitional//")) or
                  publicId.startswith(
                      ("-//w3c//dtd html 4.01 frameset//",
                       "-//w3c//dtd html 4.01 transitional//")) and
                  systemId is not None):
                self.parser.compatMode = "limited quirks"

            self.parser.phase = self.parser.phases["beforeHtml"]

        def anythingElse(self):
            self.parser.compatMode = "quirks"
            self.parser.phase = self.parser.phases["beforeHtml"]

        def processCharacters(self, token):
            self.parser.parseError("expected-doctype-but-got-chars")
            self.anythingElse()
            return token

        def processStartTag(self, token):
            self.parser.parseError("expected-doctype-but-got-start-tag",
                                   {"name": token["name"]})
            self.anythingElse()
            return token

        def processEndTag(self, token):
            self.parser.parseError("expected-doctype-but-got-end-tag",
                                   {"name": token["name"]})
            self.anythingElse()
            return token

        def processEOF(self):
            self.parser.parseError("expected-doctype-but-got-eof")
            self.anythingElse()
            return True

    class BeforeHtmlPhase(Phase):
        __slots__ = tuple()

        # helper methods
        def insertHtmlElement(self):
            self.tree.insertRoot(impliedTagToken("html", "StartTag"))
            self.parser.phase = self.parser.phases["beforeHead"]

        # other
        def processEOF(self):
            self.insertHtmlElement()
            return True

        def processComment(self, token):
            self.tree.insertComment(token, self.tree.document)

        def processSpaceCharacters(self, token):
            pass

        def processCharacters(self, token):
            self.insertHtmlElement()
            return token

        def processStartTag(self, token):
            if token["name"] == "html":
                self.parser.firstStartTag = True
            self.insertHtmlElement()
            return token

        def processEndTag(self, token):
            if token["name"] not in ("head", "body", "html", "br"):
                self.parser.parseError("unexpected-end-tag-before-html",
                                       {"name": token["name"]})
            else:
                self.insertHtmlElement()
                return token

    class BeforeHeadPhase(Phase):
        __slots__ = tuple()

        def processEOF(self):
            self.startTagHead(impliedTagToken("head", "StartTag"))
            return True

        def processSpaceCharacters(self, token):
            pass

        def processCharacters(self, token):
            self.startTagHead(impliedTagToken("head", "StartTag"))
            return token

        def startTagHtml(self, token):
            return self.parser.phases["inBody"].processStartTag(token)

        def startTagHead(self, token):
            self.tree.insertElement(token)
            self.tree.headPointer = self.tree.openElements[-1]
            self.parser.phase = self.parser.phases["inHead"]

        def startTagOther(self, token):
            self.startTagHead(impliedTagToken("head", "StartTag"))
            return token

        def endTagImplyHead(self, token):
            self.startTagHead(impliedTagToken("head", "StartTag"))
            return token

        def endTagOther(self, token):
            self.parser.parseError("end-tag-after-implied-root",
                                   {"name": token["name"]})

        startTagHandler = _utils.MethodDispatcher([
            ("html", startTagHtml),
            ("head", startTagHead)
        ])
        startTagHandler.default = startTagOther

        endTagHandler = _utils.MethodDispatcher([
            (("head", "body", "html", "br"), endTagImplyHead)
        ])
        endTagHandler.default = endTagOther

    class InHeadPhase(Phase):
        __slots__ = tuple()

        # the real thing
        def processEOF(self):
            self.anythingElse()
            return True

        def processCharacters(self, token):
            self.anythingElse()
            return token

        def startTagHtml(self, token):
            return self.parser.phases["inBody"].processStartTag(token)

        def startTagHead(self, token):
            self.parser.parseError("two-heads-are-not-better-than-one")

        def startTagBaseLinkCommand(self, token):
            self.tree.insertElement(token)
            self.tree.openElements.pop()
            token["selfClosingAcknowledged"] = True

        def startTagMeta(self, token):
            self.tree.insertElement(token)
            self.tree.openElements.pop()
            token["selfClosingAcknowledged"] = True

            attributes = token["data"]
            if self.parser.tokenizer.stream.charEncoding[1] == "tentative":
                if "charset" in attributes:
                    self.parser.tokenizer.stream.changeEncoding(attributes["charset"])
                elif ("content" in attributes and
                      "http-equiv" in attributes and
                      attributes["http-equiv"].lower() == "content-type"):
                    # Encoding it as UTF-8 here is a hack, as really we should pass
                    # the abstract Unicode string, and just use the
                    # ContentAttrParser on that, but using UTF-8 allows all chars
                    # to be encoded and as a ASCII-superset works.
                    data = _inputstream.EncodingBytes(attributes["content"].encode("utf-8"))
                    parser = _inputstream.ContentAttrParser(data)
                    codec = parser.parse()
                    self.parser.tokenizer.stream.changeEncoding(codec)

        def startTagTitle(self, token):
            self.parser.parseRCDataRawtext(token, "RCDATA")

        def startTagNoFramesStyle(self, token):
            # Need to decide whether to implement the scripting-disabled case
            self.parser.parseRCDataRawtext(token, "RAWTEXT")

        def startTagNoscript(self, token):
            if self.parser.scripting:
                self.parser.parseRCDataRawtext(token, "RAWTEXT")
            else:
                self.tree.insertElement(token)
                self.parser.phase = self.parser.phases["inHeadNoscript"]

        def startTagScript(self, token):
            self.tree.insertElement(token)
            self.parser.tokenizer.state = self.parser.tokenizer.scriptDataState
            self.parser.originalPhase = self.parser.phase
            self.parser.phase = self.parser.phases["text"]

        def startTagOther(self, token):
            self.anythingElse()
            return token

        def endTagHead(self, token):
            node = self.parser.tree.openElements.pop()
            assert node.name == "head", "Expected head got %s" % node.name
            self.parser.phase = self.parser.phases["afterHead"]

        def endTagHtmlBodyBr(self, token):
            self.anythingElse()
            return token

        def endTagOther(self, token):
            self.parser.parseError("unexpected-end-tag", {"name": token["name"]})

        def anythingElse(self):
            self.endTagHead(impliedTagToken("head"))

        startTagHandler = _utils.MethodDispatcher([
            ("html", startTagHtml),
            ("title", startTagTitle),
            (("noframes", "style"), startTagNoFramesStyle),
            ("noscript", startTagNoscript),
            ("script", startTagScript),
            (("base", "basefont", "bgsound", "command", "link"),
             startTagBaseLinkCommand),
            ("meta", startTagMeta),
            ("head", startTagHead)
        ])
        startTagHandler.default = startTagOther

        endTagHandler = _utils.MethodDispatcher([
            ("head", endTagHead),
            (("br", "html", "body"), endTagHtmlBodyBr)
        ])
        endTagHandler.default = endTagOther

    class InHeadNoscriptPhase(Phase):
        __slots__ = tuple()

        def processEOF(self):
            self.parser.parseError("eof-in-head-noscript")
            self.anythingElse()
            return True

        def processComment(self, token):
            return self.parser.phases["inHead"].processComment(token)

        def processCharacters(self, token):
            self.parser.parseError("char-in-head-noscript")
            self.anythingElse()
            return token

        def processSpaceCharacters(self, token):
            return self.parser.phases["inHead"].processSpaceCharacters(token)

        def startTagHtml(self, token):
            return self.parser.phases["inBody"].processStartTag(token)

        def startTagBaseLinkCommand(self, token):
            return self.parser.phases["inHead"].processStartTag(token)

        def startTagHeadNoscript(self, token):
            self.parser.parseError("unexpected-start-tag", {"name": token["name"]})

        def startTagOther(self, token):
            self.parser.parseError("unexpected-inhead-noscript-tag", {"name": token["name"]})
            self.anythingElse()
            return token

        def endTagNoscript(self, token):
            node = self.parser.tree.openElements.pop()
            assert node.name == "noscript", "Expected noscript got %s" % node.name
            self.parser.phase = self.parser.phases["inHead"]

        def endTagBr(self, token):
            self.parser.parseError("unexpected-inhead-noscript-tag", {"name": token["name"]})
            self.anythingElse()
            return token

        def endTagOther(self, token):
            self.parser.parseError("unexpected-end-tag", {"name": token["name"]})

        def anythingElse(self):
            # Caller must raise parse error first!
            self.endTagNoscript(impliedTagToken("noscript"))

        startTagHandler = _utils.MethodDispatcher([
            ("html", startTagHtml),
            (("basefont", "bgsound", "link", "meta", "noframes", "style"), startTagBaseLinkCommand),
            (("head", "noscript"), startTagHeadNoscript),
        ])
        startTagHandler.default = startTagOther

        endTagHandler = _utils.MethodDispatcher([
            ("noscript", endTagNoscript),
            ("br", endTagBr),
        ])
        endTagHandler.default = endTagOther

    class AfterHeadPhase(Phase):
        __slots__ = tuple()

        def processEOF(self):
            self.anythingElse()
            return True

        def processCharacters(self, token):
            self.anythingElse()
            return token

        def startTagHtml(self, token):
            return self.parser.phases["inBody"].processStartTag(token)

        def startTagBody(self, token):
            self.parser.framesetOK = False
            self.tree.insertElement(token)
            self.parser.phase = self.parser.phases["inBody"]

        def startTagFrameset(self, token):
            self.tree.insertElement(token)
            self.parser.phase = self.parser.phases["inFrameset"]

        def startTagFromHead(self, token):
            self.parser.parseError("unexpected-start-tag-out-of-my-head",
                                   {"name": token["name"]})
            self.tree.openElements.append(self.tree.headPointer)
            self.parser.phases["inHead"].processStartTag(token)
            for node in self.tree.openElements[::-1]:
                if node.name == "head":
                    self.tree.openElements.remove(node)
                    break

        def startTagHead(self, token):
            self.parser.parseError("unexpected-start-tag", {"name": token["name"]})

        def startTagOther(self, token):
            self.anythingElse()
            return token

        def endTagHtmlBodyBr(self, token):
            self.anythingElse()
            return token

        def endTagOther(self, token):
            self.parser.parseError("unexpected-end-tag", {"name": token["name"]})

        def anythingElse(self):
            self.tree.insertElement(impliedTagToken("body", "StartTag"))
            self.parser.phase = self.parser.phases["inBody"]
            self.parser.framesetOK = True

        startTagHandler = _utils.MethodDispatcher([
            ("html", startTagHtml),
            ("body", startTagBody),
            ("frameset", startTagFrameset),
            (("base", "basefont", "bgsound", "link", "meta", "noframes", "script",
              "style", "title"),
             startTagFromHead),
            ("head", startTagHead)
        ])
        startTagHandler.default = startTagOther
        endTagHandler = _utils.MethodDispatcher([(("body", "html", "br"),
                                                  endTagHtmlBodyBr)])
        endTagHandler.default = endTagOther

    class InBodyPhase(Phase):
        # http://www.whatwg.org/specs/web-apps/current-work/#parsing-main-inbody
        # the really-really-really-very crazy mode
        __slots__ = ("processSpaceCharacters",)

        def __init__(self, *args, **kwargs):
            super(InBodyPhase, self).__init__(*args, **kwargs)
            # Set this to the default handler
            self.processSpaceCharacters = self.processSpaceCharactersNonPre

        def isMatchingFormattingElement(self, node1, node2):
            return (node1.name == node2.name and
                    node1.namespace == node2.namespace and
                    node1.attributes == node2.attributes)

        # helper
        def addFormattingElement(self, token):
            self.tree.insertElement(token)
            element = self.tree.openElements[-1]

            matchingElements = []
            for node in self.tree.activeFormattingElements[::-1]:
                if node is Marker:
                    break
                elif self.isMatchingFormattingElement(node, element):
                    matchingElements.append(node)

            assert len(matchingElements) <= 3
            if len(matchingElements) == 3:
                self.tree.activeFormattingElements.remove(matchingElements[-1])
            self.tree.activeFormattingElements.append(element)

        # the real deal
        def processEOF(self):
            allowed_elements = frozenset(("dd", "dt", "li", "p", "tbody", "td",
                                          "tfoot", "th", "thead", "tr", "body",
                                          "html"))
            for node in self.tree.openElements[::-1]:
                if node.name not in allowed_elements:
                    self.parser.parseError("expected-closing-tag-but-got-eof")
                    break
            # Stop parsing

        def processSpaceCharactersDropNewline(self, token):
            # Sometimes (start of <pre>, <listing>, and <textarea> blocks) we
            # want to drop leading newlines
            data = token["data"]
            self.processSpaceCharacters = self.processSpaceCharactersNonPre
            if (data.startswith("\n") and
                self.tree.openElements[-1].name in ("pre", "listing", "textarea") and
                    not self.tree.openElements[-1].hasContent()):
                data = data[1:]
            if data:
                self.tree.reconstructActiveFormattingElements()
                self.tree.insertText(data)

        def processCharacters(self, token):
            if token["data"] == "\u0000":
                # The tokenizer should always emit null on its own
                return
            self.tree.reconstructActiveFormattingElements()
            self.tree.insertText(token["data"])
            # This must be bad for performance
            if (self.parser.framesetOK and
                any([char not in spaceCharacters
                     for char in token["data"]])):
                self.parser.framesetOK = False

        def processSpaceCharactersNonPre(self, token):
            self.tree.reconstructActiveFormattingElements()
            self.tree.insertText(token["data"])

        def startTagProcessInHead(self, token):
            return self.parser.phases["inHead"].processStartTag(token)

        def startTagBody(self, token):
            self.parser.parseError("unexpected-start-tag", {"name": "body"})
            if (len(self.tree.openElements) == 1 or
                    self.tree.openElements[1].name != "body"):
                assert self.parser.innerHTML
            else:
                self.parser.framesetOK = False
                for attr, value in token["data"].items():
                    if attr not in self.tree.openElements[1].attributes:
                        self.tree.openElements[1].attributes[attr] = value

        def startTagFrameset(self, token):
            self.parser.parseError("unexpected-start-tag", {"name": "frameset"})
            if (len(self.tree.openElements) == 1 or self.tree.openElements[1].name != "body"):
                assert self.parser.innerHTML
            elif not self.parser.framesetOK:
                pass
            else:
                if self.tree.openElements[1].parent:
                    self.tree.openElements[1].parent.removeChild(self.tree.openElements[1])
                while self.tree.openElements[-1].name != "html":
                    self.tree.openElements.pop()
                self.tree.insertElement(token)
                self.parser.phase = self.parser.phases["inFrameset"]

        def startTagCloseP(self, token):
            if self.tree.elementInScope("p", variant="button"):
                self.endTagP(impliedTagToken("p"))
            self.tree.insertElement(token)

        def startTagPreListing(self, token):
            if self.tree.elementInScope("p", variant="button"):
                self.endTagP(impliedTagToken("p"))
            self.tree.insertElement(token)
            self.parser.framesetOK = False
            self.processSpaceCharacters = self.processSpaceCharactersDropNewline

        def startTagForm(self, token):
            if self.tree.formPointer:
                self.parser.parseError("unexpected-start-tag", {"name": "form"})
            else:
                if self.tree.elementInScope("p", variant="button"):
                    self.endTagP(impliedTagToken("p"))
                self.tree.insertElement(token)
                self.tree.formPointer = self.tree.openElements[-1]

        def startTagListItem(self, token):
            self.parser.framesetOK = False

            stopNamesMap = {"li": ["li"],
                            "dt": ["dt", "dd"],
                            "dd": ["dt", "dd"]}
            stopNames = stopNamesMap[token["name"]]
            for node in reversed(self.tree.openElements):
                if node.name in stopNames:
                    self.parser.phase.processEndTag(
                        impliedTagToken(node.name, "EndTag"))
                    break
                if (node.nameTuple in specialElements and
                        node.name not in ("address", "div", "p")):
                    break

            if self.tree.elementInScope("p", variant="button"):
                self.parser.phase.processEndTag(
                    impliedTagToken("p", "EndTag"))

            self.tree.insertElement(token)

        def startTagPlaintext(self, token):
            if self.tree.elementInScope("p", variant="button"):
                self.endTagP(impliedTagToken("p"))
            self.tree.insertElement(token)
            self.parser.tokenizer.state = self.parser.tokenizer.plaintextState

        def startTagHeading(self, token):
            if self.tree.elementInScope("p", variant="button"):
                self.endTagP(impliedTagToken("p"))
            if self.tree.openElements[-1].name in headingElements:
                self.parser.parseError("unexpected-start-tag", {"name": token["name"]})
                self.tree.openElements.pop()
            self.tree.insertElement(token)

        def startTagA(self, token):
            afeAElement = self.tree.elementInActiveFormattingElements("a")
            if afeAElement:
                self.parser.parseError("unexpected-start-tag-implies-end-tag",
                                       {"startName": "a", "endName": "a"})
                self.endTagFormatting(impliedTagToken("a"))
                if afeAElement in self.tree.openElements:
                    self.tree.openElements.remove(afeAElement)
                if afeAElement in self.tree.activeFormattingElements:
                    self.tree.activeFormattingElements.remove(afeAElement)
            self.tree.reconstructActiveFormattingElements()
            self.addFormattingElement(token)

        def startTagFormatting(self, token):
            self.tree.reconstructActiveFormattingElements()
            self.addFormattingElement(token)

        def startTagNobr(self, token):
            self.tree.reconstructActiveFormattingElements()
            if self.tree.elementInScope("nobr"):
                self.parser.parseError("unexpected-start-tag-implies-end-tag",
                                       {"startName": "nobr", "endName": "nobr"})
                self.processEndTag(impliedTagToken("nobr"))
                # XXX Need tests that trigger the following
                self.tree.reconstructActiveFormattingElements()
            self.addFormattingElement(token)

        def startTagButton(self, token):
            if self.tree.elementInScope("button"):
                self.parser.parseError("unexpected-start-tag-implies-end-tag",
                                       {"startName": "button", "endName": "button"})
                self.processEndTag(impliedTagToken("button"))
                return token
            else:
                self.tree.reconstructActiveFormattingElements()
                self.tree.insertElement(token)
                self.parser.framesetOK = False

        def startTagAppletMarqueeObject(self, token):
            self.tree.reconstructActiveFormattingElements()
            self.tree.insertElement(token)
            self.tree.activeFormattingElements.append(Marker)
            self.parser.framesetOK = False

        def startTagXmp(self, token):
            if self.tree.elementInScope("p", variant="button"):
                self.endTagP(impliedTagToken("p"))
            self.tree.reconstructActiveFormattingElements()
            self.parser.framesetOK = False
            self.parser.parseRCDataRawtext(token, "RAWTEXT")

        def startTagTable(self, token):
            if self.parser.compatMode != "quirks":
                if self.tree.elementInScope("p", variant="button"):
                    self.processEndTag(impliedTagToken("p"))
            self.tree.insertElement(token)
            self.parser.framesetOK = False
            self.parser.phase = self.parser.phases["inTable"]

        def startTagVoidFormatting(self, token):
            self.tree.reconstructActiveFormattingElements()
            self.tree.insertElement(token)
            self.tree.openElements.pop()
            token["selfClosingAcknowledged"] = True
            self.parser.framesetOK = False

        def startTagInput(self, token):
            framesetOK = self.parser.framesetOK
            self.startTagVoidFormatting(token)
            if ("type" in token["data"] and
                    token["data"]["type"].translate(asciiUpper2Lower) == "hidden"):
                # input type=hidden doesn't change framesetOK
                self.parser.framesetOK = framesetOK

        def startTagParamSource(self, token):
            self.tree.insertElement(token)
            self.tree.openElements.pop()
            token["selfClosingAcknowledged"] = True

        def startTagHr(self, token):
            if self.tree.elementInScope("p", variant="button"):
                self.endTagP(impliedTagToken("p"))
            self.tree.insertElement(token)
            self.tree.openElements.pop()
            token["selfClosingAcknowledged"] = True
            self.parser.framesetOK = False

        def startTagImage(self, token):
            # No really...
            self.parser.parseError("unexpected-start-tag-treated-as",
                                   {"originalName": "image", "newName": "img"})
            self.processStartTag(impliedTagToken("img", "StartTag",
                                                 attributes=token["data"],
                                                 selfClosing=token["selfClosing"]))

        def startTagIsIndex(self, token):
            self.parser.parseError("deprecated-tag", {"name": "isindex"})
            if self.tree.formPointer:
                return
            form_attrs = {}
            if "action" in token["data"]:
                form_attrs["action"] = token["data"]["action"]
            self.processStartTag(impliedTagToken("form", "StartTag",
                                                 attributes=form_attrs))
            self.processStartTag(impliedTagToken("hr", "StartTag"))
            self.processStartTag(impliedTagToken("label", "StartTag"))
            # XXX Localization ...
            if "prompt" in token["data"]:
                prompt = token["data"]["prompt"]
            else:
                prompt = "This is a searchable index. Enter search keywords: "
            self.processCharacters(
                {"type": tokenTypes["Characters"], "data": prompt})
            attributes = token["data"].copy()
            if "action" in attributes:
                del attributes["action"]
            if "prompt" in attributes:
                del attributes["prompt"]
            attributes["name"] = "isindex"
            self.processStartTag(impliedTagToken("input", "StartTag",
                                                 attributes=attributes,
                                                 selfClosing=token["selfClosing"]))
            self.processEndTag(impliedTagToken("label"))
            self.processStartTag(impliedTagToken("hr", "StartTag"))
            self.processEndTag(impliedTagToken("form"))

        def startTagTextarea(self, token):
            self.tree.insertElement(token)
            self.parser.tokenizer.state = self.parser.tokenizer.rcdataState
            self.processSpaceCharacters = self.processSpaceCharactersDropNewline
            self.parser.framesetOK = False

        def startTagIFrame(self, token):
            self.parser.framesetOK = False
            self.startTagRawtext(token)

        def startTagNoscript(self, token):
            if self.parser.scripting:
                self.startTagRawtext(token)
            else:
                self.startTagOther(token)

        def startTagRawtext(self, token):
            """iframe, noembed noframes, noscript(if scripting enabled)"""
            self.parser.parseRCDataRawtext(token, "RAWTEXT")

        def startTagOpt(self, token):
            if self.tree.openElements[-1].name == "option":
                self.parser.phase.processEndTag(impliedTagToken("option"))
            self.tree.reconstructActiveFormattingElements()
            self.parser.tree.insertElement(token)

        def startTagSelect(self, token):
            self.tree.reconstructActiveFormattingElements()
            self.tree.insertElement(token)
            self.parser.framesetOK = False
            if self.parser.phase in (self.parser.phases["inTable"],
                                     self.parser.phases["inCaption"],
                                     self.parser.phases["inColumnGroup"],
                                     self.parser.phases["inTableBody"],
                                     self.parser.phases["inRow"],
                                     self.parser.phases["inCell"]):
                self.parser.phase = self.parser.phases["inSelectInTable"]
            else:
                self.parser.phase = self.parser.phases["inSelect"]

        def startTagRpRt(self, token):
            if self.tree.elementInScope("ruby"):
                self.tree.generateImpliedEndTags()
                if self.tree.openElements[-1].name != "ruby":
                    self.parser.parseError()
            self.tree.insertElement(token)

        def startTagMath(self, token):
            self.tree.reconstructActiveFormattingElements()
            self.parser.adjustMathMLAttributes(token)
            self.parser.adjustForeignAttributes(token)
            token["namespace"] = namespaces["mathml"]
            self.tree.insertElement(token)
            # Need to get the parse error right for the case where the token
            # has a namespace not equal to the xmlns attribute
            if token["selfClosing"]:
                self.tree.openElements.pop()
                token["selfClosingAcknowledged"] = True

        def startTagSvg(self, token):
            self.tree.reconstructActiveFormattingElements()
            self.parser.adjustSVGAttributes(token)
            self.parser.adjustForeignAttributes(token)
            token["namespace"] = namespaces["svg"]
            self.tree.insertElement(token)
            # Need to get the parse error right for the case where the token
            # has a namespace not equal to the xmlns attribute
            if token["selfClosing"]:
                self.tree.openElements.pop()
                token["selfClosingAcknowledged"] = True

        def startTagMisplaced(self, token):
            """ Elements that should be children of other elements that have a
            different insertion mode; here they are ignored
            "caption", "col", "colgroup", "frame", "frameset", "head",
            "option", "optgroup", "tbody", "td", "tfoot", "th", "thead",
            "tr", "noscript"
            """
            self.parser.parseError("unexpected-start-tag-ignored", {"name": token["name"]})

        def startTagOther(self, token):
            self.tree.reconstructActiveFormattingElements()
            self.tree.insertElement(token)

        def endTagP(self, token):
            if not self.tree.elementInScope("p", variant="button"):
                self.startTagCloseP(impliedTagToken("p", "StartTag"))
                self.parser.parseError("unexpected-end-tag", {"name": "p"})
                self.endTagP(impliedTagToken("p", "EndTag"))
            else:
                self.tree.generateImpliedEndTags("p")
                if self.tree.openElements[-1].name != "p":
                    self.parser.parseError("unexpected-end-tag", {"name": "p"})
                node = self.tree.openElements.pop()
                while node.name != "p":
                    node = self.tree.openElements.pop()

        def endTagBody(self, token):
            if not self.tree.elementInScope("body"):
                self.parser.parseError()
                return
            elif self.tree.openElements[-1].name != "body":
                for node in self.tree.openElements[2:]:
                    if node.name not in frozenset(("dd", "dt", "li", "optgroup",
                                                   "option", "p", "rp", "rt",
                                                   "tbody", "td", "tfoot",
                                                   "th", "thead", "tr", "body",
                                                   "html")):
                        # Not sure this is the correct name for the parse error
                        self.parser.parseError(
                            "expected-one-end-tag-but-got-another",
                            {"gotName": "body", "expectedName": node.name})
                        break
            self.parser.phase = self.parser.phases["afterBody"]

        def endTagHtml(self, token):
            # We repeat the test for the body end tag token being ignored here
            if self.tree.elementInScope("body"):
                self.endTagBody(impliedTagToken("body"))
                return token

        def endTagBlock(self, token):
            # Put us back in the right whitespace handling mode
            if token["name"] == "pre":
                self.processSpaceCharacters = self.processSpaceCharactersNonPre
            inScope = self.tree.elementInScope(token["name"])
            if inScope:
                self.tree.generateImpliedEndTags()
            if self.tree.openElements[-1].name != token["name"]:
                self.parser.parseError("end-tag-too-early", {"name": token["name"]})
            if inScope:
                node = self.tree.openElements.pop()
                while node.name != token["name"]:
                    node = self.tree.openElements.pop()

        def endTagForm(self, token):
            node = self.tree.formPointer
            self.tree.formPointer = None
            if node is None or not self.tree.elementInScope(node):
                self.parser.parseError("unexpected-end-tag",
                                       {"name": "form"})
            else:
                self.tree.generateImpliedEndTags()
                if self.tree.openElements[-1] != node:
                    self.parser.parseError("end-tag-too-early-ignored",
                                           {"name": "form"})
                self.tree.openElements.remove(node)

        def endTagListItem(self, token):
            if token["name"] == "li":
                variant = "list"
            else:
                variant = None
            if not self.tree.elementInScope(token["name"], variant=variant):
                self.parser.parseError("unexpected-end-tag", {"name": token["name"]})
            else:
                self.tree.generateImpliedEndTags(exclude=token["name"])
                if self.tree.openElements[-1].name != token["name"]:
                    self.parser.parseError(
                        "end-tag-too-early",
                        {"name": token["name"]})
                node = self.tree.openElements.pop()
                while node.name != token["name"]:
                    node = self.tree.openElements.pop()

        def endTagHeading(self, token):
            for item in headingElements:
                if self.tree.elementInScope(item):
                    self.tree.generateImpliedEndTags()
                    break
            if self.tree.openElements[-1].name != token["name"]:
                self.parser.parseError("end-tag-too-early", {"name": token["name"]})

            for item in headingElements:
                if self.tree.elementInScope(item):
                    item = self.tree.openElements.pop()
                    while item.name not in headingElements:
                        item = self.tree.openElements.pop()
                    break

        def endTagFormatting(self, token):
            """The much-feared adoption agency algorithm"""
            # http://svn.whatwg.org/webapps/complete.html#adoptionAgency revision 7867
            # XXX Better parseError messages appreciated.

            # Step 1
            outerLoopCounter = 0

            # Step 2
            while outerLoopCounter < 8:

                # Step 3
                outerLoopCounter += 1

                # Step 4:

                # Let the formatting element be the last element in
                # the list of active formatting elements that:
                # - is between the end of the list and the last scope
                # marker in the list, if any, or the start of the list
                # otherwise, and
                # - has the same tag name as the token.
                formattingElement = self.tree.elementInActiveFormattingElements(
                    token["name"])
                if (not formattingElement or
                    (formattingElement in self.tree.openElements and
                     not self.tree.elementInScope(formattingElement.name))):
                    # If there is no such node, then abort these steps
                    # and instead act as described in the "any other
                    # end tag" entry below.
                    self.endTagOther(token)
                    return

                # Otherwise, if there is such a node, but that node is
                # not in the stack of open elements, then this is a
                # parse error; remove the element from the list, and
                # abort these steps.
                elif formattingElement not in self.tree.openElements:
                    self.parser.parseError("adoption-agency-1.2", {"name": token["name"]})
                    self.tree.activeFormattingElements.remove(formattingElement)
                    return

                # Otherwise, if there is such a node, and that node is
                # also in the stack of open elements, but the element
                # is not in scope, then this is a parse error; ignore
                # the token, and abort these steps.
                elif not self.tree.elementInScope(formattingElement.name):
                    self.parser.parseError("adoption-agency-4.4", {"name": token["name"]})
                    return

                # Otherwise, there is a formatting element and that
                # element is in the stack and is in scope. If the
                # element is not the current node, this is a parse
                # error. In any case, proceed with the algorithm as
                # written in the following steps.
                else:
                    if formattingElement != self.tree.openElements[-1]:
                        self.parser.parseError("adoption-agency-1.3", {"name": token["name"]})

                # Step 5:

                # Let the furthest block be the topmost node in the
                # stack of open elements that is lower in the stack
                # than the formatting element, and is an element in
                # the special category. There might not be one.
                afeIndex = self.tree.openElements.index(formattingElement)
                furthestBlock = None
                for element in self.tree.openElements[afeIndex:]:
                    if element.nameTuple in specialElements:
                        furthestBlock = element
                        break

                # Step 6:

                # If there is no furthest block, then the UA must
                # first pop all the nodes from the bottom of the stack
                # of open elements, from the current node up to and
                # including the formatting element, then remove the
                # formatting element from the list of active
                # formatting elements, and finally abort these steps.
                if furthestBlock is None:
                    element = self.tree.openElements.pop()
                    while element != formattingElement:
                        element = self.tree.openElements.pop()
                    self.tree.activeFormattingElements.remove(element)
                    return

                # Step 7
                commonAncestor = self.tree.openElements[afeIndex - 1]

                # Step 8:
                # The bookmark is supposed to help us identify where to reinsert
                # nodes in step 15. We have to ensure that we reinsert nodes after
                # the node before the active formatting element. Note the bookmark
                # can move in step 9.7
                bookmark = self.tree.activeFormattingElements.index(formattingElement)

                # Step 9
                lastNode = node = furthestBlock
                innerLoopCounter = 0

                index = self.tree.openElements.index(node)
                while innerLoopCounter < 3:
                    innerLoopCounter += 1
                    # Node is element before node in open elements
                    index -= 1
                    node = self.tree.openElements[index]
                    if node not in self.tree.activeFormattingElements:
                        self.tree.openElements.remove(node)
                        continue
                    # Step 9.6
                    if node == formattingElement:
                        break
                    # Step 9.7
                    if lastNode == furthestBlock:
                        bookmark = self.tree.activeFormattingElements.index(node) + 1
                    # Step 9.8
                    clone = node.cloneNode()
                    # Replace node with clone
                    self.tree.activeFormattingElements[
                        self.tree.activeFormattingElements.index(node)] = clone
                    self.tree.openElements[
                        self.tree.openElements.index(node)] = clone
                    node = clone
                    # Step 9.9
                    # Remove lastNode from its parents, if any
                    if lastNode.parent:
                        lastNode.parent.removeChild(lastNode)
                    node.appendChild(lastNode)
                    # Step 9.10
                    lastNode = node

                # Step 10
                # Foster parent lastNode if commonAncestor is a
                # table, tbody, tfoot, thead, or tr we need to foster
                # parent the lastNode
                if lastNode.parent:
                    lastNode.parent.removeChild(lastNode)

                if commonAncestor.name in frozenset(("table", "tbody", "tfoot", "thead", "tr")):
                    parent, insertBefore = self.tree.getTableMisnestedNodePosition()
                    parent.insertBefore(lastNode, insertBefore)
                else:
                    commonAncestor.appendChild(lastNode)

                # Step 11
                clone = formattingElement.cloneNode()

                # Step 12
                furthestBlock.reparentChildren(clone)

                # Step 13
                furthestBlock.appendChild(clone)

                # Step 14
                self.tree.activeFormattingElements.remove(formattingElement)
                self.tree.activeFormattingElements.insert(bookmark, clone)

                # Step 15
                self.tree.openElements.remove(formattingElement)
                self.tree.openElements.insert(
                    self.tree.openElements.index(furthestBlock) + 1, clone)

        def endTagAppletMarqueeObject(self, token):
            if self.tree.elementInScope(token["name"]):
                self.tree.generateImpliedEndTags()
            if self.tree.openElements[-1].name != token["name"]:
                self.parser.parseError("end-tag-too-early", {"name": token["name"]})

            if self.tree.elementInScope(token["name"]):
                element = self.tree.openElements.pop()
                while element.name != token["name"]:
                    element = self.tree.openElements.pop()
                self.tree.clearActiveFormattingElements()

        def endTagBr(self, token):
            self.parser.parseError("unexpected-end-tag-treated-as",
                                   {"originalName": "br", "newName": "br element"})
            self.tree.reconstructActiveFormattingElements()
            self.tree.insertElement(impliedTagToken("br", "StartTag"))
            self.tree.openElements.pop()

        def endTagOther(self, token):
            for node in self.tree.openElements[::-1]:
                if node.name == token["name"]:
                    self.tree.generateImpliedEndTags(exclude=token["name"])
                    if self.tree.openElements[-1].name != token["name"]:
                        self.parser.parseError("unexpected-end-tag", {"name": token["name"]})
                    while self.tree.openElements.pop() != node:
                        pass
                    break
                else:
                    if node.nameTuple in specialElements:
                        self.parser.parseError("unexpected-end-tag", {"name": token["name"]})
                        break

        startTagHandler = _utils.MethodDispatcher([
            ("html", Phase.startTagHtml),
            (("base", "basefont", "bgsound", "command", "link", "meta",
              "script", "style", "title"),
             startTagProcessInHead),
            ("body", startTagBody),
            ("frameset", startTagFrameset),
            (("address", "article", "aside", "blockquote", "center", "details",
              "dir", "div", "dl", "fieldset", "figcaption", "figure",
              "footer", "header", "hgroup", "main", "menu", "nav", "ol", "p",
              "section", "summary", "ul"),
             startTagCloseP),
            (headingElements, startTagHeading),
            (("pre", "listing"), startTagPreListing),
            ("form", startTagForm),
            (("li", "dd", "dt"), startTagListItem),
            ("plaintext", startTagPlaintext),
            ("a", startTagA),
            (("b", "big", "code", "em", "font", "i", "s", "small", "strike",
              "strong", "tt", "u"), startTagFormatting),
            ("nobr", startTagNobr),
            ("button", startTagButton),
            (("applet", "marquee", "object"), startTagAppletMarqueeObject),
            ("xmp", startTagXmp),
            ("table", startTagTable),
            (("area", "br", "embed", "img", "keygen", "wbr"),
             startTagVoidFormatting),
            (("param", "source", "track"), startTagParamSource),
            ("input", startTagInput),
            ("hr", startTagHr),
            ("image", startTagImage),
            ("isindex", startTagIsIndex),
            ("textarea", startTagTextarea),
            ("iframe", startTagIFrame),
            ("noscript", startTagNoscript),
            (("noembed", "noframes"), startTagRawtext),
            ("select", startTagSelect),
            (("rp", "rt"), startTagRpRt),
            (("option", "optgroup"), startTagOpt),
            (("math"), startTagMath),
            (("svg"), startTagSvg),
            (("caption", "col", "colgroup", "frame", "head",
              "tbody", "td", "tfoot", "th", "thead",
              "tr"), startTagMisplaced)
        ])
        startTagHandler.default = startTagOther

        endTagHandler = _utils.MethodDispatcher([
            ("body", endTagBody),
            ("html", endTagHtml),
            (("address", "article", "aside", "blockquote", "button", "center",
              "details", "dialog", "dir", "div", "dl", "fieldset", "figcaption", "figure",
              "footer", "header", "hgroup", "listing", "main", "menu", "nav", "ol", "pre",
              "section", "summary", "ul"), endTagBlock),
            ("form", endTagForm),
            ("p", endTagP),
            (("dd", "dt", "li"), endTagListItem),
            (headingElements, endTagHeading),
            (("a", "b", "big", "code", "em", "font", "i", "nobr", "s", "small",
              "strike", "strong", "tt", "u"), endTagFormatting),
            (("applet", "marquee", "object"), endTagAppletMarqueeObject),
            ("br", endTagBr),
        ])
        endTagHandler.default = endTagOther

    class TextPhase(Phase):
        __slots__ = tuple()

        def processCharacters(self, token):
            self.tree.insertText(token["data"])

        def processEOF(self):
            self.parser.parseError("expected-named-closing-tag-but-got-eof",
                                   {"name": self.tree.openElements[-1].name})
            self.tree.openElements.pop()
            self.parser.phase = self.parser.originalPhase
            return True

        def startTagOther(self, token):
            assert False, "Tried to process start tag %s in RCDATA/RAWTEXT mode" % token['name']

        def endTagScript(self, token):
            node = self.tree.openElements.pop()
            assert node.name == "script"
            self.parser.phase = self.parser.originalPhase
            # The rest of this method is all stuff that only happens if
            # document.write works

        def endTagOther(self, token):
            self.tree.openElements.pop()
            self.parser.phase = self.parser.originalPhase

        startTagHandler = _utils.MethodDispatcher([])
        startTagHandler.default = startTagOther
        endTagHandler = _utils.MethodDispatcher([
            ("script", endTagScript)])
        endTagHandler.default = endTagOther

    class InTablePhase(Phase):
        # http://www.whatwg.org/specs/web-apps/current-work/#in-table
        __slots__ = tuple()

        # helper methods
        def clearStackToTableContext(self):
            # "clear the stack back to a table context"
            while self.tree.openElements[-1].name not in ("table", "html"):
                # self.parser.parseError("unexpected-implied-end-tag-in-table",
                #  {"name":  self.tree.openElements[-1].name})
                self.tree.openElements.pop()
            # When the current node is <html> it's an innerHTML case

        # processing methods
        def processEOF(self):
            if self.tree.openElements[-1].name != "html":
                self.parser.parseError("eof-in-table")
            else:
                assert self.parser.innerHTML
            # Stop parsing

        def processSpaceCharacters(self, token):
            originalPhase = self.parser.phase
            self.parser.phase = self.parser.phases["inTableText"]
            self.parser.phase.originalPhase = originalPhase
            self.parser.phase.processSpaceCharacters(token)

        def processCharacters(self, token):
            originalPhase = self.parser.phase
            self.parser.phase = self.parser.phases["inTableText"]
            self.parser.phase.originalPhase = originalPhase
            self.parser.phase.processCharacters(token)

        def insertText(self, token):
            # If we get here there must be at least one non-whitespace character
            # Do the table magic!
            self.tree.insertFromTable = True
            self.parser.phases["inBody"].processCharacters(token)
            self.tree.insertFromTable = False

        def startTagCaption(self, token):
            self.clearStackToTableContext()
            self.tree.activeFormattingElements.append(Marker)
            self.tree.insertElement(token)
            self.parser.phase = self.parser.phases["inCaption"]

        def startTagColgroup(self, token):
            self.clearStackToTableContext()
            self.tree.insertElement(token)
            self.parser.phase = self.parser.phases["inColumnGroup"]

        def startTagCol(self, token):
            self.startTagColgroup(impliedTagToken("colgroup", "StartTag"))
            return token

        def startTagRowGroup(self, token):
            self.clearStackToTableContext()
            self.tree.insertElement(token)
            self.parser.phase = self.parser.phases["inTableBody"]

        def startTagImplyTbody(self, token):
            self.startTagRowGroup(impliedTagToken("tbody", "StartTag"))
            return token

        def startTagTable(self, token):
            self.parser.parseError("unexpected-start-tag-implies-end-tag",
                                   {"startName": "table", "endName": "table"})
            self.parser.phase.processEndTag(impliedTagToken("table"))
            if not self.parser.innerHTML:
                return token

        def startTagStyleScript(self, token):
            return self.parser.phases["inHead"].processStartTag(token)

        def startTagInput(self, token):
            if ("type" in token["data"] and
                    token["data"]["type"].translate(asciiUpper2Lower) == "hidden"):
                self.parser.parseError("unexpected-hidden-input-in-table")
                self.tree.insertElement(token)
                # XXX associate with form
                self.tree.openElements.pop()
            else:
                self.startTagOther(token)

        def startTagForm(self, token):
            self.parser.parseError("unexpected-form-in-table")
            if self.tree.formPointer is None:
                self.tree.insertElement(token)
                self.tree.formPointer = self.tree.openElements[-1]
                self.tree.openElements.pop()

        def startTagOther(self, token):
            self.parser.parseError("unexpected-start-tag-implies-table-voodoo", {"name": token["name"]})
            # Do the table magic!
            self.tree.insertFromTable = True
            self.parser.phases["inBody"].processStartTag(token)
            self.tree.insertFromTable = False

        def endTagTable(self, token):
            if self.tree.elementInScope("table", variant="table"):
                self.tree.generateImpliedEndTags()
                if self.tree.openElements[-1].name != "table":
                    self.parser.parseError("end-tag-too-early-named",
                                           {"gotName": "table",
                                            "expectedName": self.tree.openElements[-1].name})
                while self.tree.openElements[-1].name != "table":
                    self.tree.openElements.pop()
                self.tree.openElements.pop()
                self.parser.resetInsertionMode()
            else:
                # innerHTML case
                assert self.parser.innerHTML
                self.parser.parseError()

        def endTagIgnore(self, token):
            self.parser.parseError("unexpected-end-tag", {"name": token["name"]})

        def endTagOther(self, token):
            self.parser.parseError("unexpected-end-tag-implies-table-voodoo", {"name": token["name"]})
            # Do the table magic!
            self.tree.insertFromTable = True
            self.parser.phases["inBody"].processEndTag(token)
            self.tree.insertFromTable = False

        startTagHandler = _utils.MethodDispatcher([
            ("html", Phase.startTagHtml),
            ("caption", startTagCaption),
            ("colgroup", startTagColgroup),
            ("col", startTagCol),
            (("tbody", "tfoot", "thead"), startTagRowGroup),
            (("td", "th", "tr"), startTagImplyTbody),
            ("table", startTagTable),
            (("style", "script"), startTagStyleScript),
            ("input", startTagInput),
            ("form", startTagForm)
        ])
        startTagHandler.default = startTagOther

        endTagHandler = _utils.MethodDispatcher([
            ("table", endTagTable),
            (("body", "caption", "col", "colgroup", "html", "tbody", "td",
              "tfoot", "th", "thead", "tr"), endTagIgnore)
        ])
        endTagHandler.default = endTagOther

    class InTableTextPhase(Phase):
        __slots__ = ("originalPhase", "characterTokens")

        def __init__(self, *args, **kwargs):
            super(InTableTextPhase, self).__init__(*args, **kwargs)
            self.originalPhase = None
            self.characterTokens = []

        def flushCharacters(self):
            data = "".join([item["data"] for item in self.characterTokens])
            if any([item not in spaceCharacters for item in data]):
                token = {"type": tokenTypes["Characters"], "data": data}
                self.parser.phases["inTable"].insertText(token)
            elif data:
                self.tree.insertText(data)
            self.characterTokens = []

        def processComment(self, token):
            self.flushCharacters()
            self.parser.phase = self.originalPhase
            return token

        def processEOF(self):
            self.flushCharacters()
            self.parser.phase = self.originalPhase
            return True

        def processCharacters(self, token):
            if token["data"] == "\u0000":
                return
            self.characterTokens.append(token)

        def processSpaceCharacters(self, token):
            # pretty sure we should never reach here
            self.characterTokens.append(token)
    #        assert False

        def processStartTag(self, token):
            self.flushCharacters()
            self.parser.phase = self.originalPhase
            return token

        def processEndTag(self, token):
            self.flushCharacters()
            self.parser.phase = self.originalPhase
            return token

    class InCaptionPhase(Phase):
        # http://www.whatwg.org/specs/web-apps/current-work/#in-caption
        __slots__ = tuple()

        def ignoreEndTagCaption(self):
            return not self.tree.elementInScope("caption", variant="table")

        def processEOF(self):
            self.parser.phases["inBody"].processEOF()

        def processCharacters(self, token):
            return self.parser.phases["inBody"].processCharacters(token)

        def startTagTableElement(self, token):
            self.parser.parseError()
            # XXX Have to duplicate logic here to find out if the tag is ignored
            ignoreEndTag = self.ignoreEndTagCaption()
            self.parser.phase.processEndTag(impliedTagToken("caption"))
            if not ignoreEndTag:
                return token

        def startTagOther(self, token):
            return self.parser.phases["inBody"].processStartTag(token)

        def endTagCaption(self, token):
            if not self.ignoreEndTagCaption():
                # AT this code is quite similar to endTagTable in "InTable"
                self.tree.generateImpliedEndTags()
                if self.tree.openElements[-1].name != "caption":
                    self.parser.parseError("expected-one-end-tag-but-got-another",
                                           {"gotName": "caption",
                                            "expectedName": self.tree.openElements[-1].name})
                while self.tree.openElements[-1].name != "caption":
                    self.tree.openElements.pop()
                self.tree.openElements.pop()
                self.tree.clearActiveFormattingElements()
                self.parser.phase = self.parser.phases["inTable"]
            else:
                # innerHTML case
                assert self.parser.innerHTML
                self.parser.parseError()

        def endTagTable(self, token):
            self.parser.parseError()
            ignoreEndTag = self.ignoreEndTagCaption()
            self.parser.phase.processEndTag(impliedTagToken("caption"))
            if not ignoreEndTag:
                return token

        def endTagIgnore(self, token):
            self.parser.parseError("unexpected-end-tag", {"name": token["name"]})

        def endTagOther(self, token):
            return self.parser.phases["inBody"].processEndTag(token)

        startTagHandler = _utils.MethodDispatcher([
            ("html", Phase.startTagHtml),
            (("caption", "col", "colgroup", "tbody", "td", "tfoot", "th",
              "thead", "tr"), startTagTableElement)
        ])
        startTagHandler.default = startTagOther

        endTagHandler = _utils.MethodDispatcher([
            ("caption", endTagCaption),
            ("table", endTagTable),
            (("body", "col", "colgroup", "html", "tbody", "td", "tfoot", "th",
              "thead", "tr"), endTagIgnore)
        ])
        endTagHandler.default = endTagOther

    class InColumnGroupPhase(Phase):
        # http://www.whatwg.org/specs/web-apps/current-work/#in-column
        __slots__ = tuple()

        def ignoreEndTagColgroup(self):
            return self.tree.openElements[-1].name == "html"

        def processEOF(self):
            if self.tree.openElements[-1].name == "html":
                assert self.parser.innerHTML
                return
            else:
                ignoreEndTag = self.ignoreEndTagColgroup()
                self.endTagColgroup(impliedTagToken("colgroup"))
                if not ignoreEndTag:
                    return True

        def processCharacters(self, token):
            ignoreEndTag = self.ignoreEndTagColgroup()
            self.endTagColgroup(impliedTagToken("colgroup"))
            if not ignoreEndTag:
                return token

        def startTagCol(self, token):
            self.tree.insertElement(token)
            self.tree.openElements.pop()
            token["selfClosingAcknowledged"] = True

        def startTagOther(self, token):
            ignoreEndTag = self.ignoreEndTagColgroup()
            self.endTagColgroup(impliedTagToken("colgroup"))
            if not ignoreEndTag:
                return token

        def endTagColgroup(self, token):
            if self.ignoreEndTagColgroup():
                # innerHTML case
                assert self.parser.innerHTML
                self.parser.parseError()
            else:
                self.tree.openElements.pop()
                self.parser.phase = self.parser.phases["inTable"]

        def endTagCol(self, token):
            self.parser.parseError("no-end-tag", {"name": "col"})

        def endTagOther(self, token):
            ignoreEndTag = self.ignoreEndTagColgroup()
            self.endTagColgroup(impliedTagToken("colgroup"))
            if not ignoreEndTag:
                return token

        startTagHandler = _utils.MethodDispatcher([
            ("html", Phase.startTagHtml),
            ("col", startTagCol)
        ])
        startTagHandler.default = startTagOther

        endTagHandler = _utils.MethodDispatcher([
            ("colgroup", endTagColgroup),
            ("col", endTagCol)
        ])
        endTagHandler.default = endTagOther

    class InTableBodyPhase(Phase):
        # http://www.whatwg.org/specs/web-apps/current-work/#in-table0
        __slots__ = tuple()

        # helper methods
        def clearStackToTableBodyContext(self):
            while self.tree.openElements[-1].name not in ("tbody", "tfoot",
                                                          "thead", "html"):
                # self.parser.parseError("unexpected-implied-end-tag-in-table",
                #  {"name": self.tree.openElements[-1].name})
                self.tree.openElements.pop()
            if self.tree.openElements[-1].name == "html":
                assert self.parser.innerHTML

        # the rest
        def processEOF(self):
            self.parser.phases["inTable"].processEOF()

        def processSpaceCharacters(self, token):
            return self.parser.phases["inTable"].processSpaceCharacters(token)

        def processCharacters(self, token):
            return self.parser.phases["inTable"].processCharacters(token)

        def startTagTr(self, token):
            self.clearStackToTableBodyContext()
            self.tree.insertElement(token)
            self.parser.phase = self.parser.phases["inRow"]

        def startTagTableCell(self, token):
            self.parser.parseError("unexpected-cell-in-table-body",
                                   {"name": token["name"]})
            self.startTagTr(impliedTagToken("tr", "StartTag"))
            return token

        def startTagTableOther(self, token):
            # XXX AT Any ideas on how to share this with endTagTable?
            if (self.tree.elementInScope("tbody", variant="table") or
                self.tree.elementInScope("thead", variant="table") or
                    self.tree.elementInScope("tfoot", variant="table")):
                self.clearStackToTableBodyContext()
                self.endTagTableRowGroup(
                    impliedTagToken(self.tree.openElements[-1].name))
                return token
            else:
                # innerHTML case
                assert self.parser.innerHTML
                self.parser.parseError()

        def startTagOther(self, token):
            return self.parser.phases["inTable"].processStartTag(token)

        def endTagTableRowGroup(self, token):
            if self.tree.elementInScope(token["name"], variant="table"):
                self.clearStackToTableBodyContext()
                self.tree.openElements.pop()
                self.parser.phase = self.parser.phases["inTable"]
            else:
                self.parser.parseError("unexpected-end-tag-in-table-body",
                                       {"name": token["name"]})

        def endTagTable(self, token):
            if (self.tree.elementInScope("tbody", variant="table") or
                self.tree.elementInScope("thead", variant="table") or
                    self.tree.elementInScope("tfoot", variant="table")):
                self.clearStackToTableBodyContext()
                self.endTagTableRowGroup(
                    impliedTagToken(self.tree.openElements[-1].name))
                return token
            else:
                # innerHTML case
                assert self.parser.innerHTML
                self.parser.parseError()

        def endTagIgnore(self, token):
            self.parser.parseError("unexpected-end-tag-in-table-body",
                                   {"name": token["name"]})

        def endTagOther(self, token):
            return self.parser.phases["inTable"].processEndTag(token)

        startTagHandler = _utils.MethodDispatcher([
            ("html", Phase.startTagHtml),
            ("tr", startTagTr),
            (("td", "th"), startTagTableCell),
            (("caption", "col", "colgroup", "tbody", "tfoot", "thead"),
             startTagTableOther)
        ])
        startTagHandler.default = startTagOther

        endTagHandler = _utils.MethodDispatcher([
            (("tbody", "tfoot", "thead"), endTagTableRowGroup),
            ("table", endTagTable),
            (("body", "caption", "col", "colgroup", "html", "td", "th",
              "tr"), endTagIgnore)
        ])
        endTagHandler.default = endTagOther

    class InRowPhase(Phase):
        # http://www.whatwg.org/specs/web-apps/current-work/#in-row
        __slots__ = tuple()

        # helper methods (XXX unify this with other table helper methods)
        def clearStackToTableRowContext(self):
            while self.tree.openElements[-1].name not in ("tr", "html"):
                self.parser.parseError("unexpected-implied-end-tag-in-table-row",
                                       {"name": self.tree.openElements[-1].name})
                self.tree.openElements.pop()

        def ignoreEndTagTr(self):
            return not self.tree.elementInScope("tr", variant="table")

        # the rest
        def processEOF(self):
            self.parser.phases["inTable"].processEOF()

        def processSpaceCharacters(self, token):
            return self.parser.phases["inTable"].processSpaceCharacters(token)

        def processCharacters(self, token):
            return self.parser.phases["inTable"].processCharacters(token)

        def startTagTableCell(self, token):
            self.clearStackToTableRowContext()
            self.tree.insertElement(token)
            self.parser.phase = self.parser.phases["inCell"]
            self.tree.activeFormattingElements.append(Marker)

        def startTagTableOther(self, token):
            ignoreEndTag = self.ignoreEndTagTr()
            self.endTagTr(impliedTagToken("tr"))
            # XXX how are we sure it's always ignored in the innerHTML case?
            if not ignoreEndTag:
                return token

        def startTagOther(self, token):
            return self.parser.phases["inTable"].processStartTag(token)

        def endTagTr(self, token):
            if not self.ignoreEndTagTr():
                self.clearStackToTableRowContext()
                self.tree.openElements.pop()
                self.parser.phase = self.parser.phases["inTableBody"]
            else:
                # innerHTML case
                assert self.parser.innerHTML
                self.parser.parseError()

        def endTagTable(self, token):
            ignoreEndTag = self.ignoreEndTagTr()
            self.endTagTr(impliedTagToken("tr"))
            # Reprocess the current tag if the tr end tag was not ignored
            # XXX how are we sure it's always ignored in the innerHTML case?
            if not ignoreEndTag:
                return token

        def endTagTableRowGroup(self, token):
            if self.tree.elementInScope(token["name"], variant="table"):
                self.endTagTr(impliedTagToken("tr"))
                return token
            else:
                self.parser.parseError()

        def endTagIgnore(self, token):
            self.parser.parseError("unexpected-end-tag-in-table-row",
                                   {"name": token["name"]})

        def endTagOther(self, token):
            return self.parser.phases["inTable"].processEndTag(token)

        startTagHandler = _utils.MethodDispatcher([
            ("html", Phase.startTagHtml),
            (("td", "th"), startTagTableCell),
            (("caption", "col", "colgroup", "tbody", "tfoot", "thead",
              "tr"), startTagTableOther)
        ])
        startTagHandler.default = startTagOther

        endTagHandler = _utils.MethodDispatcher([
            ("tr", endTagTr),
            ("table", endTagTable),
            (("tbody", "tfoot", "thead"), endTagTableRowGroup),
            (("body", "caption", "col", "colgroup", "html", "td", "th"),
             endTagIgnore)
        ])
        endTagHandler.default = endTagOther

    class InCellPhase(Phase):
        # http://www.whatwg.org/specs/web-apps/current-work/#in-cell
        __slots__ = tuple()

        # helper
        def closeCell(self):
            if self.tree.elementInScope("td", variant="table"):
                self.endTagTableCell(impliedTagToken("td"))
            elif self.tree.elementInScope("th", variant="table"):
                self.endTagTableCell(impliedTagToken("th"))

        # the rest
        def processEOF(self):
            self.parser.phases["inBody"].processEOF()

        def processCharacters(self, token):
            return self.parser.phases["inBody"].processCharacters(token)

        def startTagTableOther(self, token):
            if (self.tree.elementInScope("td", variant="table") or
                    self.tree.elementInScope("th", variant="table")):
                self.closeCell()
                return token
            else:
                # innerHTML case
                assert self.parser.innerHTML
                self.parser.parseError()

        def startTagOther(self, token):
            return self.parser.phases["inBody"].processStartTag(token)

        def endTagTableCell(self, token):
            if self.tree.elementInScope(token["name"], variant="table"):
                self.tree.generateImpliedEndTags(token["name"])
                if self.tree.openElements[-1].name != token["name"]:
                    self.parser.parseError("unexpected-cell-end-tag",
                                           {"name": token["name"]})
                    while True:
                        node = self.tree.openElements.pop()
                        if node.name == token["name"]:
                            break
                else:
                    self.tree.openElements.pop()
                self.tree.clearActiveFormattingElements()
                self.parser.phase = self.parser.phases["inRow"]
            else:
                self.parser.parseError("unexpected-end-tag", {"name": token["name"]})

        def endTagIgnore(self, token):
            self.parser.parseError("unexpected-end-tag", {"name": token["name"]})

        def endTagImply(self, token):
            if self.tree.elementInScope(token["name"], variant="table"):
                self.closeCell()
                return token
            else:
                # sometimes innerHTML case
                self.parser.parseError()

        def endTagOther(self, token):
            return self.parser.phases["inBody"].processEndTag(token)

        startTagHandler = _utils.MethodDispatcher([
            ("html", Phase.startTagHtml),
            (("caption", "col", "colgroup", "tbody", "td", "tfoot", "th",
              "thead", "tr"), startTagTableOther)
        ])
        startTagHandler.default = startTagOther

        endTagHandler = _utils.MethodDispatcher([
            (("td", "th"), endTagTableCell),
            (("body", "caption", "col", "colgroup", "html"), endTagIgnore),
            (("table", "tbody", "tfoot", "thead", "tr"), endTagImply)
        ])
        endTagHandler.default = endTagOther

    class InSelectPhase(Phase):
        __slots__ = tuple()

        # http://www.whatwg.org/specs/web-apps/current-work/#in-select
        def processEOF(self):
            if self.tree.openElements[-1].name != "html":
                self.parser.parseError("eof-in-select")
            else:
                assert self.parser.innerHTML

        def processCharacters(self, token):
            if token["data"] == "\u0000":
                return
            self.tree.insertText(token["data"])

        def startTagOption(self, token):
            # We need to imply </option> if <option> is the current node.
            if self.tree.openElements[-1].name == "option":
                self.tree.openElements.pop()
            self.tree.insertElement(token)

        def startTagOptgroup(self, token):
            if self.tree.openElements[-1].name == "option":
                self.tree.openElements.pop()
            if self.tree.openElements[-1].name == "optgroup":
                self.tree.openElements.pop()
            self.tree.insertElement(token)

        def startTagSelect(self, token):
            self.parser.parseError("unexpected-select-in-select")
            self.endTagSelect(impliedTagToken("select"))

        def startTagInput(self, token):
            self.parser.parseError("unexpected-input-in-select")
            if self.tree.elementInScope("select", variant="select"):
                self.endTagSelect(impliedTagToken("select"))
                return token
            else:
                assert self.parser.innerHTML

        def startTagScript(self, token):
            return self.parser.phases["inHead"].processStartTag(token)

        def startTagOther(self, token):
            self.parser.parseError("unexpected-start-tag-in-select",
                                   {"name": token["name"]})

        def endTagOption(self, token):
            if self.tree.openElements[-1].name == "option":
                self.tree.openElements.pop()
            else:
                self.parser.parseError("unexpected-end-tag-in-select",
                                       {"name": "option"})

        def endTagOptgroup(self, token):
            # </optgroup> implicitly closes <option>
            if (self.tree.openElements[-1].name == "option" and
                    self.tree.openElements[-2].name == "optgroup"):
                self.tree.openElements.pop()
            # It also closes </optgroup>
            if self.tree.openElements[-1].name == "optgroup":
                self.tree.openElements.pop()
            # But nothing else
            else:
                self.parser.parseError("unexpected-end-tag-in-select",
                                       {"name": "optgroup"})

        def endTagSelect(self, token):
            if self.tree.elementInScope("select", variant="select"):
                node = self.tree.openElements.pop()
                while node.name != "select":
                    node = self.tree.openElements.pop()
                self.parser.resetInsertionMode()
            else:
                # innerHTML case
                assert self.parser.innerHTML
                self.parser.parseError()

        def endTagOther(self, token):
            self.parser.parseError("unexpected-end-tag-in-select",
                                   {"name": token["name"]})

        startTagHandler = _utils.MethodDispatcher([
            ("html", Phase.startTagHtml),
            ("option", startTagOption),
            ("optgroup", startTagOptgroup),
            ("select", startTagSelect),
            (("input", "keygen", "textarea"), startTagInput),
            ("script", startTagScript)
        ])
        startTagHandler.default = startTagOther

        endTagHandler = _utils.MethodDispatcher([
            ("option", endTagOption),
            ("optgroup", endTagOptgroup),
            ("select", endTagSelect)
        ])
        endTagHandler.default = endTagOther

    class InSelectInTablePhase(Phase):
        __slots__ = tuple()

        def processEOF(self):
            self.parser.phases["inSelect"].processEOF()

        def processCharacters(self, token):
            return self.parser.phases["inSelect"].processCharacters(token)

        def startTagTable(self, token):
            self.parser.parseError("unexpected-table-element-start-tag-in-select-in-table", {"name": token["name"]})
            self.endTagOther(impliedTagToken("select"))
            return token

        def startTagOther(self, token):
            return self.parser.phases["inSelect"].processStartTag(token)

        def endTagTable(self, token):
            self.parser.parseError("unexpected-table-element-end-tag-in-select-in-table", {"name": token["name"]})
            if self.tree.elementInScope(token["name"], variant="table"):
                self.endTagOther(impliedTagToken("select"))
                return token

        def endTagOther(self, token):
            return self.parser.phases["inSelect"].processEndTag(token)

        startTagHandler = _utils.MethodDispatcher([
            (("caption", "table", "tbody", "tfoot", "thead", "tr", "td", "th"),
             startTagTable)
        ])
        startTagHandler.default = startTagOther

        endTagHandler = _utils.MethodDispatcher([
            (("caption", "table", "tbody", "tfoot", "thead", "tr", "td", "th"),
             endTagTable)
        ])
        endTagHandler.default = endTagOther

    class InForeignContentPhase(Phase):
        __slots__ = tuple()

        breakoutElements = frozenset(["b", "big", "blockquote", "body", "br",
                                      "center", "code", "dd", "div", "dl", "dt",
                                      "em", "embed", "h1", "h2", "h3",
                                      "h4", "h5", "h6", "head", "hr", "i", "img",
                                      "li", "listing", "menu", "meta", "nobr",
                                      "ol", "p", "pre", "ruby", "s", "small",
                                      "span", "strong", "strike", "sub", "sup",
                                      "table", "tt", "u", "ul", "var"])

        def adjustSVGTagNames(self, token):
            replacements = {"altglyph": "altGlyph",
                            "altglyphdef": "altGlyphDef",
                            "altglyphitem": "altGlyphItem",
                            "animatecolor": "animateColor",
                            "animatemotion": "animateMotion",
                            "animatetransform": "animateTransform",
                            "clippath": "clipPath",
                            "feblend": "feBlend",
                            "fecolormatrix": "feColorMatrix",
                            "fecomponenttransfer": "feComponentTransfer",
                            "fecomposite": "feComposite",
                            "feconvolvematrix": "feConvolveMatrix",
                            "fediffuselighting": "feDiffuseLighting",
                            "fedisplacementmap": "feDisplacementMap",
                            "fedistantlight": "feDistantLight",
                            "feflood": "feFlood",
                            "fefunca": "feFuncA",
                            "fefuncb": "feFuncB",
                            "fefuncg": "feFuncG",
                            "fefuncr": "feFuncR",
                            "fegaussianblur": "feGaussianBlur",
                            "feimage": "feImage",
                            "femerge": "feMerge",
                            "femergenode": "feMergeNode",
                            "femorphology": "feMorphology",
                            "feoffset": "feOffset",
                            "fepointlight": "fePointLight",
                            "fespecularlighting": "feSpecularLighting",
                            "fespotlight": "feSpotLight",
                            "fetile": "feTile",
                            "feturbulence": "feTurbulence",
                            "foreignobject": "foreignObject",
                            "glyphref": "glyphRef",
                            "lineargradient": "linearGradient",
                            "radialgradient": "radialGradient",
                            "textpath": "textPath"}

            if token["name"] in replacements:
                token["name"] = replacements[token["name"]]

        def processCharacters(self, token):
            if token["data"] == "\u0000":
                token["data"] = "\uFFFD"
            elif (self.parser.framesetOK and
                  any(char not in spaceCharacters for char in token["data"])):
                self.parser.framesetOK = False
            Phase.processCharacters(self, token)

        def processStartTag(self, token):
            currentNode = self.tree.openElements[-1]
            if (token["name"] in self.breakoutElements or
                (token["name"] == "font" and
                 set(token["data"].keys()) & {"color", "face", "size"})):
                self.parser.parseError("unexpected-html-element-in-foreign-content",
                                       {"name": token["name"]})
                while (self.tree.openElements[-1].namespace !=
                       self.tree.defaultNamespace and
                       not self.parser.isHTMLIntegrationPoint(self.tree.openElements[-1]) and
                       not self.parser.isMathMLTextIntegrationPoint(self.tree.openElements[-1])):
                    self.tree.openElements.pop()
                return token

            else:
                if currentNode.namespace == namespaces["mathml"]:
                    self.parser.adjustMathMLAttributes(token)
                elif currentNode.namespace == namespaces["svg"]:
                    self.adjustSVGTagNames(token)
                    self.parser.adjustSVGAttributes(token)
                self.parser.adjustForeignAttributes(token)
                token["namespace"] = currentNode.namespace
                self.tree.insertElement(token)
                if token["selfClosing"]:
                    self.tree.openElements.pop()
                    token["selfClosingAcknowledged"] = True

        def processEndTag(self, token):
            nodeIndex = len(self.tree.openElements) - 1
            node = self.tree.openElements[-1]
            if node.name.translate(asciiUpper2Lower) != token["name"]:
                self.parser.parseError("unexpected-end-tag", {"name": token["name"]})

            while True:
                if node.name.translate(asciiUpper2Lower) == token["name"]:
                    # XXX this isn't in the spec but it seems necessary
                    if self.parser.phase == self.parser.phases["inTableText"]:
                        self.parser.phase.flushCharacters()
                        self.parser.phase = self.parser.phase.originalPhase
                    while self.tree.openElements.pop() != node:
                        assert self.tree.openElements
                    new_token = None
                    break
                nodeIndex -= 1

                node = self.tree.openElements[nodeIndex]
                if node.namespace != self.tree.defaultNamespace:
                    continue
                else:
                    new_token = self.parser.phase.processEndTag(token)
                    break
            return new_token

    class AfterBodyPhase(Phase):
        __slots__ = tuple()

        def processEOF(self):
            # Stop parsing
            pass

        def processComment(self, token):
            # This is needed because data is to be appended to the <html> element
            # here and not to whatever is currently open.
            self.tree.insertComment(token, self.tree.openElements[0])

        def processCharacters(self, token):
            self.parser.parseError("unexpected-char-after-body")
            self.parser.phase = self.parser.phases["inBody"]
            return token

        def startTagHtml(self, token):
            return self.parser.phases["inBody"].processStartTag(token)

        def startTagOther(self, token):
            self.parser.parseError("unexpected-start-tag-after-body",
                                   {"name": token["name"]})
            self.parser.phase = self.parser.phases["inBody"]
            return token

        def endTagHtml(self, name):
            if self.parser.innerHTML:
                self.parser.parseError("unexpected-end-tag-after-body-innerhtml")
            else:
                self.parser.phase = self.parser.phases["afterAfterBody"]

        def endTagOther(self, token):
            self.parser.parseError("unexpected-end-tag-after-body",
                                   {"name": token["name"]})
            self.parser.phase = self.parser.phases["inBody"]
            return token

        startTagHandler = _utils.MethodDispatcher([
            ("html", startTagHtml)
        ])
        startTagHandler.default = startTagOther

        endTagHandler = _utils.MethodDispatcher([("html", endTagHtml)])
        endTagHandler.default = endTagOther

    class InFramesetPhase(Phase):
        # http://www.whatwg.org/specs/web-apps/current-work/#in-frameset
        __slots__ = tuple()

        def processEOF(self):
            if self.tree.openElements[-1].name != "html":
                self.parser.parseError("eof-in-frameset")
            else:
                assert self.parser.innerHTML

        def processCharacters(self, token):
            self.parser.parseError("unexpected-char-in-frameset")

        def startTagFrameset(self, token):
            self.tree.insertElement(token)

        def startTagFrame(self, token):
            self.tree.insertElement(token)
            self.tree.openElements.pop()

        def startTagNoframes(self, token):
            return self.parser.phases["inBody"].processStartTag(token)

        def startTagOther(self, token):
            self.parser.parseError("unexpected-start-tag-in-frameset",
                                   {"name": token["name"]})

        def endTagFrameset(self, token):
            if self.tree.openElements[-1].name == "html":
                # innerHTML case
                self.parser.parseError("unexpected-frameset-in-frameset-innerhtml")
            else:
                self.tree.openElements.pop()
            if (not self.parser.innerHTML and
                    self.tree.openElements[-1].name != "frameset"):
                # If we're not in innerHTML mode and the current node is not a
                # "frameset" element (anymore) then switch.
                self.parser.phase = self.parser.phases["afterFrameset"]

        def endTagOther(self, token):
            self.parser.parseError("unexpected-end-tag-in-frameset",
                                   {"name": token["name"]})

        startTagHandler = _utils.MethodDispatcher([
            ("html", Phase.startTagHtml),
            ("frameset", startTagFrameset),
            ("frame", startTagFrame),
            ("noframes", startTagNoframes)
        ])
        startTagHandler.default = startTagOther

        endTagHandler = _utils.MethodDispatcher([
            ("frameset", endTagFrameset)
        ])
        endTagHandler.default = endTagOther

    class AfterFramesetPhase(Phase):
        # http://www.whatwg.org/specs/web-apps/current-work/#after3
        __slots__ = tuple()

        def processEOF(self):
            # Stop parsing
            pass

        def processCharacters(self, token):
            self.parser.parseError("unexpected-char-after-frameset")

        def startTagNoframes(self, token):
            return self.parser.phases["inHead"].processStartTag(token)

        def startTagOther(self, token):
            self.parser.parseError("unexpected-start-tag-after-frameset",
                                   {"name": token["name"]})

        def endTagHtml(self, token):
            self.parser.phase = self.parser.phases["afterAfterFrameset"]

        def endTagOther(self, token):
            self.parser.parseError("unexpected-end-tag-after-frameset",
                                   {"name": token["name"]})

        startTagHandler = _utils.MethodDispatcher([
            ("html", Phase.startTagHtml),
            ("noframes", startTagNoframes)
        ])
        startTagHandler.default = startTagOther

        endTagHandler = _utils.MethodDispatcher([
            ("html", endTagHtml)
        ])
        endTagHandler.default = endTagOther

    class AfterAfterBodyPhase(Phase):
        __slots__ = tuple()

        def processEOF(self):
            pass

        def processComment(self, token):
            self.tree.insertComment(token, self.tree.document)

        def processSpaceCharacters(self, token):
            return self.parser.phases["inBody"].processSpaceCharacters(token)

        def processCharacters(self, token):
            self.parser.parseError("expected-eof-but-got-char")
            self.parser.phase = self.parser.phases["inBody"]
            return token

        def startTagHtml(self, token):
            return self.parser.phases["inBody"].processStartTag(token)

        def startTagOther(self, token):
            self.parser.parseError("expected-eof-but-got-start-tag",
                                   {"name": token["name"]})
            self.parser.phase = self.parser.phases["inBody"]
            return token

        def processEndTag(self, token):
            self.parser.parseError("expected-eof-but-got-end-tag",
                                   {"name": token["name"]})
            self.parser.phase = self.parser.phases["inBody"]
            return token

        startTagHandler = _utils.MethodDispatcher([
            ("html", startTagHtml)
        ])
        startTagHandler.default = startTagOther

    class AfterAfterFramesetPhase(Phase):
        __slots__ = tuple()

        def processEOF(self):
            pass

        def processComment(self, token):
            self.tree.insertComment(token, self.tree.document)

        def processSpaceCharacters(self, token):
            return self.parser.phases["inBody"].processSpaceCharacters(token)

        def processCharacters(self, token):
            self.parser.parseError("expected-eof-but-got-char")

        def startTagHtml(self, token):
            return self.parser.phases["inBody"].processStartTag(token)

        def startTagNoFrames(self, token):
            return self.parser.phases["inHead"].processStartTag(token)

        def startTagOther(self, token):
            self.parser.parseError("expected-eof-but-got-start-tag",
                                   {"name": token["name"]})

        def processEndTag(self, token):
            self.parser.parseError("expected-eof-but-got-end-tag",
                                   {"name": token["name"]})

        startTagHandler = _utils.MethodDispatcher([
            ("html", startTagHtml),
            ("noframes", startTagNoFrames)
        ])
        startTagHandler.default = startTagOther

    # pylint:enable=unused-argument

    return {
        "initial": InitialPhase,
        "beforeHtml": BeforeHtmlPhase,
        "beforeHead": BeforeHeadPhase,
        "inHead": InHeadPhase,
        "inHeadNoscript": InHeadNoscriptPhase,
        "afterHead": AfterHeadPhase,
        "inBody": InBodyPhase,
        "text": TextPhase,
        "inTable": InTablePhase,
        "inTableText": InTableTextPhase,
        "inCaption": InCaptionPhase,
        "inColumnGroup": InColumnGroupPhase,
        "inTableBody": InTableBodyPhase,
        "inRow": InRowPhase,
        "inCell": InCellPhase,
        "inSelect": InSelectPhase,
        "inSelectInTable": InSelectInTablePhase,
        "inForeignContent": InForeignContentPhase,
        "afterBody": AfterBodyPhase,
        "inFrameset": InFramesetPhase,
        "afterFrameset": AfterFramesetPhase,
        "afterAfterBody": AfterAfterBodyPhase,
        "afterAfterFrameset": AfterAfterFramesetPhase,
        # XXX after after frameset
    }


def adjust_attributes(token, replacements):
    needs_adjustment = viewkeys(token['data']) & viewkeys(replacements)
    if needs_adjustment:
        token['data'] = type(token['data'])((replacements.get(k, k), v)
                                            for k, v in token['data'].items())


def impliedTagToken(name, type="EndTag", attributes=None,
                    selfClosing=False):
    if attributes is None:
        attributes = {}
    return {"type": tokenTypes[type], "name": name, "data": attributes,
            "selfClosing": selfClosing}


class ParseError(Exception):
    """Error in parsed document"""
    pass
