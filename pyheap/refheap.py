import json
import urllib2

from helpers import *
from urllib import urlencode

class Refheap:
    base_url = 'https://refheap.com/api'
    
    def __init__(self, username = None, token = None):
        self.credentials = {'username': username, 'token': token}
        
    # get a paste from refheap
    def get(self, id):
        url = '%s/paste/%s' % (self.base_url, id)
        request = MethodRequest(url, 'GET')
        response = urllib2.urlopen(request)
        return json.loads(response.read())
        
    # fork a paste on refheap
    def fork(self, id):
        url = '%s/paste/%s/fork' % (self.base_url, id)
        data = urlencode(self.credentials)
        request = MethodRequest(url, 'POST', data)
        response = urllib2.urlopen(request)
        return json.loads(response.read())
        
    # delete a paste from refheap
    def delete(self, id):
        url = '%s/paste/%s' % (self.base_url, id)
        data = urlencode(self.credentials)
        request = MethodRequest(url, 'DELETE', data)
        response = urllib2.urlopen(request)
        
    # create a new paste on refheap
    def create(self, text, private = False, language = 'Plain Text'):
        private = 'true' if private else 'false'
        url = '%s/paste' % (self.base_url)
        data = urlencode(merge(self.credentials, {
            'private': private,
            'language': language,
            'contents': text}))
            
        request = MethodRequest(url, 'POST', data)
        response = urllib2.urlopen(request)
        return json.loads(response.read())
        
    # edit a paste on refheap
    def edit(self, id, text, private = None, language = None):
        paste = self.get(id)
        private = 'true' if private else 'false'
        url = '%s/paste/%s' % (self.base_url, id)
        
        data = urlencode(merge(self.credentials, {
            'private': check(private, paste['private']),
            'language': check(language, paste['language']),
            'contents': check(text, paste['contents'])}))
            
        request = MethodRequest(url, 'POST', data)
        response = urllib2.urlopen(request)
        return json.loads(response.read())
        
