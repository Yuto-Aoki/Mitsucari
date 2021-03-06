# Generated by Django 2.2.1 on 2019-09-11 07:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('qboard', '0009_auto_20190911_1241'),
    ]

    operations = [
        migrations.CreateModel(
            name='Predict',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('programming', models.IntegerField(blank=True, verbose_name='プログラミング歴')),
                ('develop_num', models.IntegerField(blank=True, verbose_name='開発物数')),
                ('gpa', models.IntegerField(blank=True, verbose_name='GPA')),
                ('atcoder', models.IntegerField(blank=True, verbose_name='Atcoderレート')),
                ('score', models.IntegerField(blank=True, verbose_name='スコア')),
                ('language', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='qboard.Language', verbose_name='言語')),
            ],
            options={
                'verbose_name': '予測データ',
                'verbose_name_plural': '予測データ',
            },
        ),
    ]
