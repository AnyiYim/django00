from oscar.apps.promotions.models import *  # noqa isort:skip
from django.db import models
from oscar.apps.promotions.models import Image


# 定制 promotioms 中 Image 模型
class MyImage(Image):
    detail = models.CharField(max_length=55)

# 必须尾部重新载入
from oscar.apps.promotions.models import *
