# Generated by Django 2.2 on 2021-01-30 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0002_shop'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(default='', max_length=200)),
                ('price', models.IntegerField()),
                ('discount', models.IntegerField()),
            ],
        ),
    ]
