from django.conf import settings
from django.db import models


class HomePage(models.Model):
    "Generated Model"
    texas = models.TextField(
        blank=True,
    )


class CustomText(models.Model):
    "Generated Model"
    albama = models.CharField(
        max_length=150,
        blank=True,
    )
