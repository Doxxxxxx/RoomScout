# Generated by Django 2.2.4 on 2019-09-19 04:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0004_inquiry'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
