#!/usr/bin/env python
# -*- coding: utf-8 -*-

from paver.easy import * # noqa

NAME = "djgotuskra"
PYCOMPILE_CACHES = ["*.pyc", "*$py.class"]


@task
@cmdopts([
    ("noerror", "E", "Ignore errors"),
])
def pep8(options):
    noerror = getattr(options, "noerror", False)
    return sh("""find %s -name "*.py" | xargs pep8 | perl -nle'\
            print; $a=1 if $_}{exit($a)'""" % NAME, ignore_error=noerror)


@task
@cmdopts([
    ("noerror", "E", "Ignore errors"),
])
def flake8(options):
    noerror = getattr(options, "noerror", False)
    sh("flake8 %s" % NAME, ignore_error=noerror)


@task
def removepyc(options):
    sh("find . -type f -a \\( %s \\) | xargs rm" % (
        " -o ".join("-name '%s'" % (pat, ) for pat in PYCOMPILE_CACHES), ))