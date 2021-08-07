# Generated by Django 3.2.4 on 2021-06-20 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0016_auto_20210620_1917'),
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('body', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Cards',
        ),
    ]
