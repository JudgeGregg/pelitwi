Developer Guides (Core)
=======================

- .. _core-howto-index-introduction:

  Introduction

  - `Executive summary <{filename}vision.rst>`_

    Connecting your software - and having fun too!


- .. _core-howto-index-tutorials:

  Getting Started

  - `Writing a TCP server <{filename}servers.rst>`_

    Basic network servers with Twisted.
  - `Writing a TCP client <{filename}clients.rst>`_

    And basic clients.
  - `Test-driven development with Twisted <{filename}trial.rst>`_

    Code without tests is broken by definition; Twisted makes it easy to test your network code.
  - `Tutorial: Twisted From Scratch <{filename}tutorial/index.rst>`_

    #. `The Evolution of Finger: building a simple finger service <{filename}tutorial/intro.rst>`_
    #. `The Evolution of Finger: adding features to the finger service <{filename}tutorial/protocol.rst>`_
    #. `The Evolution of Finger: cleaning up the finger code <{filename}tutorial/style.rst>`_
    #. `The Evolution of Finger: moving to a component based architecture <{filename}tutorial/components.rst>`_
    #. `The Evolution of Finger: pluggable backends <{filename}tutorial/backends.rst>`_
    #. `The Evolution of Finger: a clean web frontend <{filename}tutorial/web.rst>`_
    #. `The Evolution of Finger: Twisted client support using Perspective Broker <{filename}tutorial/pb.rst>`_
    #. `The Evolution of Finger: using a single factory for multiple protocols <{filename}tutorial/factory.rst>`_
    #. `The Evolution of Finger: a Twisted finger client <{filename}tutorial/client.rst>`_
    #. `The Evolution of Finger: making a finger library <{filename}tutorial/library.rst>`_
    #. `The Evolution of Finger: configuration and packaging of the finger service <{filename}tutorial/configuration.rst>`_

  - `Setting up the TwistedQuotes application <{filename}quotes.rst>`_
  - `Designing a Twisted application <{filename}design.rst>`_



- .. _core-howto-index-events:

  Networking and Other Event Sources

  - `Twisted Internet <{filename}internet-overview.rst>`_

    A brief overview of the ``twisted.internet`` package.
  - `Reactor basics <{filename}reactor-basics.rst>`_

    The event loop at the core of your program.
  - `Using SSL in Twisted <{filename}ssl.rst>`_

    Add some security to your network transport.
  - `UDP Networking <{filename}udp.rst>`_

    How to use Twisted's UDP implementation, including multicast and broadcast functionality.
  - `Using processes <{filename}process.rst>`_

    Launching sub-processes, the correct way.
  - `Introduction to Deferreds <{filename}defer-intro.rst>`_

    Like callback functions, only a lot better.
  - `Deferred reference <{filename}defer.rst>`_

    In-depth information on Deferreds.
  - `Generating deferreds <{filename}gendefer.rst>`_

    More about Deferreds.
  - `Scheduling <{filename}time.rst>`_

    Timeouts, repeated events, and more: when you want things to happen later.
  - `Using threads <{filename}threading.rst>`_

    Running code in threads, and interacting with Twisted in a thread-safe manner.
  - `Producers and Consumers: Efficient High-Volume Streaming <{filename}producers.rst>`_

    How to pause when buffers fill up.
  - `Choosing a reactor and GUI toolkit integration <{filename}choosing-reactor.rst>`_

    GTK+, Windows, epoll() and more: use your GUI of choice, or a faster event loop.


- .. _core-howto-index-highlevel:

  High-Level Infrastructure

  - `Getting Connected with Endpoints <{filename}endpoints.rst>`_

    Create configurable applications that support multiple transports (e.g. TCP and SSL).
  - `Interfaces and Adapters (Component Architecture) <{filename}components.rst>`_

    When inheritance isn't enough.
  - `Cred: Pluggable Authentication <{filename}cred.rst>`_

    Implementing authentication and authorization that is configurable, pluggable and re-usable.
  - `Twisted's plugin architecture <{filename}plugin.rst>`_

    A generic plugin system for extendable programs.


- .. _core-howto-index-deploying:

  Deploying Twisted Applications

  - `Helper programs and scripts (twistd, ..) <{filename}basics.rst>`_

    ``twistd`` lets you daemonize and run your application.
  - `Using the Twisted Application Framework <{filename}application.rst>`_

    Writing code that ``twistd`` can run.
  - `Writing Twisted Application Plugins for twistd <{filename}tap.rst>`_

    More powerful ``twistd`` deployment method.
  - `Deploying Twisted with systemd <{filename}systemd.rst>`_

    Use ``systemd`` to launch and monitor Twisted applications.


- .. _core-howto-index-utilities:

  Utilities

  - `Emitting and Observing Logs <{filename}logger.rst>`_

    Keep a record of what your application is up to, and inspect that record to discover interesting information.
    (You may also be interested in the `legacy logging system <{filename}logging.rst>`_ if you are maintaining code written to work with older versions of Twisted.)

  - `Symbolic constants <{filename}constants.rst>`_

    enum-like constants. (Deprecated, spun out into `Constantly <http://constantly.readthedocs.org/en/latest/>`_)

  - `Twisted RDBMS support with adbapi <{filename}rdbms.rst>`_

    Using SQL with your relational database via DB-API adapters.
  - `Parsing command-line arguments <{filename}options.rst>`_

    The command-line argument parsing used by ``twistd`` .
  - `Using Dirdbm: Directory-based Storage <{filename}dirdbm.rst>`_

    A simplistic way to store data on your filesystem.
  - `Tips for writing tests for Twisted code using Trial <{filename}testing.rst>`_

    More information on writing tests.
  - `Extremely Low-Level Socket Operations <{filename}sendmsg.rst>`_

    Using wrappers for sendmsg(2) and recvmsg(2).

- .. _core-howto-index-amp:

  Asynchronous Messaging Protocol (AMP)

  - `Asynchronous Messaging Protocol Overview <{filename}amp.rst>`_

    A two-way asynchronous message passing protocol, for when HTTP isn't good enough.


- .. _core-howto-index-pb:

  Perspective Broker

  - `Twisted Spread <{filename}pb.rst>`_

    A remote method invocation (RMI) protocol: call methods on remote objects.
  - `Introduction to Perspective Broker <{filename}pb-intro.rst>`_
  - `Using Perspective Broker <{filename}pb-usage.rst>`_
  - `Managing Clients of Perspectives <{filename}pb-clients.rst>`_
  - `Passing Complex Types <{filename}pb-copyable.rst>`_
  - `Authentication with Perspective Broker <{filename}pb-cred.rst>`_
  - `PB Limits <{filename}pb-limits.rst>`_


- .. _core-howto-index-positioning:

  Positioning

  - `Twisted Positioning <{filename}positioning.rst>`_


- .. _core-howto-index-appendix:

  Appendix








  - `Porting to Python 3 <{filename}python3.rst>`_
  - `Glossary <{filename}glossary.rst>`_
  - `Tips for debugging with emacs <{filename}debug-with-emacs.rst>`_

.. contents:: Table Of Contents
