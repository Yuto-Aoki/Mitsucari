# Generated by Django 2.2.1 on 2019-09-07 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qboard', '0004_auto_20190907_1629'),
    ]

    operations = [
        migrations.AddField(
            model_name='superman',
            name='twitter_name',
            field=models.CharField(max_length=20, null=True, verbose_name='ホームページ用'),
        ),
    ]
