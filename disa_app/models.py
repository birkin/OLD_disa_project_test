# -*- coding: utf-8 -*-

import datetime, json, logging, os, pprint
from django.conf import settings as project_settings
from django.core.urlresolvers import reverse
from django.db import models
from django.http import HttpResponseRedirect

log = logging.getLogger(__name__)


class Person(models.Model):
    created = models.DateTimeField( auto_now_add=True )
    modified = models.DateTimeField( auto_now=True )
    display_name = models.CharField( max_length=190, default='' )





