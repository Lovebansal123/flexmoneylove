# Generated by Django 4.0.5 on 2022-12-11 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_payments'),
    ]

    operations = [
        migrations.AddField(
            model_name='payments',
            name='slot',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
