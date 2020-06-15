from django.db import models
from django.contrib.postgres.fields import JSONField


class Paragraphs(models.Model):
    text = models.TextField()
    document = models.CharField(max_length=128)
    company = models.CharField(max_length=128, db_index=True)
    region = models.CharField(max_length=128, db_index=True, null=True)
    year = models.IntegerField(db_index=True, null=True)
    report_type = models.CharField(max_length=128, db_index=True, null=True)
    URL = models.CharField(max_length=512, null=True)
    vector = JSONField()