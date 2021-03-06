# Generated by Django 2.2.1 on 2019-09-12 20:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('qboard', '0011_auto_20190912_1444'),
    ]

    operations = [
        migrations.CreateModel(
            name='Intern',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='インターン名')),
                ('work', models.TextField(verbose_name='内容')),
                ('score', models.IntegerField(verbose_name='最低限スコア')),
                ('salary', models.IntegerField(verbose_name='給料')),
                ('url', models.URLField(verbose_name='url')),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='qboard.Language', verbose_name='プログラミング言語')),
            ],
            options={
                'verbose_name': 'インターン情報データ',
                'verbose_name_plural': 'インターン情報データ',
            },
        ),
    ]
