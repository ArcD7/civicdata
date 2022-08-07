# Generated by Django 3.2.4 on 2022-08-04 18:31

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('scheme', '0009_alter_metadata_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resourceindex',
            name='file_name',
        ),
        migrations.AddField(
            model_name='resourceindex',
            name='uploaded_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='FileManagement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name', models.FileField(upload_to='csv')),
                ('resource_id', models.ForeignKey(db_column='resource_id', on_delete=django.db.models.deletion.CASCADE, to='scheme.resourceindex')),
            ],
            options={
                'db_table': 'Files',
            },
        ),
    ]
