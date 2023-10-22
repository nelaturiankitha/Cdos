# Generated by Django 2.1.15 on 2023-10-20 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Spence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=200)),
                ('cost', models.CharField(max_length=30)),
                ('expiry_date', models.DateTimeField(verbose_name='release date')),
                ('quantity', models.IntegerField()),
                ('duration', models.FloatField()),
            ],
        ),
    ]
