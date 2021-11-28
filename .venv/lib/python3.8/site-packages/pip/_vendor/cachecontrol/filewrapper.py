from io import BytesIO


class CallbackFileWrapper(object):
    """
    Small wrapper around a fp object which will tee everything read into a
    buffer, and when that file is closed it will execute a callback with the
    contents of that buffer.

    All attributes are proxied to the underlying file object.

    This class uses members with a double underscore (__) leading prefix so as
    not to accidentally shadow an attribute.
    """

    def __init__(self, fp, callback):
        self.__buf = BytesIO()
        self.__fp = fp
        self.__callback = callback

    def __getattr__(self, name):
        # The vaguaries of garbage collection means that self.__fp is
        # not always set.  By using __getattribute__ and the private
        # name[0] allows looking up the attribute value and raising an
        # AttributeError when it doesn't exist. This stop thigns from
        # infinitely recursing calls to getattr in the case where
        # self.__fp hasn't been set.
        #
        # [0] https://docs.python.org/2/reference/expressions.html#atom-identifiers
        fp = self.__getattribute__("_CallbackFileWrapper__fp")
        return getattr(fp, name)

    def __is_fp_closed(self):
        try:
            return self.__fp.fp is None

        except AttributeError:
            pass

        try:
            return self.__fp.closed

        except AttributeError:
            pass

        # We just don't cache it then.
        # TODO: Add some logging here...
        return False

    def _close(self):
        if self.__callback:
            self.__callback(self.__buf.getvalue())

        # We assign this to None here, because otherwise we can get into
        # really tricky problems where the CPython interpreter dead locks
        # because the callback is holding a reference to something which
        # has a __del__ method. Setting this to None breaks the cycle
        # and allows the garbage collector to do it's thing normally.
        self.__callback = None

    def read(self, amt=None):
        data = self.__fp.read(amt)
        self.__buf.write(data)
        if self.__is_fp_closed():
            self._close()

        return data

    def _safe_read(self, amt):
        data = self.__fp._safe_read(amt)
        if amt == 2 and data == b"\r\n":
            # urllib executes this read to toss the CRLF at the end
            # of the chunk.
            return data

        self.__buf.write(data)
        if self.__is_fp_closed():
            self._close()

        return data
