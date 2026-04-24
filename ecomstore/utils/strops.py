from django.utils.encoding import smart_str, smart_text
# find a substring between separators

def find_between( s, first, last ):
    try:
        start = s.index( first ) + len( first )
        end = s.index( last, start )
        return s[start:end]
    except ValueError:
        return ""

def find_between_r( s, first, last ):
    try:
        start = s.rindex( first ) + len( first )
        end = s.rindex( last, start )
        return s[start:end]
    except ValueError:
        return ""

# picking up piece of string between separators
# function using partition, like partition, but drops the separators
def between(left,right,s):
    before,_,a = s.partition(left)
    a,_,after = a.partition(right)
    return before,a,after


def normalize_str(s):
   a = s.rstrip();
   b = a.lstrip();

   r = smart_str(b)

   return r

def replace_str(s, old, new):
    import re
    compiled = re.compile(re.escape(old), re.IGNORECASE)
    res = compiled.sub(new, s)

    return str(res)


def smart_truncate(s, width):
    if width >= len(s):
         return s
    if s[width].isspace():
        return s[0:width];
    else:
        return s[0:width].rsplit(None, 1)[0]

def not_null(s1, s2):
    if not s1:
        return s2
    return s1
