from decimal import Decimal

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='AdvertisementMetric',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('metric_date', models.DateField()),
                ('channel', models.CharField(blank=True, max_length=255, null=True)),
                ('country', models.CharField(blank=True, max_length=255, null=True)),
                ('operating_system', models.CharField(blank=True, max_length=255, null=True)),
                ('impressions_count', models.PositiveIntegerField(blank=True, null=True)),
                ('clicks_count', models.PositiveIntegerField(blank=True, null=True)),
                ('installations_count', models.PositiveIntegerField(blank=True, null=True)),
                ('spend_money', models.DecimalField(
                    blank=True,
                    decimal_places=2,
                    max_digits=10,
                    null=True,
                    validators=[django.core.validators.MinValueValidator(Decimal('0.0'))]
                )),
                ('revenue', models.DecimalField(
                    blank=True,
                    decimal_places=2,
                    max_digits=10,
                    null=True,
                    validators=[django.core.validators.MinValueValidator(Decimal('0.0'))]
                )),
                ('cpi', models.DecimalField(
                    blank=True,
                    decimal_places=2,
                    editable=False,
                    max_digits=10,
                    null=True,
                    validators=[django.core.validators.MinValueValidator(Decimal('0.0'))]
                )),
            ],
            options={
                'ordering': ['-metric_date'],
            },
        ),
    ]
