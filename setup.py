import os
from setuptools import setup, find_packages

base_path= os.path.abspath(os.path.dirname(__file__))
readme_path= os.path.join(base_path, 'README.rst')

setup(
    name='django-debug-toolbar',
    version=__import__('debug_toolbar').__version__,
    description='A configurable set of panels that display various debug information about the current request/response.',
    long_description=open(readme_path).read(),
    # Get more strings from http://www.python.org/pypi?:action=list_classifiers
    author='Rob Hudson',
    author_email='rob@cogit8.org',
    url='https://github.com/django-debug-toolbar/django-debug-toolbar',
    download_url='https://github.com/django-debug-toolbar/django-debug-toolbar/downloads',
    license='BSD',
    packages=find_packages(exclude=['ez_setup']),
    tests_require=[
        'django',
        'dingus',
    ],
    test_suite='debug_toolbar.runtests.runtests',
    include_package_data=True,
    zip_safe=False, # because we're including media that Django needs
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
