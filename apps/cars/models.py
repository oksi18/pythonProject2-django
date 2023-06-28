from datetime import datetime

from django.core import validators as V
from django.db import models

from apps.auto_parks.models import AutoParkModel
from apps.cars.choices.body_type_choices import BodyTypeChoices
from core.enums.regex_enums import RegExEnum
from core.models import BaseModel


class CarModel(models.Model):
    body_type = models.CharField(max_length=11, choices=BodyTypeChoices.choices)
    brand = models.CharField(max_length=25, validators=
        [V.RegexValidator(RegExEnum.BRAND.pattern, RegExEnum.BRAND.msg)
         ])
    price = models.IntegerField(validators=[
        V.MinValueValidator(0),
        V.MaxValueValidator(1000000)
    ])
    year = models.IntegerField(validators=[
        V.MinValueValidator(1990),
        V.MaxValueValidator(datetime.now().year)
    ])
    engine_volume = models.FloatField()
    seat_count = models.IntegerField()
    updated_at = models.DateTimeField(auto_now=True)
    auto_park = models.ForeignKey(AutoParkModel, on_delete=models.CASCADE, related_name='cars', blank=True, null=True)

    def __str__(self):
        return f'Car #{self.id} | {self.brand}'

    class Meta:
        db_table = 'cars'
        ordering = ['id']
