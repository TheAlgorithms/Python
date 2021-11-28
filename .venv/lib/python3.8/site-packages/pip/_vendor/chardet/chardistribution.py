######################## BEGIN LICENSE BLOCK ########################
# The Original Code is Mozilla Communicator client code.
#
# The Initial Developer of the Original Code is
# Netscape Communications Corporation.
# Portions created by the Initial Developer are Copyright (C) 1998
# the Initial Developer. All Rights Reserved.
#
# Contributor(s):
#   Mark Pilgrim - port to Python
#
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

from .euctwfreq import (EUCTW_CHAR_TO_FREQ_ORDER, EUCTW_TABLE_SIZE,
                        EUCTW_TYPICAL_DISTRIBUTION_RATIO)
from .euckrfreq import (EUCKR_CHAR_TO_FREQ_ORDER, EUCKR_TABLE_SIZE,
                        EUCKR_TYPICAL_DISTRIBUTION_RATIO)
from .gb2312freq import (GB2312_CHAR_TO_FREQ_ORDER, GB2312_TABLE_SIZE,
                         GB2312_TYPICAL_DISTRIBUTION_RATIO)
from .big5freq import (BIG5_CHAR_TO_FREQ_ORDER, BIG5_TABLE_SIZE,
                       BIG5_TYPICAL_DISTRIBUTION_RATIO)
from .jisfreq import (JIS_CHAR_TO_FREQ_ORDER, JIS_TABLE_SIZE,
                      JIS_TYPICAL_DISTRIBUTION_RATIO)


class CharDistributionAnalysis(object):
    ENOUGH_DATA_THRESHOLD = 1024
    SURE_YES = 0.99
    SURE_NO = 0.01
    MINIMUM_DATA_THRESHOLD = 3

    def __init__(self):
        # Mapping table to get frequency order from char order (get from
        # GetOrder())
        self._char_to_freq_order = None
        self._table_size = None  # Size of above table
        # This is a constant value which varies from language to language,
        # used in calculating confidence.  See
        # http://www.mozilla.org/projects/intl/UniversalCharsetDetection.html
        # for further detail.
        self.typical_distribution_ratio = None
        self._done = None
        self._total_chars = None
        self._freq_chars = None
        self.reset()

    def reset(self):
        """reset analyser, clear any state"""
        # If this flag is set to True, detection is done and conclusion has
        # been made
        self._done = False
        self._total_chars = 0  # Total characters encountered
        # The number of characters whose frequency order is less than 512
        self._freq_chars = 0

    def feed(self, char, char_len):
        """feed a character with known length"""
        if char_len == 2:
            # we only care about 2-bytes character in our distribution analysis
            order = self.get_order(char)
        else:
            order = -1
        if order >= 0:
            self._total_chars += 1
            # order is valid
            if order < self._table_size:
                if 512 > self._char_to_freq_order[order]:
                    self._freq_chars += 1

    def get_confidence(self):
        """return confidence based on existing data"""
        # if we didn't receive any character in our consideration range,
        # return negative answer
        if self._total_chars <= 0 or self._freq_chars <= self.MINIMUM_DATA_THRESHOLD:
            return self.SURE_NO

        if self._total_chars != self._freq_chars:
            r = (self._freq_chars / ((self._total_chars - self._freq_chars)
                 * self.typical_distribution_ratio))
            if r < self.SURE_YES:
                return r

        # normalize confidence (we don't want to be 100% sure)
        return self.SURE_YES

    def got_enough_data(self):
        # It is not necessary to receive all data to draw conclusion.
        # For charset detection, certain amount of data is enough
        return self._total_chars > self.ENOUGH_DATA_THRESHOLD

    def get_order(self, byte_str):
        # We do not handle characters based on the original encoding string,
        # but convert this encoding string to a number, here called order.
        # This allows multiple encodings of a language to share one frequency
        # table.
        return -1


class EUCTWDistributionAnalysis(CharDistributionAnalysis):
    def __init__(self):
        super(EUCTWDistributionAnalysis, self).__init__()
        self._char_to_freq_order = EUCTW_CHAR_TO_FREQ_ORDER
        self._table_size = EUCTW_TABLE_SIZE
        self.typical_distribution_ratio = EUCTW_TYPICAL_DISTRIBUTION_RATIO

    def get_order(self, byte_str):
        # for euc-TW encoding, we are interested
        #   first  byte range: 0xc4 -- 0xfe
        #   second byte range: 0xa1 -- 0xfe
        # no validation needed here. State machine has done that
        first_char = byte_str[0]
        if first_char >= 0xC4:
            return 94 * (first_char - 0xC4) + byte_str[1] - 0xA1
        else:
            return -1


class EUCKRDistributionAnalysis(CharDistributionAnalysis):
    def __init__(self):
        super(EUCKRDistributionAnalysis, self).__init__()
        self._char_to_freq_order = EUCKR_CHAR_TO_FREQ_ORDER
        self._table_size = EUCKR_TABLE_SIZE
        self.typical_distribution_ratio = EUCKR_TYPICAL_DISTRIBUTION_RATIO

    def get_order(self, byte_str):
        # for euc-KR encoding, we are interested
        #   first  byte range: 0xb0 -- 0xfe
        #   second byte range: 0xa1 -- 0xfe
        # no validation needed here. State machine has done that
        first_char = byte_str[0]
        if first_char >= 0xB0:
            return 94 * (first_char - 0xB0) + byte_str[1] - 0xA1
        else:
            return -1


class GB2312DistributionAnalysis(CharDistributionAnalysis):
    def __init__(self):
        super(GB2312DistributionAnalysis, self).__init__()
        self._char_to_freq_order = GB2312_CHAR_TO_FREQ_ORDER
        self._table_size = GB2312_TABLE_SIZE
        self.typical_distribution_ratio = GB2312_TYPICAL_DISTRIBUTION_RATIO

    def get_order(self, byte_str):
        # for GB2312 encoding, we are interested
        #  first  byte range: 0xb0 -- 0xfe
        #  second byte range: 0xa1 -- 0xfe
        # no validation needed here. State machine has done that
        first_char, second_char = byte_str[0], byte_str[1]
        if (first_char >= 0xB0) and (second_char >= 0xA1):
            return 94 * (first_char - 0xB0) + second_char - 0xA1
        else:
            return -1


class Big5DistributionAnalysis(CharDistributionAnalysis):
    def __init__(self):
        super(Big5DistributionAnalysis, self).__init__()
        self._char_to_freq_order = BIG5_CHAR_TO_FREQ_ORDER
        self._table_size = BIG5_TABLE_SIZE
        self.typical_distribution_ratio = BIG5_TYPICAL_DISTRIBUTION_RATIO

    def get_order(self, byte_str):
        # for big5 encoding, we are interested
        #   first  byte range: 0xa4 -- 0xfe
        #   second byte range: 0x40 -- 0x7e , 0xa1 -- 0xfe
        # no validation needed here. State machine has done that
        first_char, second_char = byte_str[0], byte_str[1]
        if first_char >= 0xA4:
            if second_char >= 0xA1:
                return 157 * (first_char - 0xA4) + second_char - 0xA1 + 63
            else:
                return 157 * (first_char - 0xA4) + second_char - 0x40
        else:
            return -1


class SJISDistributionAnalysis(CharDistributionAnalysis):
    def __init__(self):
        super(SJISDistributionAnalysis, self).__init__()
        self._char_to_freq_order = JIS_CHAR_TO_FREQ_ORDER
        self._table_size = JIS_TABLE_SIZE
        self.typical_distribution_ratio = JIS_TYPICAL_DISTRIBUTION_RATIO

    def get_order(self, byte_str):
        # for sjis encoding, we are interested
        #   first  byte range: 0x81 -- 0x9f , 0xe0 -- 0xfe
        #   second byte range: 0x40 -- 0x7e,  0x81 -- oxfe
        # no validation needed here. State machine has done that
        first_char, second_char = byte_str[0], byte_str[1]
        if (first_char >= 0x81) and (first_char <= 0x9F):
            order = 188 * (first_char - 0x81)
        elif (first_char >= 0xE0) and (first_char <= 0xEF):
            order = 188 * (first_char - 0xE0 + 31)
        else:
            return -1
        order = order + second_char - 0x40
        if second_char > 0x7F:
            order = -1
        return order


class EUCJPDistributionAnalysis(CharDistributionAnalysis):
    def __init__(self):
        super(EUCJPDistributionAnalysis, self).__init__()
        self._char_to_freq_order = JIS_CHAR_TO_FREQ_ORDER
        self._table_size = JIS_TABLE_SIZE
        self.typical_distribution_ratio = JIS_TYPICAL_DISTRIBUTION_RATIO

    def get_order(self, byte_str):
        # for euc-JP encoding, we are interested
        #   first  byte range: 0xa0 -- 0xfe
        #   second byte range: 0xa1 -- 0xfe
        # no validation needed here. State machine has done that
        char = byte_str[0]
        if char >= 0xA0:
            return 94 * (char - 0xA1) + byte_str[1] - 0xa1
        else:
            return -1
