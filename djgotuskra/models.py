#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
djgotuskra.models
~~~~~~~~~~~~~~~~~
"""
from __future__ import absolute_import

import operator

from django.db import models
from django.db.models.query import QuerySet
from django.utils.translation import ugettext as _
from django.db.models import Q

from model_utils.managers import PassThroughManager


REYKJAVIK = Q(code__range=(101, 155))
SELTJARNARNES = Q(code__range=(170, 172))
KOPAVOGUR = Q(code__range=(200, 203))
GARDABAER = Q(code__range=(210, 212))
HAFNARFJORDUR = Q(code__range=(220, 222))
ALFTANES = Q(code=225)
MOSFELLSBAER = Q(code__range=(270, 276))


class PostnumerQuerySet(QuerySet):

    def reykjavik(self):
        return self.filter(REYKJAVIK)

    def seltjarnarnes(self):
        return self.filter(SELTJARNARNES)

    def kopavogur(self):
        return self.filter(KOPAVOGUR)

    def gardabaer(self):
        return self.filter(GARDABAER)

    def hafnarfjordur(self):
        return self.filter(HAFNARFJORDUR)

    def alftanes(self):
        return self.filter(ALFTANES)

    def mosfellsbaer(self):
        return self.filter(MOSFELLSBAER)

    def capital_area(self):
        return self.filter(reduce(operator.or_, (
            REYKJAVIK, SELTJARNARNES, KOPAVOGUR,
            GARDABAER, HAFNARFJORDUR, ALFTANES,
            MOSFELLSBAER,
        )))


class Postnumer(models.Model):
    code = models.IntegerField(primary_key=True, db_index=True)
    place = models.CharField(max_length=64, db_index=True)
    address = models.CharField(max_length=128)

    class Meta:
        db_table = 'postnumer'

    def __unicode__(self):
        return u'<Postnumer: %d - %s - %s>' % (self.code,
            self.place, self.address)

    objects = PassThroughManager.for_queryset_class(PostnumerQuerySet)()

    @property
    def streets(self):
        return Street.objects.filter(postnumer=self)


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
