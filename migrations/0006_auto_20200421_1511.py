# Generated by Django 3.0.4 on 2020-04-21 15:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('NeuralPainter', '0005_auto_20200421_1506'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paint',
            name='genre',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='NeuralPainter.Genre'),
        ),
        migrations.AlterField(
            model_name='painter',
            name='genres',
            field=models.ManyToManyField(blank=True, null=True, to='NeuralPainter.Genre'),
        ),
    ]
