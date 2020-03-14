# Generated by Django 2.2 on 2020-03-14 11:39

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('webapp', '0002_file_general_access'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='private_users',
            field=models.ManyToManyField(related_name='access_files', to=settings.AUTH_USER_MODEL, verbose_name='Приват'),
        ),
    ]
