# Generated by Django 4.0.5 on 2022-07-24 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realtor', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agent',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='realtor'),
        ),
    ]
