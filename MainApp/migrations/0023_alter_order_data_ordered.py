# Generated by Django 3.2.4 on 2021-07-12 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0022_auto_20210712_1638'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='data_ordered',
            field=models.DateTimeField(default='?'),
        ),
    ]