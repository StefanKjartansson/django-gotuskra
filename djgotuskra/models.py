#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
djgotuskra.models
~~~~~~~~~~~~~~~~~
"""
from __future__ import absolute_import

from django.db import models


class Postnumer(models.Model):
    code = models.IntegerField(primary_key=True, db_index=True)
    place = models.CharField(max_length=64, db_index=True)
    address = models.CharField(max_length=128)

    class Meta:
        db_table = 'postnumer'

    def __unicode__(self):
        return u'<Postnumer: %d - %s - %s>' % (self.code,
            self.place, self.address)


class Street(models.Model):
    id = models.IntegerField(primary_key=True, db_index=True)
    postnumer = models.ForeignKey(Postnumer)
    heiti_nf = models.CharField(max_length=64, db_index=True)
    heiti_thfg = models.CharField(max_length=64, db_index=True)

    class Meta:
        db_table = 'gotuskra'

    def __unicode__(self):
        return u'<Street: %d - %d - %s - %s>' % (self.id,
            self.postnumer.code, self.heiti_nf, self.heiti_thfg)
