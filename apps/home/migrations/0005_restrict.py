# Generated by Django 3.2.6 on 2022-02-05 00:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20220201_2000'),
    ]

    operations = [
        migrations.CreateModel(
            name='restrict',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('govern', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.governorate')),
            ],
        ),
    ]