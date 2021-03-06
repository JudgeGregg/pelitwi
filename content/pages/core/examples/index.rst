Examples (Core)
===============

Simple Echo server and client
-----------------------------

- `simpleclient.py` - simple TCP client
- `simpleserv.py` - simple TCP echo server


Chat
----

- `chatserver.py` - shows how to communicate between clients


Echo server & client variants
-----------------------------

- `echoserv.py` - variant on a simple TCP echo server
- `echoclient.py` - variant on a simple TCP client
- `echoserv_udp.py` - simplest possible UDP server
- `echoclient_udp.py` - simple UDP client
- `echoserv_ssl.py` - simple SSL server
- `echoclient_ssl.py` - simple SSL client


AMP server & client variants
----------------------------

- `ampserver.py` - do math using AMP
- `ampclient.py` - do math using AMP


Perspective Broker
------------------

- `pbsimple.py` - simplest possible PB server
- `pbsimpleclient.py` - simplest possible PB client
- `pbbenchclient.py` - benchmarking client
- `pbbenchserver.py` - benchmarking server
- `pbecho.py` - echo server that uses login
- `pbechoclient.py` - echo client using login
- `pb_exceptions.py` - example of exceptions over PB
- `pbgtk2.py` - example of using GTK2 with PB
- `pbinterop.py` - shows off various types supported by PB
- `bananabench.py` - benchmark for banana


Cred
----

- `cred.py` - Authenticate a user with an in-memory username/password database
- `dbcred.py` - Using a database backend to authenticate a user


GUI
---

- `wxdemo.py` - demo of wxPython integration with Twisted
- `pbgtk2.py` - example of using GTK2 with PB
- `pyuidemo.py` - PyUI


FTP examples
------------

- `ftpclient.py` - example of using the FTP client
- `ftpserver.py` - create an FTP server which serves files for anonymous users from the working directory and serves files for authenticated users from ``/home``.


Logging
-------

- `twistd-logging.tac` - logging example using ILogObserver
- `testlogging.py` - use twisted.python.log to log errors to standard out
- `rotatinglog.py` - example of log file rotation


POSIX Specific Tricks
---------------------

- `sendfd.py`, `recvfd.py` - send and receive file descriptors over UNIX domain sockets


Miscellaneous
-------------

- `shaper.py` - example of rate-limiting your web server
- `stdiodemo.py` - example using stdio, Deferreds, LineReceiver and twisted.web.client.
- `ptyserv.py` - serve shells in pseudo-terminals over TCP
- `courier.py` - example of interfacing to Courier's mail filter interface
- `longex.py` - example of doing arbitrarily long calculations nicely in Twisted
- `longex2.py` - using generators to do long calculations
- `stdin.py` - reading a line at a time from standard input without blocking the reactor
- `streaming.py` - example of a push producer/consumer system
- `filewatch.py` - write the content of a file to standard out one line at a time
- `shoutcast.py` - example Shoutcast client
- `wxacceptance.py` - acceptance tests for wxreactor
- `postfix.py` - test application for PostfixTCPMapServer
- `udpbroadcast.py` - broadcasting using UDP
- `tls_alpn_npn_client.py` - example of TLS next-protocol negotiation on the client side using NPN and ALPN.
- `tls_alpn_npn_server.py` - example of TLS next-protocol negotiation on the server side using NPN and ALPN.

.. contents:: Table Of Contents
