import os
from setuptools import setup, find_packages

def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

version = '0.1'

long_description = read('README.rst') + "\n" + \
                   read('docs', 'CHANGELOG.rst') + \
                   read('docs', 'CONTRIBUTORS.rst')

setup(
    name = 'collective.django',
    version = version,
    description = "Django transaction integration for Plone",
    long_description = long_description,
    # Get more strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers = [
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Plone',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License'
    ],
    keywords = '',
    author = 'Simone Deponti',
    author_email = 'simone.deponti@abstract.it',
    url = 'http://github.com/collective/collective.django',
    license = 'BSD',
    packages = find_packages(exclude=['bootstrap']),
    namespace_packages = ['collective'],
    include_package_data = True,
    zip_safe = False,
    install_requires = [
        'setuptools',
        'distribute',
        'Django',
        'zope.interface',
        'transaction',
        'zope.configuration',
        'zope.i18nmessageid'
    ],
    extras_require = {
        'test': [
            'unittest2',
            'plone.testing [zca]'
        ]
    },
    entry_points = {
        'z3c.autoinclude.plugin': ['target = plone']
    }
)
