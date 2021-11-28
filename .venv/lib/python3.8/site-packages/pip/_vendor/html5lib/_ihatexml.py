from __future__ import absolute_import, division, unicode_literals

import re
import warnings

from .constants import DataLossWarning

baseChar = """
[#x0041-#x005A] | [#x0061-#x007A] | [#x00C0-#x00D6] | [#x00D8-#x00F6] |
[#x00F8-#x00FF] | [#x0100-#x0131] | [#x0134-#x013E] | [#x0141-#x0148] |
[#x014A-#x017E] | [#x0180-#x01C3] | [#x01CD-#x01F0] | [#x01F4-#x01F5] |
[#x01FA-#x0217] | [#x0250-#x02A8] | [#x02BB-#x02C1] | #x0386 |
[#x0388-#x038A] | #x038C | [#x038E-#x03A1] | [#x03A3-#x03CE] |
[#x03D0-#x03D6] | #x03DA | #x03DC | #x03DE | #x03E0 | [#x03E2-#x03F3] |
[#x0401-#x040C] | [#x040E-#x044F] | [#x0451-#x045C] | [#x045E-#x0481] |
[#x0490-#x04C4] | [#x04C7-#x04C8] | [#x04CB-#x04CC] | [#x04D0-#x04EB] |
[#x04EE-#x04F5] | [#x04F8-#x04F9] | [#x0531-#x0556] | #x0559 |
[#x0561-#x0586] | [#x05D0-#x05EA] | [#x05F0-#x05F2] | [#x0621-#x063A] |
[#x0641-#x064A] | [#x0671-#x06B7] | [#x06BA-#x06BE] | [#x06C0-#x06CE] |
[#x06D0-#x06D3] | #x06D5 | [#x06E5-#x06E6] | [#x0905-#x0939] | #x093D |
[#x0958-#x0961] | [#x0985-#x098C] | [#x098F-#x0990] | [#x0993-#x09A8] |
[#x09AA-#x09B0] | #x09B2 | [#x09B6-#x09B9] | [#x09DC-#x09DD] |
[#x09DF-#x09E1] | [#x09F0-#x09F1] | [#x0A05-#x0A0A] | [#x0A0F-#x0A10] |
[#x0A13-#x0A28] | [#x0A2A-#x0A30] | [#x0A32-#x0A33] | [#x0A35-#x0A36] |
[#x0A38-#x0A39] | [#x0A59-#x0A5C] | #x0A5E | [#x0A72-#x0A74] |
[#x0A85-#x0A8B] | #x0A8D | [#x0A8F-#x0A91] | [#x0A93-#x0AA8] |
[#x0AAA-#x0AB0] | [#x0AB2-#x0AB3] | [#x0AB5-#x0AB9] | #x0ABD | #x0AE0 |
[#x0B05-#x0B0C] | [#x0B0F-#x0B10] | [#x0B13-#x0B28] | [#x0B2A-#x0B30] |
[#x0B32-#x0B33] | [#x0B36-#x0B39] | #x0B3D | [#x0B5C-#x0B5D] |
[#x0B5F-#x0B61] | [#x0B85-#x0B8A] | [#x0B8E-#x0B90] | [#x0B92-#x0B95] |
[#x0B99-#x0B9A] | #x0B9C | [#x0B9E-#x0B9F] | [#x0BA3-#x0BA4] |
[#x0BA8-#x0BAA] | [#x0BAE-#x0BB5] | [#x0BB7-#x0BB9] | [#x0C05-#x0C0C] |
[#x0C0E-#x0C10] | [#x0C12-#x0C28] | [#x0C2A-#x0C33] | [#x0C35-#x0C39] |
[#x0C60-#x0C61] | [#x0C85-#x0C8C] | [#x0C8E-#x0C90] | [#x0C92-#x0CA8] |
[#x0CAA-#x0CB3] | [#x0CB5-#x0CB9] | #x0CDE | [#x0CE0-#x0CE1] |
[#x0D05-#x0D0C] | [#x0D0E-#x0D10] | [#x0D12-#x0D28] | [#x0D2A-#x0D39] |
[#x0D60-#x0D61] | [#x0E01-#x0E2E] | #x0E30 | [#x0E32-#x0E33] |
[#x0E40-#x0E45] | [#x0E81-#x0E82] | #x0E84 | [#x0E87-#x0E88] | #x0E8A |
#x0E8D | [#x0E94-#x0E97] | [#x0E99-#x0E9F] | [#x0EA1-#x0EA3] | #x0EA5 |
#x0EA7 | [#x0EAA-#x0EAB] | [#x0EAD-#x0EAE] | #x0EB0 | [#x0EB2-#x0EB3] |
#x0EBD | [#x0EC0-#x0EC4] | [#x0F40-#x0F47] | [#x0F49-#x0F69] |
[#x10A0-#x10C5] | [#x10D0-#x10F6] | #x1100 | [#x1102-#x1103] |
[#x1105-#x1107] | #x1109 | [#x110B-#x110C] | [#x110E-#x1112] | #x113C |
#x113E | #x1140 | #x114C | #x114E | #x1150 | [#x1154-#x1155] | #x1159 |
[#x115F-#x1161] | #x1163 | #x1165 | #x1167 | #x1169 | [#x116D-#x116E] |
[#x1172-#x1173] | #x1175 | #x119E | #x11A8 | #x11AB | [#x11AE-#x11AF] |
[#x11B7-#x11B8] | #x11BA | [#x11BC-#x11C2] | #x11EB | #x11F0 | #x11F9 |
[#x1E00-#x1E9B] | [#x1EA0-#x1EF9] | [#x1F00-#x1F15] | [#x1F18-#x1F1D] |
[#x1F20-#x1F45] | [#x1F48-#x1F4D] | [#x1F50-#x1F57] | #x1F59 | #x1F5B |
#x1F5D | [#x1F5F-#x1F7D] | [#x1F80-#x1FB4] | [#x1FB6-#x1FBC] | #x1FBE |
[#x1FC2-#x1FC4] | [#x1FC6-#x1FCC] | [#x1FD0-#x1FD3] | [#x1FD6-#x1FDB] |
[#x1FE0-#x1FEC] | [#x1FF2-#x1FF4] | [#x1FF6-#x1FFC] | #x2126 |
[#x212A-#x212B] | #x212E | [#x2180-#x2182] | [#x3041-#x3094] |
[#x30A1-#x30FA] | [#x3105-#x312C] | [#xAC00-#xD7A3]"""

ideographic = """[#x4E00-#x9FA5] | #x3007 | [#x3021-#x3029]"""

combiningCharacter = """
[#x0300-#x0345] | [#x0360-#x0361] | [#x0483-#x0486] | [#x0591-#x05A1] |
[#x05A3-#x05B9] | [#x05BB-#x05BD] | #x05BF | [#x05C1-#x05C2] | #x05C4 |
[#x064B-#x0652] | #x0670 | [#x06D6-#x06DC] | [#x06DD-#x06DF] |
[#x06E0-#x06E4] | [#x06E7-#x06E8] | [#x06EA-#x06ED] | [#x0901-#x0903] |
#x093C | [#x093E-#x094C] | #x094D | [#x0951-#x0954] | [#x0962-#x0963] |
[#x0981-#x0983] | #x09BC | #x09BE | #x09BF | [#x09C0-#x09C4] |
[#x09C7-#x09C8] | [#x09CB-#x09CD] | #x09D7 | [#x09E2-#x09E3] | #x0A02 |
#x0A3C | #x0A3E | #x0A3F | [#x0A40-#x0A42] | [#x0A47-#x0A48] |
[#x0A4B-#x0A4D] | [#x0A70-#x0A71] | [#x0A81-#x0A83] | #x0ABC |
[#x0ABE-#x0AC5] | [#x0AC7-#x0AC9] | [#x0ACB-#x0ACD] | [#x0B01-#x0B03] |
#x0B3C | [#x0B3E-#x0B43] | [#x0B47-#x0B48] | [#x0B4B-#x0B4D] |
[#x0B56-#x0B57] | [#x0B82-#x0B83] | [#x0BBE-#x0BC2] | [#x0BC6-#x0BC8] |
[#x0BCA-#x0BCD] | #x0BD7 | [#x0C01-#x0C03] | [#x0C3E-#x0C44] |
[#x0C46-#x0C48] | [#x0C4A-#x0C4D] | [#x0C55-#x0C56] | [#x0C82-#x0C83] |
[#x0CBE-#x0CC4] | [#x0CC6-#x0CC8] | [#x0CCA-#x0CCD] | [#x0CD5-#x0CD6] |
[#x0D02-#x0D03] | [#x0D3E-#x0D43] | [#x0D46-#x0D48] | [#x0D4A-#x0D4D] |
#x0D57 | #x0E31 | [#x0E34-#x0E3A] | [#x0E47-#x0E4E] | #x0EB1 |
[#x0EB4-#x0EB9] | [#x0EBB-#x0EBC] | [#x0EC8-#x0ECD] | [#x0F18-#x0F19] |
#x0F35 | #x0F37 | #x0F39 | #x0F3E | #x0F3F | [#x0F71-#x0F84] |
[#x0F86-#x0F8B] | [#x0F90-#x0F95] | #x0F97 | [#x0F99-#x0FAD] |
[#x0FB1-#x0FB7] | #x0FB9 | [#x20D0-#x20DC] | #x20E1 | [#x302A-#x302F] |
#x3099 | #x309A"""

digit = """
[#x0030-#x0039] | [#x0660-#x0669] | [#x06F0-#x06F9] | [#x0966-#x096F] |
[#x09E6-#x09EF] | [#x0A66-#x0A6F] | [#x0AE6-#x0AEF] | [#x0B66-#x0B6F] |
[#x0BE7-#x0BEF] | [#x0C66-#x0C6F] | [#x0CE6-#x0CEF] | [#x0D66-#x0D6F] |
[#x0E50-#x0E59] | [#x0ED0-#x0ED9] | [#x0F20-#x0F29]"""

extender = """
#x00B7 | #x02D0 | #x02D1 | #x0387 | #x0640 | #x0E46 | #x0EC6 | #x3005 |
#[#x3031-#x3035] | [#x309D-#x309E] | [#x30FC-#x30FE]"""

letter = " | ".join([baseChar, ideographic])

# Without the
name = " | ".join([letter, digit, ".", "-", "_", combiningCharacter,
                   extender])
nameFirst = " | ".join([letter, "_"])

reChar = re.compile(r"#x([\d|A-F]{4,4})")
reCharRange = re.compile(r"\[#x([\d|A-F]{4,4})-#x([\d|A-F]{4,4})\]")


def charStringToList(chars):
    charRanges = [item.strip() for item in chars.split(" | ")]
    rv = []
    for item in charRanges:
        foundMatch = False
        for regexp in (reChar, reCharRange):
            match = regexp.match(item)
            if match is not None:
                rv.append([hexToInt(item) for item in match.groups()])
                if len(rv[-1]) == 1:
                    rv[-1] = rv[-1] * 2
                foundMatch = True
                break
        if not foundMatch:
            assert len(item) == 1

            rv.append([ord(item)] * 2)
    rv = normaliseCharList(rv)
    return rv


def normaliseCharList(charList):
    charList = sorted(charList)
    for item in charList:
        assert item[1] >= item[0]
    rv = []
    i = 0
    while i < len(charList):
        j = 1
        rv.append(charList[i])
        while i + j < len(charList) and charList[i + j][0] <= rv[-1][1] + 1:
            rv[-1][1] = charList[i + j][1]
            j += 1
        i += j
    return rv


# We don't really support characters above the BMP :(
max_unicode = int("FFFF", 16)


def missingRanges(charList):
    rv = []
    if charList[0] != 0:
        rv.append([0, charList[0][0] - 1])
    for i, item in enumerate(charList[:-1]):
        rv.append([item[1] + 1, charList[i + 1][0] - 1])
    if charList[-1][1] != max_unicode:
        rv.append([charList[-1][1] + 1, max_unicode])
    return rv


def listToRegexpStr(charList):
    rv = []
    for item in charList:
        if item[0] == item[1]:
            rv.append(escapeRegexp(chr(item[0])))
        else:
            rv.append(escapeRegexp(chr(item[0])) + "-" +
                      escapeRegexp(chr(item[1])))
    return "[%s]" % "".join(rv)


def hexToInt(hex_str):
    return int(hex_str, 16)


def escapeRegexp(string):
    specialCharacters = (".", "^", "$", "*", "+", "?", "{", "}",
                         "[", "]", "|", "(", ")", "-")
    for char in specialCharacters:
        string = string.replace(char, "\\" + char)

    return string

# output from the above
nonXmlNameBMPRegexp = re.compile('[\x00-,/:-@\\[-\\^`\\{-\xb6\xb8-\xbf\xd7\xf7\u0132-\u0133\u013f-\u0140\u0149\u017f\u01c4-\u01cc\u01f1-\u01f3\u01f6-\u01f9\u0218-\u024f\u02a9-\u02ba\u02c2-\u02cf\u02d2-\u02ff\u0346-\u035f\u0362-\u0385\u038b\u038d\u03a2\u03cf\u03d7-\u03d9\u03db\u03dd\u03df\u03e1\u03f4-\u0400\u040d\u0450\u045d\u0482\u0487-\u048f\u04c5-\u04c6\u04c9-\u04ca\u04cd-\u04cf\u04ec-\u04ed\u04f6-\u04f7\u04fa-\u0530\u0557-\u0558\u055a-\u0560\u0587-\u0590\u05a2\u05ba\u05be\u05c0\u05c3\u05c5-\u05cf\u05eb-\u05ef\u05f3-\u0620\u063b-\u063f\u0653-\u065f\u066a-\u066f\u06b8-\u06b9\u06bf\u06cf\u06d4\u06e9\u06ee-\u06ef\u06fa-\u0900\u0904\u093a-\u093b\u094e-\u0950\u0955-\u0957\u0964-\u0965\u0970-\u0980\u0984\u098d-\u098e\u0991-\u0992\u09a9\u09b1\u09b3-\u09b5\u09ba-\u09bb\u09bd\u09c5-\u09c6\u09c9-\u09ca\u09ce-\u09d6\u09d8-\u09db\u09de\u09e4-\u09e5\u09f2-\u0a01\u0a03-\u0a04\u0a0b-\u0a0e\u0a11-\u0a12\u0a29\u0a31\u0a34\u0a37\u0a3a-\u0a3b\u0a3d\u0a43-\u0a46\u0a49-\u0a4a\u0a4e-\u0a58\u0a5d\u0a5f-\u0a65\u0a75-\u0a80\u0a84\u0a8c\u0a8e\u0a92\u0aa9\u0ab1\u0ab4\u0aba-\u0abb\u0ac6\u0aca\u0ace-\u0adf\u0ae1-\u0ae5\u0af0-\u0b00\u0b04\u0b0d-\u0b0e\u0b11-\u0b12\u0b29\u0b31\u0b34-\u0b35\u0b3a-\u0b3b\u0b44-\u0b46\u0b49-\u0b4a\u0b4e-\u0b55\u0b58-\u0b5b\u0b5e\u0b62-\u0b65\u0b70-\u0b81\u0b84\u0b8b-\u0b8d\u0b91\u0b96-\u0b98\u0b9b\u0b9d\u0ba0-\u0ba2\u0ba5-\u0ba7\u0bab-\u0bad\u0bb6\u0bba-\u0bbd\u0bc3-\u0bc5\u0bc9\u0bce-\u0bd6\u0bd8-\u0be6\u0bf0-\u0c00\u0c04\u0c0d\u0c11\u0c29\u0c34\u0c3a-\u0c3d\u0c45\u0c49\u0c4e-\u0c54\u0c57-\u0c5f\u0c62-\u0c65\u0c70-\u0c81\u0c84\u0c8d\u0c91\u0ca9\u0cb4\u0cba-\u0cbd\u0cc5\u0cc9\u0cce-\u0cd4\u0cd7-\u0cdd\u0cdf\u0ce2-\u0ce5\u0cf0-\u0d01\u0d04\u0d0d\u0d11\u0d29\u0d3a-\u0d3d\u0d44-\u0d45\u0d49\u0d4e-\u0d56\u0d58-\u0d5f\u0d62-\u0d65\u0d70-\u0e00\u0e2f\u0e3b-\u0e3f\u0e4f\u0e5a-\u0e80\u0e83\u0e85-\u0e86\u0e89\u0e8b-\u0e8c\u0e8e-\u0e93\u0e98\u0ea0\u0ea4\u0ea6\u0ea8-\u0ea9\u0eac\u0eaf\u0eba\u0ebe-\u0ebf\u0ec5\u0ec7\u0ece-\u0ecf\u0eda-\u0f17\u0f1a-\u0f1f\u0f2a-\u0f34\u0f36\u0f38\u0f3a-\u0f3d\u0f48\u0f6a-\u0f70\u0f85\u0f8c-\u0f8f\u0f96\u0f98\u0fae-\u0fb0\u0fb8\u0fba-\u109f\u10c6-\u10cf\u10f7-\u10ff\u1101\u1104\u1108\u110a\u110d\u1113-\u113b\u113d\u113f\u1141-\u114b\u114d\u114f\u1151-\u1153\u1156-\u1158\u115a-\u115e\u1162\u1164\u1166\u1168\u116a-\u116c\u116f-\u1171\u1174\u1176-\u119d\u119f-\u11a7\u11a9-\u11aa\u11ac-\u11ad\u11b0-\u11b6\u11b9\u11bb\u11c3-\u11ea\u11ec-\u11ef\u11f1-\u11f8\u11fa-\u1dff\u1e9c-\u1e9f\u1efa-\u1eff\u1f16-\u1f17\u1f1e-\u1f1f\u1f46-\u1f47\u1f4e-\u1f4f\u1f58\u1f5a\u1f5c\u1f5e\u1f7e-\u1f7f\u1fb5\u1fbd\u1fbf-\u1fc1\u1fc5\u1fcd-\u1fcf\u1fd4-\u1fd5\u1fdc-\u1fdf\u1fed-\u1ff1\u1ff5\u1ffd-\u20cf\u20dd-\u20e0\u20e2-\u2125\u2127-\u2129\u212c-\u212d\u212f-\u217f\u2183-\u3004\u3006\u3008-\u3020\u3030\u3036-\u3040\u3095-\u3098\u309b-\u309c\u309f-\u30a0\u30fb\u30ff-\u3104\u312d-\u4dff\u9fa6-\uabff\ud7a4-\uffff]')  # noqa

nonXmlNameFirstBMPRegexp = re.compile('[\x00-@\\[-\\^`\\{-\xbf\xd7\xf7\u0132-\u0133\u013f-\u0140\u0149\u017f\u01c4-\u01cc\u01f1-\u01f3\u01f6-\u01f9\u0218-\u024f\u02a9-\u02ba\u02c2-\u0385\u0387\u038b\u038d\u03a2\u03cf\u03d7-\u03d9\u03db\u03dd\u03df\u03e1\u03f4-\u0400\u040d\u0450\u045d\u0482-\u048f\u04c5-\u04c6\u04c9-\u04ca\u04cd-\u04cf\u04ec-\u04ed\u04f6-\u04f7\u04fa-\u0530\u0557-\u0558\u055a-\u0560\u0587-\u05cf\u05eb-\u05ef\u05f3-\u0620\u063b-\u0640\u064b-\u0670\u06b8-\u06b9\u06bf\u06cf\u06d4\u06d6-\u06e4\u06e7-\u0904\u093a-\u093c\u093e-\u0957\u0962-\u0984\u098d-\u098e\u0991-\u0992\u09a9\u09b1\u09b3-\u09b5\u09ba-\u09db\u09de\u09e2-\u09ef\u09f2-\u0a04\u0a0b-\u0a0e\u0a11-\u0a12\u0a29\u0a31\u0a34\u0a37\u0a3a-\u0a58\u0a5d\u0a5f-\u0a71\u0a75-\u0a84\u0a8c\u0a8e\u0a92\u0aa9\u0ab1\u0ab4\u0aba-\u0abc\u0abe-\u0adf\u0ae1-\u0b04\u0b0d-\u0b0e\u0b11-\u0b12\u0b29\u0b31\u0b34-\u0b35\u0b3a-\u0b3c\u0b3e-\u0b5b\u0b5e\u0b62-\u0b84\u0b8b-\u0b8d\u0b91\u0b96-\u0b98\u0b9b\u0b9d\u0ba0-\u0ba2\u0ba5-\u0ba7\u0bab-\u0bad\u0bb6\u0bba-\u0c04\u0c0d\u0c11\u0c29\u0c34\u0c3a-\u0c5f\u0c62-\u0c84\u0c8d\u0c91\u0ca9\u0cb4\u0cba-\u0cdd\u0cdf\u0ce2-\u0d04\u0d0d\u0d11\u0d29\u0d3a-\u0d5f\u0d62-\u0e00\u0e2f\u0e31\u0e34-\u0e3f\u0e46-\u0e80\u0e83\u0e85-\u0e86\u0e89\u0e8b-\u0e8c\u0e8e-\u0e93\u0e98\u0ea0\u0ea4\u0ea6\u0ea8-\u0ea9\u0eac\u0eaf\u0eb1\u0eb4-\u0ebc\u0ebe-\u0ebf\u0ec5-\u0f3f\u0f48\u0f6a-\u109f\u10c6-\u10cf\u10f7-\u10ff\u1101\u1104\u1108\u110a\u110d\u1113-\u113b\u113d\u113f\u1141-\u114b\u114d\u114f\u1151-\u1153\u1156-\u1158\u115a-\u115e\u1162\u1164\u1166\u1168\u116a-\u116c\u116f-\u1171\u1174\u1176-\u119d\u119f-\u11a7\u11a9-\u11aa\u11ac-\u11ad\u11b0-\u11b6\u11b9\u11bb\u11c3-\u11ea\u11ec-\u11ef\u11f1-\u11f8\u11fa-\u1dff\u1e9c-\u1e9f\u1efa-\u1eff\u1f16-\u1f17\u1f1e-\u1f1f\u1f46-\u1f47\u1f4e-\u1f4f\u1f58\u1f5a\u1f5c\u1f5e\u1f7e-\u1f7f\u1fb5\u1fbd\u1fbf-\u1fc1\u1fc5\u1fcd-\u1fcf\u1fd4-\u1fd5\u1fdc-\u1fdf\u1fed-\u1ff1\u1ff5\u1ffd-\u2125\u2127-\u2129\u212c-\u212d\u212f-\u217f\u2183-\u3006\u3008-\u3020\u302a-\u3040\u3095-\u30a0\u30fb-\u3104\u312d-\u4dff\u9fa6-\uabff\ud7a4-\uffff]')  # noqa

# Simpler things
nonPubidCharRegexp = re.compile("[^\x20\x0D\x0Aa-zA-Z0-9\\-'()+,./:=?;!*#@$_%]")


class InfosetFilter(object):
    replacementRegexp = re.compile(r"U[\dA-F]{5,5}")

    def __init__(self,
                 dropXmlnsLocalName=False,
                 dropXmlnsAttrNs=False,
                 preventDoubleDashComments=False,
                 preventDashAtCommentEnd=False,
                 replaceFormFeedCharacters=True,
                 preventSingleQuotePubid=False):

        self.dropXmlnsLocalName = dropXmlnsLocalName
        self.dropXmlnsAttrNs = dropXmlnsAttrNs

        self.preventDoubleDashComments = preventDoubleDashComments
        self.preventDashAtCommentEnd = preventDashAtCommentEnd

        self.replaceFormFeedCharacters = replaceFormFeedCharacters

        self.preventSingleQuotePubid = preventSingleQuotePubid

        self.replaceCache = {}

    def coerceAttribute(self, name, namespace=None):
        if self.dropXmlnsLocalName and name.startswith("xmlns:"):
            warnings.warn("Attributes cannot begin with xmlns", DataLossWarning)
            return None
        elif (self.dropXmlnsAttrNs and
              namespace == "http://www.w3.org/2000/xmlns/"):
            warnings.warn("Attributes cannot be in the xml namespace", DataLossWarning)
            return None
        else:
            return self.toXmlName(name)

    def coerceElement(self, name):
        return self.toXmlName(name)

    def coerceComment(self, data):
        if self.preventDoubleDashComments:
            while "--" in data:
                warnings.warn("Comments cannot contain adjacent dashes", DataLossWarning)
                data = data.replace("--", "- -")
            if data.endswith("-"):
                warnings.warn("Comments cannot end in a dash", DataLossWarning)
                data += " "
        return data

    def coerceCharacters(self, data):
        if self.replaceFormFeedCharacters:
            for _ in range(data.count("\x0C")):
                warnings.warn("Text cannot contain U+000C", DataLossWarning)
            data = data.replace("\x0C", " ")
        # Other non-xml characters
        return data

    def coercePubid(self, data):
        dataOutput = data
        for char in nonPubidCharRegexp.findall(data):
            warnings.warn("Coercing non-XML pubid", DataLossWarning)
            replacement = self.getReplacementCharacter(char)
            dataOutput = dataOutput.replace(char, replacement)
        if self.preventSingleQuotePubid and dataOutput.find("'") >= 0:
            warnings.warn("Pubid cannot contain single quote", DataLossWarning)
            dataOutput = dataOutput.replace("'", self.getReplacementCharacter("'"))
        return dataOutput

    def toXmlName(self, name):
        nameFirst = name[0]
        nameRest = name[1:]
        m = nonXmlNameFirstBMPRegexp.match(nameFirst)
        if m:
            warnings.warn("Coercing non-XML name: %s" % name, DataLossWarning)
            nameFirstOutput = self.getReplacementCharacter(nameFirst)
        else:
            nameFirstOutput = nameFirst

        nameRestOutput = nameRest
        replaceChars = set(nonXmlNameBMPRegexp.findall(nameRest))
        for char in replaceChars:
            warnings.warn("Coercing non-XML name: %s" % name, DataLossWarning)
            replacement = self.getReplacementCharacter(char)
            nameRestOutput = nameRestOutput.replace(char, replacement)
        return nameFirstOutput + nameRestOutput

    def getReplacementCharacter(self, char):
        if char in self.replaceCache:
            replacement = self.replaceCache[char]
        else:
            replacement = self.escapeChar(char)
        return replacement

    def fromXmlName(self, name):
        for item in set(self.replacementRegexp.findall(name)):
            name = name.replace(item, self.unescapeChar(item))
        return name

    def escapeChar(self, char):
        replacement = "U%05X" % ord(char)
        self.replaceCache[char] = replacement
        return replacement

    def unescapeChar(self, charcode):
        return chr(int(charcode[1:], 16))
