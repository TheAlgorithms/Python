######################## BEGIN LICENSE BLOCK ########################
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA
# 02110-1301  USA
######################### END LICENSE BLOCK #########################


from .universaldetector import UniversalDetector
from .enums import InputState
from .version import __version__, VERSION


__all__ = ['UniversalDetector', 'detect', 'detect_all', '__version__', 'VERSION']


def detect(byte_str):
    """
    Detect the encoding of the given byte string.

    :param byte_str:     The byte sequence to examine.
    :type byte_str:      ``bytes`` or ``bytearray``
    """
    if not isinstance(byte_str, bytearray):
        if not isinstance(byte_str, bytes):
            raise TypeError('Expected object of type bytes or bytearray, got: '
                            '{}'.format(type(byte_str)))
        else:
            byte_str = bytearray(byte_str)
    detector = UniversalDetector()
    detector.feed(byte_str)
    return detector.close()


def detect_all(byte_str):
    """
    Detect all the possible encodings of the given byte string.

    :param byte_str:     The byte sequence to examine.
    :type byte_str:      ``bytes`` or ``bytearray``
    """
    if not isinstance(byte_str, bytearray):
        if not isinstance(byte_str, bytes):
            raise TypeError('Expected object of type bytes or bytearray, got: '
                            '{}'.format(type(byte_str)))
        else:
            byte_str = bytearray(byte_str)

    detector = UniversalDetector()
    detector.feed(byte_str)
    detector.close()

    if detector._input_state == InputState.HIGH_BYTE:
        results = []
        for prober in detector._charset_probers:
            if prober.get_confidence() > detector.MINIMUM_THRESHOLD:
                charset_name = prober.charset_name
                lower_charset_name = prober.charset_name.lower()
                # Use Windows encoding name instead of ISO-8859 if we saw any
                # extra Windows-specific bytes
                if lower_charset_name.startswith('iso-8859'):
                    if detector._has_win_bytes:
                        charset_name = detector.ISO_WIN_MAP.get(lower_charset_name,
                                                            charset_name)
                results.append({
                    'encoding': charset_name,
                    'confidence': prober.get_confidence(),
                    'language': prober.language,
                })
        if len(results) > 0:
            return sorted(results, key=lambda result: -result['confidence'])

    return [detector.result]
