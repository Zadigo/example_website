# Generated by Django 3.2.8 on 2021-10-22 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_myuser_user_permissions'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='is_superuser',
            field=models.BooleanField(default=False, help_text='Gives all permissions to a designated user', verbose_name='superuser status'),
        ),
    ]
