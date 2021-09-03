Examples (Web)
==============

twisted.web.client
------------------

- `httpclient.py` - use ``twisted.web.client.Agent`` to download a web page.
- (deprecated) `getpage.py` - use ``twisted.web.client.getPage`` to download a web page.
- (deprecated) `dlpage.py` - add callbacks to ``twisted.web.client.downloadPage`` to display errors that occur when downloading a web page


XML-RPC
-------

- `xmlrpcserver.py` XML-RPC server with several methods, including echoing, faulting, returning deferreds and failed deferreds
- `xmlrpcclient.py` - use ``twisted.web.xmlrpc.Proxy`` to call remote XML-RPC methods
- `xmlrpc-debug.py` - use ``xmlrpc.Proxy``'s ``queryFactory`` to debug raw XML-RPC traffic
- `advogato.py` - use ``twisted.web.xmlrpc`` to post a diary entry to advogato.org; requires an advogato account


Virtual hosts and proxies
-------------------------

- `proxy.py` - use ``twisted.web.proxy.Proxy`` to make the simplest proxy
- `logging-proxy.py` - example of subclassing the core classes of ``twisted.web.proxy`` to log requests through a proxy
- `reverse-proxy.py` - use ``twisted.web.proxy.ReverseProxyResource`` to make any HTTP request to the proxy port get applied to a specified website
- `rootscript.py` - example use of ``twisted.web.vhost.NameVirtualHost``
- `web.py` - an example of both using the ``processors`` attribute to set how certain file types are treated and using ``twisted.web.vhost.VHostMonsterResource`` to reverse proxy


.rpys and ResourceTemplate
--------------------------

- `hello.rpy` - use ``twisted.web.static`` to create a static resource to serve
- `fortune.rpy` - create a resource that returns the output of a process run on the server
- `report.rpy` - display various properties of a resource, including path, host, and port
- `users.rpy` - use ``twisted.web.distrib`` to publish user directories as for a "community web site"
- `simple.rtl` - example use of ``twisted.web.resource.ResourceTemplate``


Miscellaneous
-------------

- `webguard.py` - pairing ``twisted.web`` with ``twisted.cred`` to guard resources against unauthenticated users
- `silly-web.py` - bare-bones distributed web setup with a master and slave using ``twisted.web.distrib`` and ``twisted.spread.pb``
- `soap.py` - use ``twisted.web.soap`` to publish SOAP methods

.. contents:: Table Of Contents
