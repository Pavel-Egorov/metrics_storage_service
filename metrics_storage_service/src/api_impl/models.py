from decimal import Decimal

from django.core.validators import MinValueValidator
from django.db import models

MAX_LENGTH = 255


class AdvertisementMetric(models.Model):
    metric_date = models.DateField()

    channel = models.CharField(max_length=MAX_LENGTH, null=True, blank=True)
    country = models.CharField(max_length=MAX_LENGTH, null=True, blank=True)
    operating_system = models.CharField(max_length=MAX_LENGTH, null=True, blank=True)

    impressions_count = models.PositiveIntegerField(null=True, blank=True)
    clicks_count = models.PositiveIntegerField(null=True, blank=True)
    installations_count = models.PositiveIntegerField(null=True, blank=True)

    spend_money = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True, validators=[MinValueValidator(Decimal('0.0'))],
    )
    revenue = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True, validators=[MinValueValidator(Decimal('0.0'))],
    )
    cpi = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
        editable=False,
        validators=[MinValueValidator(Decimal('0.0'))],
    )

    def save(self, *args, **kwargs):
        if self.spend_money is not None and self.installations_count is not None:
            self.cpi = Decimal(self.spend_money / self.installations_count)
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['-metric_date']

    def __str__(self):
        return f'{self.metric_date}: {self.channel} in {self.country} from {self.operating_system} OS'
