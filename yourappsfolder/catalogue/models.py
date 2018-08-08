# from oscar.apps.catalogue.models import *  # noqa isort:skip
from django.db import models

from oscar.apps.catalogue.abstract_models import AbstractProduct


class Product(AbstractProduct):
    video_url = models.URLField()

# 第一个得注释掉 不然出现重复导入错误
from oscar.apps.catalogue.models import *