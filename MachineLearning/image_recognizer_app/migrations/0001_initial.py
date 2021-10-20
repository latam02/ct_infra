# Generated by Django 3.2.5 on 2021-10-10 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Assets',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('path', models.CharField(max_length=50)),
                ('checksum', models.CharField(max_length=100)),
            ],
            options={
                'managed': True,
            },
        ),
    ]