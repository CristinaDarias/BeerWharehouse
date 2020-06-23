from django.conf import settings
from django.db import models
from django.utils.timezone import now


class CommonInfo(models.Model):
    created_at = models.DateTimeField("Created at", default=now, blank=True)
    last_modified = models.DateTimeField("Last modified at", default=now, blank=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, "Created by", blank=True, null=True, on_delete=models.DO_NOTHING)
    last_modified_by = models.ForeignKey(settings.AUTH_USER_MODEL, "Last Modified by", blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.created_at:
            self.created_at = now()

        self.last_modified_at = now()
        super(CommonInfo, self).save(*args, **kwargs)

    class Meta:
        abstract = True