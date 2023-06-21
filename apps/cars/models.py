from django.db import models

from apps.auto_parks.models import AutoParkModel


class CarModel(models.Model):
    brand = models.CharField(max_length=25)
    price = models.IntegerField(default=0)
    year = models.IntegerField(default=0)
    updated_at = models.DateTimeField(auto_now=True)
    auto_park = models.ForeignKey(AutoParkModel, on_delete=models.CASCADE, related_name='cars', blank=True, null=True)

    def __str__(self):
        return f'Car #{self.id} | {self.brand}'

    class Meta:
        db_table = 'cars'