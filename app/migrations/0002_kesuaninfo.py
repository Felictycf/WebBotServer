# Generated by Django 4.0.5 on 2022-06-24 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='KeSuanInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('address', models.CharField(max_length=32)),
                ('age', models.IntegerField(default=2)),
                ('number', models.CharField(max_length=64)),
                ('jiating', models.CharField(max_length=64)),
                ('vaccine', models.CharField(max_length=64)),
                ('kesuan', models.CharField(max_length=64)),
                ('jinzhu', models.CharField(max_length=64)),
            ],
        ),
    ]