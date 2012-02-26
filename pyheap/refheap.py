from json import loads
from httplib2 import Http
from urllib import urlencode
from httplib2.socks import HTTPError

class Paste:
  base_url = 'https://refheap.com/api'
  
  def __init__(self, username=None, token=None):
    self.credentials = {'username':username, 'token':token}
    
  # Get paste
  def get(self, id):
    '''Gets a paste from RefHeap.'''
    try:
      url = '%s/paste/%s' % (self.base_url, id)
      conn = Http(disable_ssl_certificate_validation=True)
      resp, content = conn.request(url, 'GET')
    except HTTPError, e:return e
    else:return (resp, content)
    
  # Create paste
  def create(self, text, private=False, lang='Plain Text'):
    '''Creates a new paste on RefHeap.'''
    try:
      url = '%s/paste' % (self.base_url)
      conn = Http(disable_ssl_certificate_validation=True)
      #conn.add_credentials(self.credentials['username'], self.credentials['token'])
      data = {'contents':text, 'private':int(private), 'language':lang}
      data.update(self.credentials)
      resp, content = conn.request(url, 'POST', urlencode(data))
    except HTTPError, e:return e
    else:return (resp, content)
    
  # Edit paste
  def edit():
    '''Edits a paste on RefHeap.'''
    return None
    
  # Fork paste
  def fork():
    '''Creates a fork of a paste on RefHeap.'''
    return None
    
  # Delete paste
  def delete():
    '''Deletes a paste from RefHeap.'''
    return None
    
