# Generated by Django 3.2.4 on 2022-08-03 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ResourceIndex',
            fields=[
                ('resource_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=128)),
                ('description', models.CharField(max_length=128, null=True)),
                ('tags', models.CharField(max_length=128, null=True)),
            ],
            options={
                'db_table': 'Index',
            },
        ),
    ]
