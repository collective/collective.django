from plone.testing import Layer, zca
from zope.configuration import xmlconfig

# The following two lines shall go when zc.recipe.testrunner is updated
import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'dummyproject.settings'


class DjangoLayer(Layer):
    defaultBases = (zca.ZCML_DIRECTIVES,)

    def setUp(self):
        import collective.django
        self['configurationContext'] = context = zca.pushConfigurationContext(
            self.get('configurationContext')
        )
        xmlconfig.file('configure.zcml', collective.django, context=context)

    def testSetUp(self):
        from django.db import connection
        from django.core.management.commands.syncdb import Command as SyncDB
        syncdb = SyncDB()
        syncdb.handle()
        connection.cursor()

    def testTearDown(self):
        from django.db import connection
        # This is due to Django being idiotic
        connection.connection.close()
        connection.connection = None

    def tearDown(self):
        zca.popConfigurationContext()
        del self['configurationContext']


DJANGO_LAYER = DjangoLayer()
