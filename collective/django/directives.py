from zope.interface import Interface
from zope.configuration.fields import GlobalObject
from zope.configuration.exceptions import ConfigurationError
from zope.i18nmessageid import MessageFactory

_ = MessageFactory('collective.django')


class IInitialize(Interface):

    component = GlobalObject(
        title = _(u"Initializer"),
        description = _(u"The callable that performs some Django initialization"),
        required = True
    )


def initialize(_context, component):
    if not callable(component):
        raise ConfigurationError("'component' should be callable")
    _context.action(
        discriminator = "%s.%s" % (component.__module__, component.__name__),
        callable = component,
        args = ()
    )
