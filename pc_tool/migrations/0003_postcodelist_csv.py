# Generated by Django 2.2.3 on 2019-07-11 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pc_tool', '0002_auto_20190711_1444'),
    ]

    operations = [
        migrations.AddField(
            model_name='postcodelist',
            name='csv',
            field=models.TextField(default=''),
        ),
    ]