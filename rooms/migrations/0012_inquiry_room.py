# Generated by Django 2.2.4 on 2019-09-19 20:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0011_inquiry'),
    ]

    operations = [
        migrations.AddField(
            model_name='inquiry',
            name='room',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='rooms.Room'),
            preserve_default=False,
        ),
    ]
