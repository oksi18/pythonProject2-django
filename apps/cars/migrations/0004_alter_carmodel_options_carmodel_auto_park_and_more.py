# Generated by Django 4.2.2 on 2023-06-28 20:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auto_parks', '0001_initial'),
        ('cars', '0003_carmodel_delete_car'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='carmodel',
            options={'ordering': ['id']},
        ),
        migrations.AddField(
            model_name='carmodel',
            name='price',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='carmodel',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='carmodel',
            name='body_type',
            field=models.CharField(choices=[('Hatchback', 'Hatchback'), ('Sedan', 'Sedan'), ('MUV / SUV', 'Muv Suv'), ('Coupe', 'Coupe'), ('Convertible', 'Convertible'), ('Wagon', 'Wagon'), ('Van', 'Van'), ('Jeep', 'Jeep')], max_length=11),
        ),
        migrations.AlterField(
            model_name='carmodel',
            name='year',
            field=models.IntegerField(default=0),
        ),
    ]
