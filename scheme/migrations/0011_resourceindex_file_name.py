# Generated by Django 3.2.4 on 2022-08-04 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scheme', '0010_auto_20220804_1831'),
    ]

    operations = [
        migrations.AddField(
            model_name='resourceindex',
            name='file_name',
            field=models.FileField(default=None, upload_to='csv'),
        ),
    ]
