from setuptools import setup, find_packages

version = '0.1'

setup(
    name = 'dummyproject',
    version = version,
    description = "Test project",
    long_description = "Test project",
    author = 'Antonio Escarrillo Jimenez',
    author_email = 'cardinal.jimenez@example.com',
    url = 'http://example.com/dummyproject',
    license = 'BSD',
    packages = find_packages(),
    include_package_data = True,
    zip_safe = False,
    install_requires = [
        'distribute',
        'Django'
    ]
)
