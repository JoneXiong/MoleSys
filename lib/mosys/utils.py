# -*- coding: utf-8 -*-

def is_protected_type(obj):
    """Determine if the object instance is of a protected type.

    Objects of protected types are preserved as-is when passed to
    force_unicode(strings_only=True).
    """
    return isinstance(obj, (
        types.NoneType,
        int, long,
        datetime.datetime, datetime.date, datetime.time,
        float, Decimal)
    )
    
def gettext(msg):
    return msg



if type('') is not type(b''):
    def u(s):
        return s
    bytes_type = bytes
    unicode_type = str
    basestring_type = str
else:
    def u(s):
        return s.decode('unicode_escape')
    bytes_type = str
    unicode_type = unicode
    basestring_type = basestring
    
_UTF8_TYPES = (bytes_type, type(None))

def utf8(value):
    """Converts a string argument to a byte string.

    If the argument is already a byte string or None, it is returned unchanged.
    Otherwise it must be a unicode string and is encoded as utf8.
    """
    if isinstance(value, _UTF8_TYPES):
        return value
    assert isinstance(value, unicode_type)
    return value.encode("utf-8")



import string, sys

text_characters = "".join(map(chr, range(32, 127)) + list("\n\r\t\b"))
_null_trans = string.maketrans("", "")

def istextfile(filename, blocksize = 512):
    return istext(open(filename).read(blocksize))

def istext(s):
    return 1
    if "\0" in s:
        return 0
    
    if not s:  # Empty files are considered text
        return 1

    # Get the non-text characters (maps a character to itself then
    # use the ‘remove’ option to get rid of the text characters.)
    t = s.translate(_null_trans, text_characters)

    # If more than 30% non-text characters, then
    # this is considered a binary file
    if len(t)/len(s) > 0.30:
        return 0
    return 1