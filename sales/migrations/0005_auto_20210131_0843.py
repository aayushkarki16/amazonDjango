# Generated by Django 2.2 on 2021-01-31 02:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0004_offer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='image',
            field=models.ImageField(default='kg.jpg', null=True, upload_to='image/'),
        ),
    ]
