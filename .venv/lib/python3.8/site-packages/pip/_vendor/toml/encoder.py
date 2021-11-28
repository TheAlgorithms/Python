import datetime
import re
import sys
from decimal import Decimal

from pip._vendor.toml.decoder import InlineTableDict

if sys.version_info >= (3,):
    unicode = str


def dump(o, f, encoder=None):
    """Writes out dict as toml to a file

    Args:
        o: Object to dump into toml
        f: File descriptor where the toml should be stored
        encoder: The ``TomlEncoder`` to use for constructing the output string

    Returns:
        String containing the toml corresponding to dictionary

    Raises:
        TypeError: When anything other than file descriptor is passed
    """

    if not f.write:
        raise TypeError("You can only dump an object to a file descriptor")
    d = dumps(o, encoder=encoder)
    f.write(d)
    return d


def dumps(o, encoder=None):
    """Stringifies input dict as toml

    Args:
        o: Object to dump into toml
        encoder: The ``TomlEncoder`` to use for constructing the output string

    Returns:
        String containing the toml corresponding to dict

    Examples:
        ```python
        >>> import toml
        >>> output = {
        ... 'a': "I'm a string",
        ... 'b': ["I'm", "a", "list"],
        ... 'c': 2400
        ... }
        >>> toml.dumps(output)
        'a = "I\'m a string"\nb = [ "I\'m", "a", "list",]\nc = 2400\n'
        ```
    """

    retval = ""
    if encoder is None:
        encoder = TomlEncoder(o.__class__)
    addtoretval, sections = encoder.dump_sections(o, "")
    retval += addtoretval
    outer_objs = [id(o)]
    while sections:
        section_ids = [id(section) for section in sections.values()]
        for outer_obj in outer_objs:
            if outer_obj in section_ids:
                raise ValueError("Circular reference detected")
        outer_objs += section_ids
        newsections = encoder.get_empty_table()
        for section in sections:
            addtoretval, addtosections = encoder.dump_sections(
                sections[section], section)

            if addtoretval or (not addtoretval and not addtosections):
                if retval and retval[-2:] != "\n\n":
                    retval += "\n"
                retval += "[" + section + "]\n"
                if addtoretval:
                    retval += addtoretval
            for s in addtosections:
                newsections[section + "." + s] = addtosections[s]
        sections = newsections
    return retval


def _dump_str(v):
    if sys.version_info < (3,) and hasattr(v, 'decode') and isinstance(v, str):
        v = v.decode('utf-8')
    v = "%r" % v
    if v[0] == 'u':
        v = v[1:]
    singlequote = v.startswith("'")
    if singlequote or v.startswith('"'):
        v = v[1:-1]
    if singlequote:
        v = v.replace("\\'", "'")
        v = v.replace('"', '\\"')
    v = v.split("\\x")
    while len(v) > 1:
        i = -1
        if not v[0]:
            v = v[1:]
        v[0] = v[0].replace("\\\\", "\\")
        # No, I don't know why != works and == breaks
        joinx = v[0][i] != "\\"
        while v[0][:i] and v[0][i] == "\\":
            joinx = not joinx
            i -= 1
        if joinx:
            joiner = "x"
        else:
            joiner = "u00"
        v = [v[0] + joiner + v[1]] + v[2:]
    return unicode('"' + v[0] + '"')


def _dump_float(v):
    return "{}".format(v).replace("e+0", "e+").replace("e-0", "e-")


def _dump_time(v):
    utcoffset = v.utcoffset()
    if utcoffset is None:
        return v.isoformat()
    # The TOML norm specifies that it's local time thus we drop the offset
    return v.isoformat()[:-6]


class TomlEncoder(object):

    def __init__(self, _dict=dict, preserve=False):
        self._dict = _dict
        self.preserve = preserve
        self.dump_funcs = {
            str: _dump_str,
            unicode: _dump_str,
            list: self.dump_list,
            bool: lambda v: unicode(v).lower(),
            int: lambda v: v,
            float: _dump_float,
            Decimal: _dump_float,
            datetime.datetime: lambda v: v.isoformat().replace('+00:00', 'Z'),
            datetime.time: _dump_time,
            datetime.date: lambda v: v.isoformat()
        }

    def get_empty_table(self):
        return self._dict()

    def dump_list(self, v):
        retval = "["
        for u in v:
            retval += " " + unicode(self.dump_value(u)) + ","
        retval += "]"
        return retval

    def dump_inline_table(self, section):
        """Preserve inline table in its compact syntax instead of expanding
        into subsection.

        https://github.com/toml-lang/toml#user-content-inline-table
        """
        retval = ""
        if isinstance(section, dict):
            val_list = []
            for k, v in section.items():
                val = self.dump_inline_table(v)
                val_list.append(k + " = " + val)
            retval += "{ " + ", ".join(val_list) + " }\n"
            return retval
        else:
            return unicode(self.dump_value(section))

    def dump_value(self, v):
        # Lookup function corresponding to v's type
        dump_fn = self.dump_funcs.get(type(v))
        if dump_fn is None and hasattr(v, '__iter__'):
            dump_fn = self.dump_funcs[list]
        # Evaluate function (if it exists) else return v
        return dump_fn(v) if dump_fn is not None else self.dump_funcs[str](v)

    def dump_sections(self, o, sup):
        retstr = ""
        if sup != "" and sup[-1] != ".":
            sup += '.'
        retdict = self._dict()
        arraystr = ""
        for section in o:
            section = unicode(section)
            qsection = section
            if not re.match(r'^[A-Za-z0-9_-]+$', section):
                qsection = _dump_str(section)
            if not isinstance(o[section], dict):
                arrayoftables = False
                if isinstance(o[section], list):
                    for a in o[section]:
                        if isinstance(a, dict):
                            arrayoftables = True
                if arrayoftables:
                    for a in o[section]:
                        arraytabstr = "\n"
                        arraystr += "[[" + sup + qsection + "]]\n"
                        s, d = self.dump_sections(a, sup + qsection)
                        if s:
                            if s[0] == "[":
                                arraytabstr += s
                            else:
                                arraystr += s
                        while d:
                            newd = self._dict()
                            for dsec in d:
                                s1, d1 = self.dump_sections(d[dsec], sup +
                                                            qsection + "." +
                                                            dsec)
                                if s1:
                                    arraytabstr += ("[" + sup + qsection +
                                                    "." + dsec + "]\n")
                                    arraytabstr += s1
                                for s1 in d1:
                                    newd[dsec + "." + s1] = d1[s1]
                            d = newd
                        arraystr += arraytabstr
                else:
                    if o[section] is not None:
                        retstr += (qsection + " = " +
                                   unicode(self.dump_value(o[section])) + '\n')
            elif self.preserve and isinstance(o[section], InlineTableDict):
                retstr += (qsection + " = " +
                           self.dump_inline_table(o[section]))
            else:
                retdict[qsection] = o[section]
        retstr += arraystr
        return (retstr, retdict)


class TomlPreserveInlineDictEncoder(TomlEncoder):

    def __init__(self, _dict=dict):
        super(TomlPreserveInlineDictEncoder, self).__init__(_dict, True)


class TomlArraySeparatorEncoder(TomlEncoder):

    def __init__(self, _dict=dict, preserve=False, separator=","):
        super(TomlArraySeparatorEncoder, self).__init__(_dict, preserve)
        if separator.strip() == "":
            separator = "," + separator
        elif separator.strip(' \t\n\r,'):
            raise ValueError("Invalid separator for arrays")
        self.separator = separator

    def dump_list(self, v):
        t = []
        retval = "["
        for u in v:
            t.append(self.dump_value(u))
        while t != []:
            s = []
            for u in t:
                if isinstance(u, list):
                    for r in u:
                        s.append(r)
                else:
                    retval += " " + unicode(u) + self.separator
            t = s
        retval += "]"
        return retval


class TomlNumpyEncoder(TomlEncoder):

    def __init__(self, _dict=dict, preserve=False):
        import numpy as np
        super(TomlNumpyEncoder, self).__init__(_dict, preserve)
        self.dump_funcs[np.float16] = _dump_float
        self.dump_funcs[np.float32] = _dump_float
        self.dump_funcs[np.float64] = _dump_float
        self.dump_funcs[np.int16] = self._dump_int
        self.dump_funcs[np.int32] = self._dump_int
        self.dump_funcs[np.int64] = self._dump_int

    def _dump_int(self, v):
        return "{}".format(int(v))


class TomlPreserveCommentEncoder(TomlEncoder):

    def __init__(self, _dict=dict, preserve=False):
        from pip._vendor.toml.decoder import CommentValue
        super(TomlPreserveCommentEncoder, self).__init__(_dict, preserve)
        self.dump_funcs[CommentValue] = lambda v: v.dump(self.dump_value)


class TomlPathlibEncoder(TomlEncoder):

    def _dump_pathlib_path(self, v):
        return _dump_str(str(v))

    def dump_value(self, v):
        if (3, 4) <= sys.version_info:
            import pathlib
            if isinstance(v, pathlib.PurePath):
                v = str(v)
        return super(TomlPathlibEncoder, self).dump_value(v)
