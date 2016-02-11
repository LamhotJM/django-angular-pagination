from __future__ import unicode_literals

from django.db import models
import datetime
# Create your models here.


class State(models.Model):
    title = models.CharField(
        max_length=255, blank=True, null=True, db_index=True)
    created_at = models.DateTimeField(editable=False, null=True)
    modified_at = models.DateTimeField(editable=False, null=True)

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created_at = datetime.datetime.today()

        self.modified_at = datetime.datetime.today()
        return super(State, self).save(*args, **kwargs)
