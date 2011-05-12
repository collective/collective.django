This package allows you to use the Django_ ORM within Plone_.

It takes care to merge Django transaction management within Zope's own
transaction manager.

Basic usage
===========

In order to use this package you must have a setup that looks like the following:

 1. Your settings module must be within buildout's "adjusted"
    ``sys.path``. This means it should be importable from within Plone, hence
    that it should be an egg (either released or more commonly in development).
    Jacob Kaplan-Moss explains how to do this for a `Django buildout`_.

 2. Your buildout should contain both the Plone parts and the Django parts
    together, hence the standard Plone buildouts plus the bits you see in
    Jacob's tutorial. Make sure that your plone instance has, within its eggs,
    the project one (``shorturls`` in Jacob's example) either derived from
    buildout's ones or local to the instance.

The second step is to make sure that your Plone instance has a special
environment variable that Django needs to know where its settings are. Hence
put, under your instance buildout section, something like this::

    [buildout]
    ...
    [instance]
    recipe = plone.recipe.zope2instance
    ...
    environment-vars =
        DJANGO_SETTINGS_MODULE shorturls.testsettings

Again values are borrowed from Jacob's post.

.. note:: Please note that this environment variable will be set only if you
          run ``bin/instance``. Therefore when using supervisord, make sure you
          have it run ``bin/instance console`` and not any ``run.py`` script
          directly which would completely bypass setting the environment
          variable and leave you in the mud.

Then just add the egg to your buildout, like this::

    [buildout]
    ...
    eggs =
        ...
        collective.django

The package itself relies on ``z3c.autoinclude`` to load its ZCML when Plone is
pulled up. In case this does not work, include a::

    <include package="collective.django" />

Within your package ZCML.

And whenever you will import your Django models from Plone, the transaction
will be managed by Zope.

Testing
=======

To run the tests, a minimal buildout is included. After checking out the source
code, run the following::

    $ python bootstrap.py
    $ bin/buildout
    $ bin/test

And the tests should be ran.

.. _Django: http://www.djangoproject.com/
.. _Plone: http://www.plone.org/
.. _`Django buildout`: http://jacobian.org/writing/django-apps-with-buildout/
