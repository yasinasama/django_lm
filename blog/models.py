from django.db import models


class Artical(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    createtime = models.DateField(auto_now_add=True)