# Generated by Django 4.0 on 2021-12-20 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_link_shortener_link_end'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='shortener_link_end',
            field=models.CharField(max_length=30),
        ),
    ]
