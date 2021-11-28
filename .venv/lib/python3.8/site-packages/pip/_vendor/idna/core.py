from . import idnadata
import bisect
import unicodedata
import re
import sys
from .intranges import intranges_contain

_virama_combining_class = 9
_alabel_prefix = b'xn--'
_unicode_dots_re = re.compile('[\u002e\u3002\uff0e\uff61]')

class IDNAError(UnicodeError):
    """ Base exception for all IDNA-encoding related problems """
    pass


class IDNABidiError(IDNAError):
    """ Exception when bidirectional requirements are not satisfied """
    pass


class InvalidCodepoint(IDNAError):
    """ Exception when a disallowed or unallocated codepoint is used """
    pass


class InvalidCodepointContext(IDNAError):
    """ Exception when the codepoint is not valid in the context it is used """
    pass


def _combining_class(cp):
    v = unicodedata.combining(chr(cp))
    if v == 0:
        if not unicodedata.name(chr(cp)):
            raise ValueError('Unknown character in unicodedata')
    return v

def _is_script(cp, script):
    return intranges_contain(ord(cp), idnadata.scripts[script])

def _punycode(s):
    return s.encode('punycode')

def _unot(s):
    return 'U+{:04X}'.format(s)


def valid_label_length(label):

    if len(label) > 63:
        return False
    return True


def valid_string_length(label, trailing_dot):

    if len(label) > (254 if trailing_dot else 253):
        return False
    return True


def check_bidi(label, check_ltr=False):

    # Bidi rules should only be applied if string contains RTL characters
    bidi_label = False
    for (idx, cp) in enumerate(label, 1):
        direction = unicodedata.bidirectional(cp)
        if direction == '':
            # String likely comes from a newer version of Unicode
            raise IDNABidiError('Unknown directionality in label {} at position {}'.format(repr(label), idx))
        if direction in ['R', 'AL', 'AN']:
            bidi_label = True
    if not bidi_label and not check_ltr:
        return True

    # Bidi rule 1
    direction = unicodedata.bidirectional(label[0])
    if direction in ['R', 'AL']:
        rtl = True
    elif direction == 'L':
        rtl = False
    else:
        raise IDNABidiError('First codepoint in label {} must be directionality L, R or AL'.format(repr(label)))

    valid_ending = False
    number_type = False
    for (idx, cp) in enumerate(label, 1):
        direction = unicodedata.bidirectional(cp)

        if rtl:
            # Bidi rule 2
            if not direction in ['R', 'AL', 'AN', 'EN', 'ES', 'CS', 'ET', 'ON', 'BN', 'NSM']:
                raise IDNABidiError('Invalid direction for codepoint at position {} in a right-to-left label'.format(idx))
            # Bidi rule 3
            if direction in ['R', 'AL', 'EN', 'AN']:
                valid_ending = True
            elif direction != 'NSM':
                valid_ending = False
            # Bidi rule 4
            if direction in ['AN', 'EN']:
                if not number_type:
                    number_type = direction
                else:
                    if number_type != direction:
                        raise IDNABidiError('Can not mix numeral types in a right-to-left label')
        else:
            # Bidi rule 5
            if not direction in ['L', 'EN', 'ES', 'CS', 'ET', 'ON', 'BN', 'NSM']:
                raise IDNABidiError('Invalid direction for codepoint at position {} in a left-to-right label'.format(idx))
            # Bidi rule 6
            if direction in ['L', 'EN']:
                valid_ending = True
            elif direction != 'NSM':
                valid_ending = False

    if not valid_ending:
        raise IDNABidiError('Label ends with illegal codepoint directionality')

    return True


def check_initial_combiner(label):

    if unicodedata.category(label[0])[0] == 'M':
        raise IDNAError('Label begins with an illegal combining character')
    return True


def check_hyphen_ok(label):

    if label[2:4] == '--':
        raise IDNAError('Label has disallowed hyphens in 3rd and 4th position')
    if label[0] == '-' or label[-1] == '-':
        raise IDNAError('Label must not start or end with a hyphen')
    return True


def check_nfc(label):

    if unicodedata.normalize('NFC', label) != label:
        raise IDNAError('Label must be in Normalization Form C')


def valid_contextj(label, pos):

    cp_value = ord(label[pos])

    if cp_value == 0x200c:

        if pos > 0:
            if _combining_class(ord(label[pos - 1])) == _virama_combining_class:
                return True

        ok = False
        for i in range(pos-1, -1, -1):
            joining_type = idnadata.joining_types.get(ord(label[i]))
            if joining_type == ord('T'):
                continue
            if joining_type in [ord('L'), ord('D')]:
                ok = True
                break

        if not ok:
            return False

        ok = False
        for i in range(pos+1, len(label)):
            joining_type = idnadata.joining_types.get(ord(label[i]))
            if joining_type == ord('T'):
                continue
            if joining_type in [ord('R'), ord('D')]:
                ok = True
                break
        return ok

    if cp_value == 0x200d:

        if pos > 0:
            if _combining_class(ord(label[pos - 1])) == _virama_combining_class:
                return True
        return False

    else:

        return False


def valid_contexto(label, pos, exception=False):

    cp_value = ord(label[pos])

    if cp_value == 0x00b7:
        if 0 < pos < len(label)-1:
            if ord(label[pos - 1]) == 0x006c and ord(label[pos + 1]) == 0x006c:
                return True
        return False

    elif cp_value == 0x0375:
        if pos < len(label)-1 and len(label) > 1:
            return _is_script(label[pos + 1], 'Greek')
        return False

    elif cp_value == 0x05f3 or cp_value == 0x05f4:
        if pos > 0:
            return _is_script(label[pos - 1], 'Hebrew')
        return False

    elif cp_value == 0x30fb:
        for cp in label:
            if cp == '\u30fb':
                continue
            if _is_script(cp, 'Hiragana') or _is_script(cp, 'Katakana') or _is_script(cp, 'Han'):
                return True
        return False

    elif 0x660 <= cp_value <= 0x669:
        for cp in label:
            if 0x6f0 <= ord(cp) <= 0x06f9:
                return False
        return True

    elif 0x6f0 <= cp_value <= 0x6f9:
        for cp in label:
            if 0x660 <= ord(cp) <= 0x0669:
                return False
        return True


def check_label(label):

    if isinstance(label, (bytes, bytearray)):
        label = label.decode('utf-8')
    if len(label) == 0:
        raise IDNAError('Empty Label')

    check_nfc(label)
    check_hyphen_ok(label)
    check_initial_combiner(label)

    for (pos, cp) in enumerate(label):
        cp_value = ord(cp)
        if intranges_contain(cp_value, idnadata.codepoint_classes['PVALID']):
            continue
        elif intranges_contain(cp_value, idnadata.codepoint_classes['CONTEXTJ']):
            try:
                if not valid_contextj(label, pos):
                    raise InvalidCodepointContext('Joiner {} not allowed at position {} in {}'.format(
                        _unot(cp_value), pos+1, repr(label)))
            except ValueError:
                raise IDNAError('Unknown codepoint adjacent to joiner {} at position {} in {}'.format(
                    _unot(cp_value), pos+1, repr(label)))
        elif intranges_contain(cp_value, idnadata.codepoint_classes['CONTEXTO']):
            if not valid_contexto(label, pos):
                raise InvalidCodepointContext('Codepoint {} not allowed at position {} in {}'.format(_unot(cp_value), pos+1, repr(label)))
        else:
            raise InvalidCodepoint('Codepoint {} at position {} of {} not allowed'.format(_unot(cp_value), pos+1, repr(label)))

    check_bidi(label)


def alabel(label):

    try:
        label = label.encode('ascii')
        ulabel(label)
        if not valid_label_length(label):
            raise IDNAError('Label too long')
        return label
    except UnicodeEncodeError:
        pass

    if not label:
        raise IDNAError('No Input')

    label = str(label)
    check_label(label)
    label = _punycode(label)
    label = _alabel_prefix + label

    if not valid_label_length(label):
        raise IDNAError('Label too long')

    return label


def ulabel(label):

    if not isinstance(label, (bytes, bytearray)):
        try:
            label = label.encode('ascii')
        except UnicodeEncodeError:
            check_label(label)
            return label

    label = label.lower()
    if label.startswith(_alabel_prefix):
        label = label[len(_alabel_prefix):]
        if not label:
            raise IDNAError('Malformed A-label, no Punycode eligible content found')
        if label.decode('ascii')[-1] == '-':
            raise IDNAError('A-label must not end with a hyphen')
    else:
        check_label(label)
        return label.decode('ascii')

    label = label.decode('punycode')
    check_label(label)
    return label


def uts46_remap(domain, std3_rules=True, transitional=False):
    """Re-map the characters in the string according to UTS46 processing."""
    from .uts46data import uts46data
    output = ''
    try:
        for pos, char in enumerate(domain):
            code_point = ord(char)
            uts46row = uts46data[code_point if code_point < 256 else
                bisect.bisect_left(uts46data, (code_point, 'Z')) - 1]
            status = uts46row[1]
            replacement = uts46row[2] if len(uts46row) == 3 else None
            if (status == 'V' or
                    (status == 'D' and not transitional) or
                    (status == '3' and not std3_rules and replacement is None)):
                output += char
            elif replacement is not None and (status == 'M' or
                    (status == '3' and not std3_rules) or
                    (status == 'D' and transitional)):
                output += replacement
            elif status != 'I':
                raise IndexError()
        return unicodedata.normalize('NFC', output)
    except IndexError:
        raise InvalidCodepoint(
            'Codepoint {} not allowed at position {} in {}'.format(
            _unot(code_point), pos + 1, repr(domain)))


def encode(s, strict=False, uts46=False, std3_rules=False, transitional=False):

    if isinstance(s, (bytes, bytearray)):
        s = s.decode('ascii')
    if uts46:
        s = uts46_remap(s, std3_rules, transitional)
    trailing_dot = False
    result = []
    if strict:
        labels = s.split('.')
    else:
        labels = _unicode_dots_re.split(s)
    if not labels or labels == ['']:
        raise IDNAError('Empty domain')
    if labels[-1] == '':
        del labels[-1]
        trailing_dot = True
    for label in labels:
        s = alabel(label)
        if s:
            result.append(s)
        else:
            raise IDNAError('Empty label')
    if trailing_dot:
        result.append(b'')
    s = b'.'.join(result)
    if not valid_string_length(s, trailing_dot):
        raise IDNAError('Domain too long')
    return s


def decode(s, strict=False, uts46=False, std3_rules=False):

    if isinstance(s, (bytes, bytearray)):
        s = s.decode('ascii')
    if uts46:
        s = uts46_remap(s, std3_rules, False)
    trailing_dot = False
    result = []
    if not strict:
        labels = _unicode_dots_re.split(s)
    else:
        labels = s.split('.')
    if not labels or labels == ['']:
        raise IDNAError('Empty domain')
    if not labels[-1]:
        del labels[-1]
        trailing_dot = True
    for label in labels:
        s = ulabel(label)
        if s:
            result.append(s)
        else:
            raise IDNAError('Empty label')
    if trailing_dot:
        result.append('')
    return '.'.join(result)
