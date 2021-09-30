from django.db import models


class TimeStampedModel(models.Model):
    added = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    # class Fields:
    #     ADDED = 'added'
    #     EDITED = 'edited'
