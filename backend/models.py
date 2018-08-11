from django.db import models
# # 代码高亮
# from pygments.lexers import get_all_lexers
# from pygments.styles import get_all_styles

# Create your models here.
#
# # 代码高亮的配置
# LEXERS = [item for item in get_all_lexers() if item[1]]
# LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
# STYLE_CHOICES = sorted((item, item) for item in get_all_styles())


class Person(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    #
    # def __str__(self):
    #         return self.name

