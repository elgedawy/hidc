# Generated by Django 3.2.6 on 2022-02-26 18:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_request_mark'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='phone',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='request',
            name='device',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.device', verbose_name='نوع الجهاز'),
        ),
        migrations.AlterField(
            model_name='request',
            name='edara',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.edara', verbose_name='إدارة'),
        ),
        migrations.AlterField(
            model_name='request',
            name='govern',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.governorate', verbose_name='محافظة'),
        ),
        migrations.AlterField(
            model_name='request',
            name='mark',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.mark', verbose_name='الماركة'),
        ),
        migrations.AlterField(
            model_name='request',
            name='model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.model', verbose_name='الموديل'),
        ),
        migrations.AlterField(
            model_name='request',
            name='name',
            field=models.CharField(max_length=50, verbose_name='الاسم'),
        ),
        migrations.AlterField(
            model_name='request',
            name='national_id',
            field=models.IntegerField(max_length=14, verbose_name='الرقم القومى'),
        ),
        migrations.AlterField(
            model_name='request',
            name='place',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.place', verbose_name='مكان العمل '),
        ),
        migrations.AlterField(
            model_name='request',
            name='serial',
            field=models.IntegerField(verbose_name='الرقم المسلسل'),
        ),
        migrations.AlterField(
            model_name='request',
            name='unit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.unit', verbose_name='وحدة'),
        ),
    ]
