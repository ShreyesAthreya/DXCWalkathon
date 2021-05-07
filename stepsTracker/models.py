from decimal import Decimal

from django.conf import settings
from django.core.validators import MinValueValidator
from django.db import models

# Create your models here.
from django.urls import reverse


class Step(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    steps: float = models.DecimalField(default=0, max_digits=10, decimal_places=0)
    week1: float = models.DecimalField(
        blank=True,
        null=True,
        default=0,
        max_digits=8,
        decimal_places=0,
        validators=[MinValueValidator(Decimal("0"))],
    )
    week2: float = models.DecimalField(
        blank=True,
        null=True,
        default=0,
        max_digits=8,
        decimal_places=0,
        validators=[MinValueValidator(Decimal("0"))],
    )
    week3: float = models.DecimalField(
        blank=True,
        null=True,
        default=0,
        max_digits=8,
        decimal_places=0,
        validators=[MinValueValidator(Decimal("0"))],
    )
    week4: float = models.DecimalField(
        blank=True,
        null=True,
        default=0,
        max_digits=8,
        decimal_places=0,
        validators=[MinValueValidator(Decimal("0"))],
    )

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse("view-steps", args=[str(self.id)])

    def save(self, *args, **kwargs):
        self.steps = self.week1 + self.week2 + self.week3 + self.week4
        super().save(*args, **kwargs)
