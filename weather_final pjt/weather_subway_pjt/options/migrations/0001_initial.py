# Generated by Django 4.1 on 2022-11-10 01:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tourism',
            fields=[
                ('t_idx', models.BigAutoField(primary_key=True, serialize=False)),
                ('station_name', models.CharField(max_length=100)),
                ('t_name', models.CharField(max_length=100)),
                ('cate', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=100)),
                ('lat', models.FloatField()),
                ('lon', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'tourism',
                'managed': False,
            },
        ),
    ]
