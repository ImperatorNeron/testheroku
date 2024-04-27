from django.db import models


class TestModel(models.Model):
    name = models.CharField(max_length=100, verbose_name="Name")
    photo = models.ImageField(upload_to="test", verbose_name="Image")
