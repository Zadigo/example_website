# Generated by Django 3.2.8 on 2021-10-22 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('accounts', '0004_myuser_is_superuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='groups',
            field=models.ManyToManyField(blank=True, related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups'),
        ),
    ]