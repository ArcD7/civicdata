# Generated by Django 3.2.4 on 2022-08-04 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scheme', '0008_auto_20220804_1044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='metadata',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
