# Generated by Django 4.0 on 2021-12-20 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='link',
            name='shortener_link_end',
            field=models.URLField(blank=True, null=True),
        ),
    ]