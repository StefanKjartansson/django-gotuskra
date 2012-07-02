#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
djgotuskra.test
~~~~~~~~~~~~~~~
"""
from __future__ import absolute_import

from django.utils import unittest

from .models import Postnumer, Street


class PostnumerTestCase(unittest.TestCase):

    def test_initial_fill(self):
        self.assertTrue(Postnumer.objects.all().count() > 1)
        self.assertTrue(Street.objects.all().count() > 1)

        pnr = Postnumer.objects.get(code=101)
        self.assertIsNotNone(unicode(pnr))

        self.assertIn(pnr, Postnumer.objects.reykjavik())

        self.assertTrue(Postnumer.objects.capital_area().count() > 1)
        self.assertTrue(Postnumer.objects.seltjarnarnes().count() > 1)
        self.assertTrue(Postnumer.objects.kopavogur().count() > 1)
        self.assertTrue(Postnumer.objects.gardabaer().count() > 1)
        self.assertTrue(Postnumer.objects.hafnarfjordur().count() > 1)
        self.assertTrue(Postnumer.objects.alftanes().count() == 1)
        self.assertTrue(Postnumer.objects.mosfellsbaer().count() > 1)

        self.assertIn(
            Postnumer.objects.get(code=200),
            Postnumer.objects.capital_area())

        bs = Street.objects.get(heiti_nf=u'Barónsstígur')
        self.assertIn(bs, pnr.streets)
        self.assertIsNotNone(unicode(bs))
