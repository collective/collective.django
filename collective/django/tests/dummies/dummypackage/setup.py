from setuptools import setup, find_packages

version = '0.1'

setup(
    name = 'dummypackage',
    version = version,
    description = "Test package",
    long_description = "Test package",
    author = 'Antonio Escarrillo Jimenez',
    author_email = 'cardinal.jimenez@example.com',
    url = 'http://example.com/dummypackage',
    license = 'BSD',
    packages = find_packages(),
    include_package_data = True,
    zip_safe = False,
    install_requires = [
        'distribute',
        'Django'
    ]
)
