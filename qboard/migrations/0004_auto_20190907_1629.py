# Generated by Django 2.2.1 on 2019-09-07 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qboard', '0003_internname_superman'),
    ]

    operations = [
        migrations.AlterField(
            model_name='superman',
            name='intern_name',
            field=models.ManyToManyField(blank=True, to='qboard.InternName', verbose_name='インターン名'),
        ),
    ]