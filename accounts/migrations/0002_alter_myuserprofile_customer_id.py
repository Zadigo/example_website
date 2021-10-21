# Generated by Django 3.2.8 on 2021-10-20 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuserprofile',
            name='customer_id',
            field=models.CharField(blank=True, help_text='Stripe customer ID', max_length=100, null=True, unique=True),
        ),
    ]