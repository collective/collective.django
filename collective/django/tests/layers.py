from plone.testing import Layer, zca
from zope.comfiguration import xmlconfig


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
        connection.cursor()

    def testTearDown(self):
        from django.db import connection
        connection.close()

    def tearDown(self):
        zca.popConfigurationContext()
        del self['configurationContext']


DJANGO_LAYER = DjangoLayer()
