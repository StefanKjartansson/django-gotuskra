===============
Django Gotuskra
===============

.. image:: https://secure.travis-ci.org/StefanKjartansson/django-gotuskra.png?branch=master
        :target: https://secure.travis-ci.org/StefanKjartansson/django-gotuskra

**Django Gotuskra** is a pluggable application for the `Django Web Framework`_
providing Icelandic post codes and street names. Downloads and bootstraps
the database tables using csv files from the Icelandic post office.

Project page
    https://github.com/StefanKjartansson/django-gotuskra

.. _`Django Web Framework`: http://www.djangoproject.com


Installing & Setup
==================

**Django Gotuskra** is in the `Python Package Index (PyPI)`_ and you can easily install
the latest stable version of it using the tools ``pip`` or
``easy_install``. Try::

  pip install django-gotuskra

or::

  easy_install django-gotuskra

.. _`Python Package Index (PyPI)`: http://pypi.python.org


Alternatively, you can install **Django Gotuskra** from source code running the follow
command on directory that contains the file ``setup.py``::

  python setup.py install

After installation you need configure your project to recognize the application
by adding ``'djgotuskra'`` to your ``INSTALLED_APPS`` setting and running syncdb.
