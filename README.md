# pyheap

pyheap is a Python implementation of the [RefHeap](https://refheap.com) API. It was originally created as a Python learning project for myself, but still continues to be tweaked and improved.

## Setup

You can obtain the pyheap source through [GitHub](https://github.com/aburdette/pyheap):

    git clone git://github.com/aburdette/pyheap.git
  
## Usage

Add the pyheap folder to your project and import `refheap`:

    from pyheap import refheap
  
From there, you can instantiate a `Paste` object, optionally passing in _username_ and _api-token_ (**Note:** username and token are required for some API calls):

    p = refheap.Paste('username', 'token')
  
API calls are made through this new `Paste` object. A tuple containing the web service response and the content is returned. Here is some copy/paste from IDLE showing some basic usage:

    >>> p = Paste('username', 'api-token')
    >>> resp = p.get(1)
    >>> print(resp[0]['status'])
    200
    >>> print(resp[1]['contents'])
    (begin)
    >>> resp = p.create('This is a new private paste.', True)
    >>> print(resp[0]['status'])
    201
    >>> print(resp[1]['private'])
    True
    >>> print(resp[1]['contents'])
    This is a new private paste.
    >>> resp = p.delete(resp[1]['paste-id'])
    >>> print(resp[0]['status'])
    204
  
## License

Copyright © 2012 Andre Burdette

Distributed under the [Eclipse Public License](http://www.eclipse.org/legal/epl-v10.html), same as RefHeap.

