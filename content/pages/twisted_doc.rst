Twisted Matrix Labs (Demo Site)
-------------------------------

What is Twisted?
~~~~~~~~~~~~~~~~

Twisted is an event-driven networking engine written in Python and licensed under the open source ​MIT license. It supports CPython 3.6+ and PyPy3. 

Get Started with Pip
~~~~~~~~~~~~~~~~~~~~

.. code-block:: shell

    $ python -m venv try-twisted
    $ . try-twisted/bin/activate
    $ pip install twisted[tls]
    $ twist --help

Code Example
~~~~~~~~~~~~

Twisted includes an event-driven web server.
Here's a sample web application;
notice how the resource object persists in memory,
rather than being recreated on each request: 

.. code-block:: python


    from twisted.web import server, resource
    from twisted.internet import reactor, endpoints

    class Counter(resource.Resource):
        isLeaf = True
        numberRequests = 0

        def render_GET(self, request):
            self.numberRequests += 1
            request.setHeader(b"content-type", b"text/plain")
            content = u"I am request #{}\n".format(self.numberRequests)
            return content.encode("ascii")

    endpoints.serverFromString(reactor, "tcp:8080").listen(server.Site(Counter()))
    reactor.run()

See `Code Examples <{filename}/pages/code-examples.rst>`_.
