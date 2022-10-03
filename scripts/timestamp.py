from datetime import tzinfo , timedelta , datetime
import time as t

zero = timedelta(0)

STDOFFSET = timedelta(seconds=-t.timezone)

if t.daylight:
    DSTOFFSET = timedelta(seconds=-t.altzone)
else:
    DSTOFFSET = STDOFFSET

DSTDIFF = DSTOFFSET - STDOFFSET

class UTC(tzinfo):
    def utcoffset(self, dt):
        if self._isdst(dt):
            return DSTOFFSET
        else:
            return STDOFFSET

    def tzname(self, dt):
        return t.tzname[self._isdst(dt)]

    def dst(self, dt):
        if self._isdst(dt):
            return DSTDIFF
        else:
            return zero

    def _isdst(self, dt):
        tt = (dt.year, dt.month, dt.day,
              dt.hour, dt.minute, dt.second,
              dt.weekday(), 0, 0)
        stamp = t.mktime(tt)
        tt = t.localtime(stamp)
        return tt.tm_isdst > 0

Local = UTC()

d = datetime.now(Local)
print(d.isoformat('T'))
