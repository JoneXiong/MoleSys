# -*- coding: utf-8 -*-

class Promise(object):
    """
    This is just a base class for the proxy class created in
    the closure of the lazy function. It can be used to recognize
    promises in code.
    """
    pass

def smart_str(s, encoding='utf-8', strings_only=False, errors='strict'):
    """
    Returns a bytestring version of 's', encoded as specified in 'encoding'.

    If strings_only is True, don't convert (some) non-string-like objects.
    """
    if strings_only and isinstance(s, (types.NoneType, int)):
        return s
    if isinstance(s, Promise):
        return unicode(s).encode(encoding, errors)
    elif not isinstance(s, basestring):
        try:
            return str(s)
        except UnicodeEncodeError:
            if isinstance(s, Exception):
                # An Exception subclass containing non-ASCII data that doesn't
                # know how to print itself properly. We shouldn't raise a
                # further exception.
                return ' '.join([smart_str(arg, encoding, strings_only,
                        errors) for arg in s])
            return unicode(s).encode(encoding, errors)
    elif isinstance(s, unicode):
        return s.encode(encoding, errors)
    elif s and encoding != 'utf-8':
        return s.decode('utf-8', errors).encode(encoding, errors)
    else:
        return s
    
def force_unicode(s, encoding='utf-8', strings_only=False, errors='strict'):
    """
    Similar to smart_unicode, except that lazy instances are resolved to
    strings, rather than kept as lazy objects.

    If strings_only is True, don't convert (some) non-string-like objects.
    """
    from ..utils import is_protected_type
    if strings_only and is_protected_type(s):
        return s
    try:
        if not isinstance(s, basestring,):
            if hasattr(s, '__unicode__'):
                s = unicode(s)
            else:
                try:
                    s = unicode(str(s), encoding, errors)
                except UnicodeEncodeError:
                    if not isinstance(s, Exception):
                        raise
                    # If we get to here, the caller has passed in an Exception
                    # subclass populated with non-ASCII data without special
                    # handling to display as a string. We need to handle this
                    # without raising a further exception. We do an
                    # approximation to what the Exception's standard str()
                    # output should be.
                    s = ' '.join([force_unicode(arg, encoding, strings_only,
                            errors) for arg in s])
        elif not isinstance(s, unicode):
            # Note: We use .decode() here, instead of unicode(s, encoding,
            # errors), so that if s is a SafeString, it ends up being a
            # SafeUnicode at the end.
            s = s.decode(encoding, errors)
    except UnicodeDecodeError, e:
        if not isinstance(s, Exception):
            raise DjangoUnicodeDecodeError(s, *e.args)
        else:
            # If we get to here, the caller has passed in an Exception
            # subclass populated with non-ASCII bytestring data without a
            # working unicode method. Try to handle this without raising a
            # further exception by individually forcing the exception args
            # to unicode.
            s = ' '.join([force_unicode(arg, encoding, strings_only,
                    errors) for arg in s])
    return s

def smart_unicode(s, encoding='utf-8', strings_only=False, errors='strict'):
    """
    Returns a unicode object representing 's'. Treats bytestrings using the
    'encoding' codec.

    If strings_only is True, don't convert (some) non-string-like objects.
    """
    if isinstance(s, Promise):
        # The input is the result of a gettext_lazy() call.
        return s
    return force_unicode(s, encoding, strings_only, errors)

class StrAndUnicode(object):
    """
    A class whose __str__ returns its __unicode__ as a UTF-8 bytestring.

    Useful as a mix-in.
    """
    def __str__(self):
        return self.__unicode__().encode('utf-8')