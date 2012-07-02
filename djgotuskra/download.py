#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
djgotuskra.download
~~~~~~~~~~~~~~~~~~~
"""
from __future__ import absolute_import

import itertools
import requests

from .models import Postnumer, Street


def download_file(url):
    """
    Downloads the file and splits the csv file.
    """
    return (i.split(';') for i in
        requests.get(url).text.splitlines()[1:])


def download_postcodes():
    """
    Downloads the Postnumer objects
    """
    url = 'http://www.postur.is/gogn/Gotuskra/postnumer.txt'
    for code, place, address in download_file(url):
        yield Postnumer(code=int(code), place=place, address=address)


def download_streets():
    """
    Downloads the Street objects
    """
    url = 'http://www.postur.is/gogn/Gotuskra/gotuskra.txt'

    #lookup dictionary to speed things up a bit.
    pnr_dict = dict((i.code, i) for i in Postnumer.objects.all())

    for id, pnr, heiti_nf, heiti_thfg in download_file(url):
        yield Street(id=int(id), postnumer=pnr_dict[int(pnr)],
            heiti_nf=heiti_nf, heiti_thfg=heiti_thfg)


def fill_database():
    """
    Downloads the Postnumer and Street name csv files and
    bootstraps the database.
    """

    #Batch the call to bulk_create in case our database has trouble
    #consuming a lot of records at the same time.
    def batch(n, iterable):
        args = [iter(iterable)] * n
        return itertools.izip_longest(*args)

    Postnumer.objects.bulk_create(download_postcodes())
    for b in batch(200, download_streets()):
        Street.objects.bulk_create((i for i in b if i))
