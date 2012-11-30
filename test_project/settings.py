#!/usr/bin/env python
# -*- coding: utf-8 -*-

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'test.db',
    }
}

SITE_ID = 1
ROOT_URLCONF = 'test_project.urls'

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'djgotuskra',
)

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
NOSE_ARGS = ['djgotuskra',
    '--failed',
    '--stop',
    #'--with-coverage',
    '--cover-erase',
    '--cover-package=djgotuskra',
    '--cover-tests',
    '--with-xcoverage',
    '--with-xunit',
]
