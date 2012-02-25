## PyHeap

PyHeap is a Python wrapper around [RefHeap](https://refheap.com) API. Originally, it was created as a Python learning project for myself. PyHeap is still new and doesn't do much error checking, but it's a start.

You can get the PyHeap source from GitHub:

    git clone git://github.com/aburdette/pyheap.git

Currently, you can import pyheap to a project by adding the folder and usign the line:

    from pyheap.refheap import *

Here's some copy/paste from working with pyheap in IDLE:

    >>> heap = Refheap('nyrd', 'a87ac957-a709-4c4b-9f40-ab3ce80b01db')
    >>> paste = heap.get(1)
    >>> print(paste)
    {u'language': u'Clojure', u'url': u'https://refheap.com/paste/1', u'lines': 1, u'private': False, u'user': u'raynes', u'date': u'2012-01-04T01:44:22.964Z', u'paste-id': u'1', u'contents': u'(begin)'}
    >>> print(paste['user'])
    raynes
    >>> paste = heap.create('Posted by pyheap!', True)
    >>> print(paste)
    {u'fork': None, u'language': u'Plain Text', u'url': u'https://refheap.com/paste/4f485a2ee4b0859a612220ab', u'lines': 1, u'private': True, u'user': u'nyrd', u'date': u'2012-02-25T03:49:02.056Z', u'paste-id': u'4f485a2ee4b0859a612220ab', u'contents': u'Posted by pyheap!'}
    >>> print(paste['user'])
    nyrd
    >>> paste = heap.edit(paste['paste-id'], 'PyHeap is awesome!')
    >>> print(paste['contents'])
    PyHeap is awesome!
    >>> heap.delete(paste['paste-id'])
    >>> 
