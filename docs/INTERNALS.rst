Basic schema
============

.. note:: The following schema is merely a draft, as far as my understanding of
          Django internals goes

Whenever a database operation is required, Django will fetch the
``DatabaseWrapper`` (subclass of ``django.db.backends.BaseDatabaseWrapper``)
and try to obtain a cursor.

This will check if there is a valid opened connection to use (initially, there
is none) and if there is not, a connection is created. When the connection is
created, a ``django.db.backends.signals.connection_created`` signal is
raised. This package puts a listener on that signal and, upon receiving it,
will obtain the current Zope transaction and iterate through all its extensions
to see if there is a transaction manager hooked in that has the same connection
as the one that was passed in.

If there is, a small check on whether the connection is still in managed mode
and hasn't lost its state is done. If the state was lost, it is restored.

If there isn't, a new extension is spawned and joined.

The real commit happens late on ``tpc_vote()``, as ``zope.sqlalchemy`` does (as
Django has no TPC support) and it is done, like rollback, only if the
connection is marked dirty.

If ``abort`` is invoked, the connection is also closed: as the datamanager will
be unjoined and therefore if new data happens, it will be rejoined because the
connection will be respawned.

The connection is also closed on ``__del__`` to make sure that the spawning of
a new connection will make it join the zope transaction (this is to avoid
having a zope transaction and a Django connection present in the same thread
but unlinked).
