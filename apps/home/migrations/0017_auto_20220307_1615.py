# Generated by Django 3.2.6 on 2022-03-07 14:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_auto_20220226_2024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='device',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.device', verbose_name=''),
        ),
        migrations.AlterField(
            model_name='request',
            name='edara',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.edara', verbose_name=''),
        ),
        migrations.AlterField(
            model_name='request',
            name='govern',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.governorate', verbose_name=''),
        ),
        migrations.AlterField(
            model_name='request',
            name='mark',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.mark', verbose_name=''),
        ),
        migrations.AlterField(
            model_name='request',
            name='model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.model', verbose_name=''),
        ),
        migrations.AlterField(
            model_name='request',
            name='name',
            field=models.CharField(max_length=50, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='request',
            name='national_id',
            field=models.IntegerField(max_length=14, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='request',
            name='phone',
            field=models.IntegerField(verbose_name=''),
        ),
        migrations.AlterField(
            model_name='request',
            name='place',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.place', verbose_name=' '),
        ),
        migrations.AlterField(
            model_name='request',
            name='serial',
            field=models.IntegerField(verbose_name=''),
        ),
        migrations.AlterField(
            model_name='request',
            name='unit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.unit', verbose_name=''),
        ),
    ]
