# Generated by Django 2.0.13 on 2019-08-04 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0002_auto_20190803_2140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postres',
            name='nombre',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='postres',
            name='precio',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='postres',
            name='stock',
            field=models.CharField(max_length=100),
        ),
    ]