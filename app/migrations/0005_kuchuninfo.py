# Generated by Django 3.2.3 on 2022-07-06 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_jinhuoinfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='kuchunINfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('sum', models.CharField(max_length=64)),
                ('status', models.CharField(max_length=64)),
            ],
        ),
    ]