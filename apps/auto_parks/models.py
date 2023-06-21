from django.db import models


class AutoParkModel(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return f'Auto_park: #{self.id} | {self.name}'

    class Meta:
        db_table = 'auto_parks'