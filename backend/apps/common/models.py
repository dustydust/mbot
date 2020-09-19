import uuid

from django.conf import settings
from django.db import models


class UUIDMixin(models.Model):
    uuid = models.UUIDField(primary_key=False, default=uuid.uuid4, editable=False, unique=True)

    class Meta:
        abstract = True

    def __str__(self):
        return f"{self.uuid}"


class BaseModelMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def _get_orig(self):
        created = True if not self.pk else False
        orig = None
        if not created:
            orig = self.__class__.objects.get(pk=self.pk)

        return orig

    def __repr__(self):
        return f"{self.__class__.__name__} object {self.pk}"


class BaseUUIDModel(BaseModelMixin, UUIDMixin):
    class Meta:
        abstract = True

    def natural_key(self):
        return str(self.uuid)
