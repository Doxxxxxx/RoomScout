# Generated by Django 2.2.6 on 2019-11-11 02:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emails', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='emailmessage',
            name='status',
            field=models.CharField(choices=[('S', 'SUCCESS'), ('F', 'FAILED')], default='F', max_length=2),
        ),
    ]
