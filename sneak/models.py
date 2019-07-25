from __future__ import unicode_literals

from django.db import models


class SneakModel(models.Model):
    class Meta:
        abstract = True
