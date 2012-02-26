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
    else:return (resp, loads(content))
    
  # Create paste
  def create(self, text, private=False, lang='Plain Text'):
    '''Creates a new paste on RefHeap.'''
    try:
      url = '%s/paste' % (self.base_url)
      data = {'contents':text, 'private':str.lower(str(private)), 'language':lang}
      data.update(self.credentials) # Add username/token to data hash
      headers = {'Content-Type':'application/x-www-form-urlencoded'}
      conn = Http(disable_ssl_certificate_validation=True)
      resp, content = conn.request(url, 'POST', urlencode(data), headers)
    except HTTPError, e:return e
    else:return (resp, loads(content))
    
  # Edit paste
  def edit(self, id, text=None, private=None, lang=None):
    '''Edits a paste on RefHeap.'''
    try:
      orig_p = (self.get(id))[1] # Get the original paste
      url = '%s/paste/%s' % (self.base_url, id)
      data = { # Check for changes to original paste
        'contents':orig_p['contents'] if text is None else text,
        'private':str.lower(str(orig_p['private'] if private is None else private)),
        'language':orig_p['language'] if lang is None else lang}
      data.update(self.credentials) # Add username/token to data hash
      headers = {'Content-Type':'application/x-www-form-urlencoded'}
      conn = Http(disable_ssl_certificate_validation=True)
      resp, content = conn.request(url, 'POST', urlencode(data), headers)
    except HTTPError, e:return e
    else:return (resp, loads(content))
    
  # Fork paste
  def fork(self, id):
    '''Creates a fork of a paste on RefHeap.'''
    try:
      url = '%s/paste/%s/fork' % (self.base_url, id)
      conn = Http(disable_ssl_certificate_validation=True)
      headers = {'Content-Type':'application/x-www-form-urlencoded'}
      resp, content = conn.request(url, 'POST', urlencode(self.credentials), headers)
    except HTTPError, e:return e
    else:return (resp, loads(content))
    
  # Delete paste
  def delete(self, id):
    '''Deletes a paste from RefHeap.'''
    try:
      url = '%s/paste/%s' % (self.base_url, id)
      conn = Http(disable_ssl_certificate_validation=True)
      headers = {'Content-Type':'application/x-www-form-urlencoded'}
      resp, content = conn.request(url, 'DELETE', urlencode(self.credentials), headers)
    except HTTPError, e:return e
    else:return (resp, None)
    
