#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
djgotuskra.management
~~~~~~~~~~~~~~~~~~~~~
"""
from __future__ import absolute_import

from django.db.models.signals import post_syncdb

from .. import models
from ..download import fill_database


def initial_fill(sender, **kwargs):
    #Hack
    if models.Postnumer.objects.all().count() == 0:
        fill_database()


post_syncdb.connect(initial_fill, sender=models)
