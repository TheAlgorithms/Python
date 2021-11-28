from __future__ import absolute_import, division, unicode_literals

from pip._vendor.six import text_type
from pip._vendor.six.moves import http_client, urllib

import codecs
import re
from io import BytesIO, StringIO

from pip._vendor import webencodings

from .constants import EOF, spaceCharacters, asciiLetters, asciiUppercase
from .constants import _ReparseException
from . import _utils

# Non-unicode versions of constants for use in the pre-parser
spaceCharactersBytes = frozenset([item.encode("ascii") for item in spaceCharacters])
asciiLettersBytes = frozenset([item.encode("ascii") for item in asciiLetters])
asciiUppercaseBytes = frozenset([item.encode("ascii") for item in asciiUppercase])
spacesAngleBrackets = spaceCharactersBytes | frozenset([b">", b"<"])


invalid_unicode_no_surrogate = "[\u0001-\u0008\u000B\u000E-\u001F\u007F-\u009F\uFDD0-\uFDEF\uFFFE\uFFFF\U0001FFFE\U0001FFFF\U0002FFFE\U0002FFFF\U0003FFFE\U0003FFFF\U0004FFFE\U0004FFFF\U0005FFFE\U0005FFFF\U0006FFFE\U0006FFFF\U0007FFFE\U0007FFFF\U0008FFFE\U0008FFFF\U0009FFFE\U0009FFFF\U000AFFFE\U000AFFFF\U000BFFFE\U000BFFFF\U000CFFFE\U000CFFFF\U000DFFFE\U000DFFFF\U000EFFFE\U000EFFFF\U000FFFFE\U000FFFFF\U0010FFFE\U0010FFFF]"  # noqa

if _utils.supports_lone_surrogates:
    # Use one extra step of indirection and create surrogates with
    # eval. Not using this indirection would introduce an illegal
    # unicode literal on platforms not supporting such lone
    # surrogates.
    assert invalid_unicode_no_surrogate[-1] == "]" and invalid_unicode_no_surrogate.count("]") == 1
    invalid_unicode_re = re.compile(invalid_unicode_no_surrogate[:-1] +
                                    eval('"\\uD800-\\uDFFF"') +  # pylint:disable=eval-used
                                    "]")
else:
    invalid_unicode_re = re.compile(invalid_unicode_no_surrogate)

non_bmp_invalid_codepoints = {0x1FFFE, 0x1FFFF, 0x2FFFE, 0x2FFFF, 0x3FFFE,
                              0x3FFFF, 0x4FFFE, 0x4FFFF, 0x5FFFE, 0x5FFFF,
                              0x6FFFE, 0x6FFFF, 0x7FFFE, 0x7FFFF, 0x8FFFE,
                              0x8FFFF, 0x9FFFE, 0x9FFFF, 0xAFFFE, 0xAFFFF,
                              0xBFFFE, 0xBFFFF, 0xCFFFE, 0xCFFFF, 0xDFFFE,
                              0xDFFFF, 0xEFFFE, 0xEFFFF, 0xFFFFE, 0xFFFFF,
                              0x10FFFE, 0x10FFFF}

ascii_punctuation_re = re.compile("[\u0009-\u000D\u0020-\u002F\u003A-\u0040\u005C\u005B-\u0060\u007B-\u007E]")

# Cache for charsUntil()
charsUntilRegEx = {}


class BufferedStream(object):
    """Buffering for streams that do not have buffering of their own

    The buffer is implemented as a list of chunks on the assumption that
    joining many strings will be slow since it is O(n**2)
    """

    def __init__(self, stream):
        self.stream = stream
        self.buffer = []
        self.position = [-1, 0]  # chunk number, offset

    def tell(self):
        pos = 0
        for chunk in self.buffer[:self.position[0]]:
            pos += len(chunk)
        pos += self.position[1]
        return pos

    def seek(self, pos):
        assert pos <= self._bufferedBytes()
        offset = pos
        i = 0
        while len(self.buffer[i]) < offset:
            offset -= len(self.buffer[i])
            i += 1
        self.position = [i, offset]

    def read(self, bytes):
        if not self.buffer:
            return self._readStream(bytes)
        elif (self.position[0] == len(self.buffer) and
              self.position[1] == len(self.buffer[-1])):
            return self._readStream(bytes)
        else:
            return self._readFromBuffer(bytes)

    def _bufferedBytes(self):
        return sum([len(item) for item in self.buffer])

    def _readStream(self, bytes):
        data = self.stream.read(bytes)
        self.buffer.append(data)
        self.position[0] += 1
        self.position[1] = len(data)
        return data

    def _readFromBuffer(self, bytes):
        remainingBytes = bytes
        rv = []
        bufferIndex = self.position[0]
        bufferOffset = self.position[1]
        while bufferIndex < len(self.buffer) and remainingBytes != 0:
            assert remainingBytes > 0
            bufferedData = self.buffer[bufferIndex]

            if remainingBytes <= len(bufferedData) - bufferOffset:
                bytesToRead = remainingBytes
                self.position = [bufferIndex, bufferOffset + bytesToRead]
            else:
                bytesToRead = len(bufferedData) - bufferOffset
                self.position = [bufferIndex, len(bufferedData)]
                bufferIndex += 1
            rv.append(bufferedData[bufferOffset:bufferOffset + bytesToRead])
            remainingBytes -= bytesToRead

            bufferOffset = 0

        if remainingBytes:
            rv.append(self._readStream(remainingBytes))

        return b"".join(rv)


def HTMLInputStream(source, **kwargs):
    # Work around Python bug #20007: read(0) closes the connection.
    # http://bugs.python.org/issue20007
    if (isinstance(source, http_client.HTTPResponse) or
        # Also check for addinfourl wrapping HTTPResponse
        (isinstance(source, urllib.response.addbase) and
         isinstance(source.fp, http_client.HTTPResponse))):
        isUnicode = False
    elif hasattr(source, "read"):
        isUnicode = isinstance(source.read(0), text_type)
    else:
        isUnicode = isinstance(source, text_type)

    if isUnicode:
        encodings = [x for x in kwargs if x.endswith("_encoding")]
        if encodings:
            raise TypeError("Cannot set an encoding with a unicode input, set %r" % encodings)

        return HTMLUnicodeInputStream(source, **kwargs)
    else:
        return HTMLBinaryInputStream(source, **kwargs)


class HTMLUnicodeInputStream(object):
    """Provides a unicode stream of characters to the HTMLTokenizer.

    This class takes care of character encoding and removing or replacing
    incorrect byte-sequences and also provides column and line tracking.

    """

    _defaultChunkSize = 10240

    def __init__(self, source):
        """Initialises the HTMLInputStream.

        HTMLInputStream(source, [encoding]) -> Normalized stream from source
        for use by html5lib.

        source can be either a file-object, local filename or a string.

        The optional encoding parameter must be a string that indicates
        the encoding.  If specified, that encoding will be used,
        regardless of any BOM or later declaration (such as in a meta
        element)

        """

        if not _utils.supports_lone_surrogates:
            # Such platforms will have already checked for such
            # surrogate errors, so no need to do this checking.
            self.reportCharacterErrors = None
        elif len("\U0010FFFF") == 1:
            self.reportCharacterErrors = self.characterErrorsUCS4
        else:
            self.reportCharacterErrors = self.characterErrorsUCS2

        # List of where new lines occur
        self.newLines = [0]

        self.charEncoding = (lookupEncoding("utf-8"), "certain")
        self.dataStream = self.openStream(source)

        self.reset()

    def reset(self):
        self.chunk = ""
        self.chunkSize = 0
        self.chunkOffset = 0
        self.errors = []

        # number of (complete) lines in previous chunks
        self.prevNumLines = 0
        # number of columns in the last line of the previous chunk
        self.prevNumCols = 0

        # Deal with CR LF and surrogates split over chunk boundaries
        self._bufferedCharacter = None

    def openStream(self, source):
        """Produces a file object from source.

        source can be either a file object, local filename or a string.

        """
        # Already a file object
        if hasattr(source, 'read'):
            stream = source
        else:
            stream = StringIO(source)

        return stream

    def _position(self, offset):
        chunk = self.chunk
        nLines = chunk.count('\n', 0, offset)
        positionLine = self.prevNumLines + nLines
        lastLinePos = chunk.rfind('\n', 0, offset)
        if lastLinePos == -1:
            positionColumn = self.prevNumCols + offset
        else:
            positionColumn = offset - (lastLinePos + 1)
        return (positionLine, positionColumn)

    def position(self):
        """Returns (line, col) of the current position in the stream."""
        line, col = self._position(self.chunkOffset)
        return (line + 1, col)

    def char(self):
        """ Read one character from the stream or queue if available. Return
            EOF when EOF is reached.
        """
        # Read a new chunk from the input stream if necessary
        if self.chunkOffset >= self.chunkSize:
            if not self.readChunk():
                return EOF

        chunkOffset = self.chunkOffset
        char = self.chunk[chunkOffset]
        self.chunkOffset = chunkOffset + 1

        return char

    def readChunk(self, chunkSize=None):
        if chunkSize is None:
            chunkSize = self._defaultChunkSize

        self.prevNumLines, self.prevNumCols = self._position(self.chunkSize)

        self.chunk = ""
        self.chunkSize = 0
        self.chunkOffset = 0

        data = self.dataStream.read(chunkSize)

        # Deal with CR LF and surrogates broken across chunks
        if self._bufferedCharacter:
            data = self._bufferedCharacter + data
            self._bufferedCharacter = None
        elif not data:
            # We have no more data, bye-bye stream
            return False

        if len(data) > 1:
            lastv = ord(data[-1])
            if lastv == 0x0D or 0xD800 <= lastv <= 0xDBFF:
                self._bufferedCharacter = data[-1]
                data = data[:-1]

        if self.reportCharacterErrors:
            self.reportCharacterErrors(data)

        # Replace invalid characters
        data = data.replace("\r\n", "\n")
        data = data.replace("\r", "\n")

        self.chunk = data
        self.chunkSize = len(data)

        return True

    def characterErrorsUCS4(self, data):
        for _ in range(len(invalid_unicode_re.findall(data))):
            self.errors.append("invalid-codepoint")

    def characterErrorsUCS2(self, data):
        # Someone picked the wrong compile option
        # You lose
        skip = False
        for match in invalid_unicode_re.finditer(data):
            if skip:
                continue
            codepoint = ord(match.group())
            pos = match.start()
            # Pretty sure there should be endianness issues here
            if _utils.isSurrogatePair(data[pos:pos + 2]):
                # We have a surrogate pair!
                char_val = _utils.surrogatePairToCodepoint(data[pos:pos + 2])
                if char_val in non_bmp_invalid_codepoints:
                    self.errors.append("invalid-codepoint")
                skip = True
            elif (codepoint >= 0xD800 and codepoint <= 0xDFFF and
                  pos == len(data) - 1):
                self.errors.append("invalid-codepoint")
            else:
                skip = False
                self.errors.append("invalid-codepoint")

    def charsUntil(self, characters, opposite=False):
        """ Returns a string of characters from the stream up to but not
        including any character in 'characters' or EOF. 'characters' must be
        a container that supports the 'in' method and iteration over its
        characters.
        """

        # Use a cache of regexps to find the required characters
        try:
            chars = charsUntilRegEx[(characters, opposite)]
        except KeyError:
            if __debug__:
                for c in characters:
                    assert(ord(c) < 128)
            regex = "".join(["\\x%02x" % ord(c) for c in characters])
            if not opposite:
                regex = "^%s" % regex
            chars = charsUntilRegEx[(characters, opposite)] = re.compile("[%s]+" % regex)

        rv = []

        while True:
            # Find the longest matching prefix
            m = chars.match(self.chunk, self.chunkOffset)
            if m is None:
                # If nothing matched, and it wasn't because we ran out of chunk,
                # then stop
                if self.chunkOffset != self.chunkSize:
                    break
            else:
                end = m.end()
                # If not the whole chunk matched, return everything
                # up to the part that didn't match
                if end != self.chunkSize:
                    rv.append(self.chunk[self.chunkOffset:end])
                    self.chunkOffset = end
                    break
            # If the whole remainder of the chunk matched,
            # use it all and read the next chunk
            rv.append(self.chunk[self.chunkOffset:])
            if not self.readChunk():
                # Reached EOF
                break

        r = "".join(rv)
        return r

    def unget(self, char):
        # Only one character is allowed to be ungotten at once - it must
        # be consumed again before any further call to unget
        if char is not EOF:
            if self.chunkOffset == 0:
                # unget is called quite rarely, so it's a good idea to do
                # more work here if it saves a bit of work in the frequently
                # called char and charsUntil.
                # So, just prepend the ungotten character onto the current
                # chunk:
                self.chunk = char + self.chunk
                self.chunkSize += 1
            else:
                self.chunkOffset -= 1
                assert self.chunk[self.chunkOffset] == char


class HTMLBinaryInputStream(HTMLUnicodeInputStream):
    """Provides a unicode stream of characters to the HTMLTokenizer.

    This class takes care of character encoding and removing or replacing
    incorrect byte-sequences and also provides column and line tracking.

    """

    def __init__(self, source, override_encoding=None, transport_encoding=None,
                 same_origin_parent_encoding=None, likely_encoding=None,
                 default_encoding="windows-1252", useChardet=True):
        """Initialises the HTMLInputStream.

        HTMLInputStream(source, [encoding]) -> Normalized stream from source
        for use by html5lib.

        source can be either a file-object, local filename or a string.

        The optional encoding parameter must be a string that indicates
        the encoding.  If specified, that encoding will be used,
        regardless of any BOM or later declaration (such as in a meta
        element)

        """
        # Raw Stream - for unicode objects this will encode to utf-8 and set
        #              self.charEncoding as appropriate
        self.rawStream = self.openStream(source)

        HTMLUnicodeInputStream.__init__(self, self.rawStream)

        # Encoding Information
        # Number of bytes to use when looking for a meta element with
        # encoding information
        self.numBytesMeta = 1024
        # Number of bytes to use when using detecting encoding using chardet
        self.numBytesChardet = 100
        # Things from args
        self.override_encoding = override_encoding
        self.transport_encoding = transport_encoding
        self.same_origin_parent_encoding = same_origin_parent_encoding
        self.likely_encoding = likely_encoding
        self.default_encoding = default_encoding

        # Determine encoding
        self.charEncoding = self.determineEncoding(useChardet)
        assert self.charEncoding[0] is not None

        # Call superclass
        self.reset()

    def reset(self):
        self.dataStream = self.charEncoding[0].codec_info.streamreader(self.rawStream, 'replace')
        HTMLUnicodeInputStream.reset(self)

    def openStream(self, source):
        """Produces a file object from source.

        source can be either a file object, local filename or a string.

        """
        # Already a file object
        if hasattr(source, 'read'):
            stream = source
        else:
            stream = BytesIO(source)

        try:
            stream.seek(stream.tell())
        except Exception:
            stream = BufferedStream(stream)

        return stream

    def determineEncoding(self, chardet=True):
        # BOMs take precedence over everything
        # This will also read past the BOM if present
        charEncoding = self.detectBOM(), "certain"
        if charEncoding[0] is not None:
            return charEncoding

        # If we've been overridden, we've been overridden
        charEncoding = lookupEncoding(self.override_encoding), "certain"
        if charEncoding[0] is not None:
            return charEncoding

        # Now check the transport layer
        charEncoding = lookupEncoding(self.transport_encoding), "certain"
        if charEncoding[0] is not None:
            return charEncoding

        # Look for meta elements with encoding information
        charEncoding = self.detectEncodingMeta(), "tentative"
        if charEncoding[0] is not None:
            return charEncoding

        # Parent document encoding
        charEncoding = lookupEncoding(self.same_origin_parent_encoding), "tentative"
        if charEncoding[0] is not None and not charEncoding[0].name.startswith("utf-16"):
            return charEncoding

        # "likely" encoding
        charEncoding = lookupEncoding(self.likely_encoding), "tentative"
        if charEncoding[0] is not None:
            return charEncoding

        # Guess with chardet, if available
        if chardet:
            try:
                from pip._vendor.chardet.universaldetector import UniversalDetector
            except ImportError:
                pass
            else:
                buffers = []
                detector = UniversalDetector()
                while not detector.done:
                    buffer = self.rawStream.read(self.numBytesChardet)
                    assert isinstance(buffer, bytes)
                    if not buffer:
                        break
                    buffers.append(buffer)
                    detector.feed(buffer)
                detector.close()
                encoding = lookupEncoding(detector.result['encoding'])
                self.rawStream.seek(0)
                if encoding is not None:
                    return encoding, "tentative"

        # Try the default encoding
        charEncoding = lookupEncoding(self.default_encoding), "tentative"
        if charEncoding[0] is not None:
            return charEncoding

        # Fallback to html5lib's default if even that hasn't worked
        return lookupEncoding("windows-1252"), "tentative"

    def changeEncoding(self, newEncoding):
        assert self.charEncoding[1] != "certain"
        newEncoding = lookupEncoding(newEncoding)
        if newEncoding is None:
            return
        if newEncoding.name in ("utf-16be", "utf-16le"):
            newEncoding = lookupEncoding("utf-8")
            assert newEncoding is not None
        elif newEncoding == self.charEncoding[0]:
            self.charEncoding = (self.charEncoding[0], "certain")
        else:
            self.rawStream.seek(0)
            self.charEncoding = (newEncoding, "certain")
            self.reset()
            raise _ReparseException("Encoding changed from %s to %s" % (self.charEncoding[0], newEncoding))

    def detectBOM(self):
        """Attempts to detect at BOM at the start of the stream. If
        an encoding can be determined from the BOM return the name of the
        encoding otherwise return None"""
        bomDict = {
            codecs.BOM_UTF8: 'utf-8',
            codecs.BOM_UTF16_LE: 'utf-16le', codecs.BOM_UTF16_BE: 'utf-16be',
            codecs.BOM_UTF32_LE: 'utf-32le', codecs.BOM_UTF32_BE: 'utf-32be'
        }

        # Go to beginning of file and read in 4 bytes
        string = self.rawStream.read(4)
        assert isinstance(string, bytes)

        # Try detecting the BOM using bytes from the string
        encoding = bomDict.get(string[:3])         # UTF-8
        seek = 3
        if not encoding:
            # Need to detect UTF-32 before UTF-16
            encoding = bomDict.get(string)         # UTF-32
            seek = 4
            if not encoding:
                encoding = bomDict.get(string[:2])  # UTF-16
                seek = 2

        # Set the read position past the BOM if one was found, otherwise
        # set it to the start of the stream
        if encoding:
            self.rawStream.seek(seek)
            return lookupEncoding(encoding)
        else:
            self.rawStream.seek(0)
            return None

    def detectEncodingMeta(self):
        """Report the encoding declared by the meta element
        """
        buffer = self.rawStream.read(self.numBytesMeta)
        assert isinstance(buffer, bytes)
        parser = EncodingParser(buffer)
        self.rawStream.seek(0)
        encoding = parser.getEncoding()

        if encoding is not None and encoding.name in ("utf-16be", "utf-16le"):
            encoding = lookupEncoding("utf-8")

        return encoding


class EncodingBytes(bytes):
    """String-like object with an associated position and various extra methods
    If the position is ever greater than the string length then an exception is
    raised"""
    def __new__(self, value):
        assert isinstance(value, bytes)
        return bytes.__new__(self, value.lower())

    def __init__(self, value):
        # pylint:disable=unused-argument
        self._position = -1

    def __iter__(self):
        return self

    def __next__(self):
        p = self._position = self._position + 1
        if p >= len(self):
            raise StopIteration
        elif p < 0:
            raise TypeError
        return self[p:p + 1]

    def next(self):
        # Py2 compat
        return self.__next__()

    def previous(self):
        p = self._position
        if p >= len(self):
            raise StopIteration
        elif p < 0:
            raise TypeError
        self._position = p = p - 1
        return self[p:p + 1]

    def setPosition(self, position):
        if self._position >= len(self):
            raise StopIteration
        self._position = position

    def getPosition(self):
        if self._position >= len(self):
            raise StopIteration
        if self._position >= 0:
            return self._position
        else:
            return None

    position = property(getPosition, setPosition)

    def getCurrentByte(self):
        return self[self.position:self.position + 1]

    currentByte = property(getCurrentByte)

    def skip(self, chars=spaceCharactersBytes):
        """Skip past a list of characters"""
        p = self.position               # use property for the error-checking
        while p < len(self):
            c = self[p:p + 1]
            if c not in chars:
                self._position = p
                return c
            p += 1
        self._position = p
        return None

    def skipUntil(self, chars):
        p = self.position
        while p < len(self):
            c = self[p:p + 1]
            if c in chars:
                self._position = p
                return c
            p += 1
        self._position = p
        return None

    def matchBytes(self, bytes):
        """Look for a sequence of bytes at the start of a string. If the bytes
        are found return True and advance the position to the byte after the
        match. Otherwise return False and leave the position alone"""
        rv = self.startswith(bytes, self.position)
        if rv:
            self.position += len(bytes)
        return rv

    def jumpTo(self, bytes):
        """Look for the next sequence of bytes matching a given sequence. If
        a match is found advance the position to the last byte of the match"""
        try:
            self._position = self.index(bytes, self.position) + len(bytes) - 1
        except ValueError:
            raise StopIteration
        return True


class EncodingParser(object):
    """Mini parser for detecting character encoding from meta elements"""

    def __init__(self, data):
        """string - the data to work on for encoding detection"""
        self.data = EncodingBytes(data)
        self.encoding = None

    def getEncoding(self):
        if b"<meta" not in self.data:
            return None

        methodDispatch = (
            (b"<!--", self.handleComment),
            (b"<meta", self.handleMeta),
            (b"</", self.handlePossibleEndTag),
            (b"<!", self.handleOther),
            (b"<?", self.handleOther),
            (b"<", self.handlePossibleStartTag))
        for _ in self.data:
            keepParsing = True
            try:
                self.data.jumpTo(b"<")
            except StopIteration:
                break
            for key, method in methodDispatch:
                if self.data.matchBytes(key):
                    try:
                        keepParsing = method()
                        break
                    except StopIteration:
                        keepParsing = False
                        break
            if not keepParsing:
                break

        return self.encoding

    def handleComment(self):
        """Skip over comments"""
        return self.data.jumpTo(b"-->")

    def handleMeta(self):
        if self.data.currentByte not in spaceCharactersBytes:
            # if we have <meta not followed by a space so just keep going
            return True
        # We have a valid meta element we want to search for attributes
        hasPragma = False
        pendingEncoding = None
        while True:
            # Try to find the next attribute after the current position
            attr = self.getAttribute()
            if attr is None:
                return True
            else:
                if attr[0] == b"http-equiv":
                    hasPragma = attr[1] == b"content-type"
                    if hasPragma and pendingEncoding is not None:
                        self.encoding = pendingEncoding
                        return False
                elif attr[0] == b"charset":
                    tentativeEncoding = attr[1]
                    codec = lookupEncoding(tentativeEncoding)
                    if codec is not None:
                        self.encoding = codec
                        return False
                elif attr[0] == b"content":
                    contentParser = ContentAttrParser(EncodingBytes(attr[1]))
                    tentativeEncoding = contentParser.parse()
                    if tentativeEncoding is not None:
                        codec = lookupEncoding(tentativeEncoding)
                        if codec is not None:
                            if hasPragma:
                                self.encoding = codec
                                return False
                            else:
                                pendingEncoding = codec

    def handlePossibleStartTag(self):
        return self.handlePossibleTag(False)

    def handlePossibleEndTag(self):
        next(self.data)
        return self.handlePossibleTag(True)

    def handlePossibleTag(self, endTag):
        data = self.data
        if data.currentByte not in asciiLettersBytes:
            # If the next byte is not an ascii letter either ignore this
            # fragment (possible start tag case) or treat it according to
            # handleOther
            if endTag:
                data.previous()
                self.handleOther()
            return True

        c = data.skipUntil(spacesAngleBrackets)
        if c == b"<":
            # return to the first step in the overall "two step" algorithm
            # reprocessing the < byte
            data.previous()
        else:
            # Read all attributes
            attr = self.getAttribute()
            while attr is not None:
                attr = self.getAttribute()
        return True

    def handleOther(self):
        return self.data.jumpTo(b">")

    def getAttribute(self):
        """Return a name,value pair for the next attribute in the stream,
        if one is found, or None"""
        data = self.data
        # Step 1 (skip chars)
        c = data.skip(spaceCharactersBytes | frozenset([b"/"]))
        assert c is None or len(c) == 1
        # Step 2
        if c in (b">", None):
            return None
        # Step 3
        attrName = []
        attrValue = []
        # Step 4 attribute name
        while True:
            if c == b"=" and attrName:
                break
            elif c in spaceCharactersBytes:
                # Step 6!
                c = data.skip()
                break
            elif c in (b"/", b">"):
                return b"".join(attrName), b""
            elif c in asciiUppercaseBytes:
                attrName.append(c.lower())
            elif c is None:
                return None
            else:
                attrName.append(c)
            # Step 5
            c = next(data)
        # Step 7
        if c != b"=":
            data.previous()
            return b"".join(attrName), b""
        # Step 8
        next(data)
        # Step 9
        c = data.skip()
        # Step 10
        if c in (b"'", b'"'):
            # 10.1
            quoteChar = c
            while True:
                # 10.2
                c = next(data)
                # 10.3
                if c == quoteChar:
                    next(data)
                    return b"".join(attrName), b"".join(attrValue)
                # 10.4
                elif c in asciiUppercaseBytes:
                    attrValue.append(c.lower())
                # 10.5
                else:
                    attrValue.append(c)
        elif c == b">":
            return b"".join(attrName), b""
        elif c in asciiUppercaseBytes:
            attrValue.append(c.lower())
        elif c is None:
            return None
        else:
            attrValue.append(c)
        # Step 11
        while True:
            c = next(data)
            if c in spacesAngleBrackets:
                return b"".join(attrName), b"".join(attrValue)
            elif c in asciiUppercaseBytes:
                attrValue.append(c.lower())
            elif c is None:
                return None
            else:
                attrValue.append(c)


class ContentAttrParser(object):
    def __init__(self, data):
        assert isinstance(data, bytes)
        self.data = data

    def parse(self):
        try:
            # Check if the attr name is charset
            # otherwise return
            self.data.jumpTo(b"charset")
            self.data.position += 1
            self.data.skip()
            if not self.data.currentByte == b"=":
                # If there is no = sign keep looking for attrs
                return None
            self.data.position += 1
            self.data.skip()
            # Look for an encoding between matching quote marks
            if self.data.currentByte in (b'"', b"'"):
                quoteMark = self.data.currentByte
                self.data.position += 1
                oldPosition = self.data.position
                if self.data.jumpTo(quoteMark):
                    return self.data[oldPosition:self.data.position]
                else:
                    return None
            else:
                # Unquoted value
                oldPosition = self.data.position
                try:
                    self.data.skipUntil(spaceCharactersBytes)
                    return self.data[oldPosition:self.data.position]
                except StopIteration:
                    # Return the whole remaining value
                    return self.data[oldPosition:]
        except StopIteration:
            return None


def lookupEncoding(encoding):
    """Return the python codec name corresponding to an encoding or None if the
    string doesn't correspond to a valid encoding."""
    if isinstance(encoding, bytes):
        try:
            encoding = encoding.decode("ascii")
        except UnicodeDecodeError:
            return None

    if encoding is not None:
        try:
            return webencodings.lookup(encoding)
        except AttributeError:
            return None
    else:
        return None
