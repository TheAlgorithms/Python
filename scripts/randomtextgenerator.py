import random
import string


digits = "".join( [random.choice(string.digits) for i in xrange(8)] )
chars = "".join( [random.choice(string.letters) for i in xrange(15)] )

print digits + chars
