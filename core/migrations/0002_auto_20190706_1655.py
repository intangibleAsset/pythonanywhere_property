# Generated by Django 2.2 on 2019-07-06 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemimage',
            name='thumbnail',
            field=models.ImageField(null=True, upload_to='home/tolca/property/media/'),
        ),
    ]
