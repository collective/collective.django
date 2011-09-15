import logging

from zope.interface import implements
from transaction.interfaces import ISavepointDataManager, IDataManagerSavepoint
from transaction import manager

import os
if 'DJANGO_SETTINGS_MODULE' not in os.environ:
    DJANGO_ENABLED = False
    logging.info("No DJANGO_SETTINGS_MODULE found. " + \
                      "Skipping configuration")
else:
    from django.db.backends.signals import connection_created
    from django.db import connections
    DJANGO_ENABLED = True


# BBB: we might want to commit them?
class DjangoDataSavePoint(object):
    implements(IDataManagerSavepoint)

    def __init__(self, connection):
        self.connection = connection
        try:
            self.sid = self.connection.savepoint()
        except:
            logging.exception("Error creating savepoint")
            self.sid = None
            self.valid = False
        else:
            self.valid = True

    def rollback(self):
        if self.valid:
            self.connection.savepoint_rollback(self.sid)


class DjangoDataManager(object):
    implements(ISavepointDataManager)

    def __init__(self, transaction_manager, connection):
        self.transaction_manager = transaction_manager
        self.connection = connection
        self.savepoints = []
        self.django_t_begin()

    def django_t_begin(self):
        if not self.connection.is_managed():
            self.connection.enter_transaction_management()
            self.connection.managed(True)

    def abort(self, transaction):
        self.tpc_abort(transaction)
        self.connection.close()

    def tpc_begin(self, transaction):
        pass

    def commit(self, transaction):
        assert self.connection is not None
        assert self.connection.is_managed()

    def tpc_vote(self, transaction):
        if self.connection.is_dirty():
            self.connection.commit()

    def tpc_finish(self, transaction):
        self.connection.set_clean()

    def tpc_abort(self, transaction):
        if self.connection.is_dirty():
            self.connection.rollback()
        self.connection.set_clean()

    def sortKey(self):
        try:
            return "~django:%d" % self.connection.alias
        except:
            return "~django:%s" % self.connection.alias

    def savepoint(self):
        return DjangoDataSavePoint(self.connection)

    def __del__(self):
        if self.connection:
            self.connection.close()


def link(signal, sender, connection, **kwargs):
    """Whenever a connection is created, we link it to the Zope session,
    basically turning on transaction management at Django level and then
    joining in with the Zope one
    """
    txn = manager.get()
    for dm in txn._resources:
        if isinstance(dm, DjangoDataManager) and \
                dm.connection == connection:
            dm.django_t_begin()
            return
    dm = DjangoDataManager(manager, connection)
    txn.join(dm)


def attach_signals():
    if not DJANGO_ENABLED:
        return
    global link
    connection_created.connect(link)
    # Link all connections that might have popped up while we were
    # loading. This will happen for sure if django-livesettings is installed as
    # importing settings will automagically open a connection to the default
    # database.
    for conn in connections.all():
        if conn.connection is not None:
            link(conn.__class__, conn)
