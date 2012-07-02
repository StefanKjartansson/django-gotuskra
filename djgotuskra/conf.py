#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
djgotuskra.conf
~~~~~~~~~~~~~~~
"""
from __future__ import absolute_import

from django.conf import settings  # noqa
from appconf import AppConf


class GotuskraConf(AppConf):
    PNR_URL = 'http://www.postur.is/gogn/Gotuskra/postnumer.txt'
    URL = 'http://www.postur.is/gogn/Gotuskra/gotuskra.txt'

    class Meta:
        prefix = 'gotuskra'
