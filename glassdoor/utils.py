import re

def intify(s):
    """Coerce string to int, returning 'NA' if string contains no numbers"""
    stripped = re.sub("[^0-9]", "", s)
    if stripped is '':
        return 'NA'
    return int(stripped)

def tryelse(func, default='', exception=Exception, log=False):
    """
    """
    try:
        return func()
    except exception as e:
        if log:
            print e
        return default
