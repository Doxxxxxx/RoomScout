# Generated by Django 2.2.3 on 2019-07-23 22:29

from django.db import migrations, models


class Migration(migrations.Migration):
	dependencies = [
		('houses', '0003_auto_20190723_1827'),
	]

	operations = [
		migrations.AddField(
			model_name='house',
			name='hide_address',
			field=models.BooleanField(default=False),
		),
	]
