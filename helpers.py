import urllib2

class MethodRequest(urllib2.Request):
    '''
    Work around for using DELETE and PUT with urllib2.
    '''
    
    def __init__(self, url, method, data = None, headers = {},
        origin_req_host = None, unverifiable = False):
        self._method = method
        urllib2.Request.__init__(self, url, data, headers,
            origin_req_host, unverifiable)
    
    def get_method(self):
        if self._method:
            return self._method
        else:
            return urllib2.Request.get_method(self)
        
def merge(source, destination, mergeKeyValues = False):
    '''
    Merges two dictionaries, non-destructively, combining
    values on duplicate keys as defined by mergeKeyValues.
    '''
    
    result = dict(destination)
    
    for k,v in source.iteritems():
        if k in result:
            result[k] = result[k]+';'+v if mergeKeyValues else v
        else:
            result[k] = v
        
    return result
    
def check(v1, v2):
    '''
    Compares two values.
    Returns second value if first does not exist.
    '''
    
    if v1:return v1
    else:return v2
    
