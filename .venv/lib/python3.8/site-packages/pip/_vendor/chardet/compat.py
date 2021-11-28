######################## BEGIN LICENSE BLOCK ########################
# Contributor(s):
#   Dan Blanchard
#   Ian Cordasco
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

import sys


if sys.version_info < (3, 0):
    PY2 = True
    PY3 = False
    string_types = (str, unicode)
    text_type = unicode
    iteritems = dict.iteritems
else:
    PY2 = False
    PY3 = True
    string_types = (bytes, str)
    text_type = str
    iteritems = dict.items
