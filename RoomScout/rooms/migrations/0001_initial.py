# Generated by Django 2.2.3 on 2019-07-23 19:02

from django.db import migrations, models


class Migration(migrations.Migration):
	initial = True

	dependencies = [
	]

	operations = [
		migrations.CreateModel(
			name='Room',
			fields=[
				('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
				('name', models.CharField(default='', max_length=200)),
				('is_available', models.BooleanField(default=True)),
				('created_at', models.DateTimeField(auto_now_add=True)),
				('updated_at', models.DateTimeField(auto_now=True)),
				('price', models.FloatField(default=0.0)),
				('image', models.ImageField(blank=True, upload_to='images/')),
				('image2', models.ImageField(blank=True, upload_to='images/')),
				('image3', models.ImageField(blank=True, upload_to='images/')),
				('image4', models.ImageField(blank=True, upload_to='images/')),
				('image5', models.ImageField(blank=True, upload_to='images/')),
			],
		),
	]
