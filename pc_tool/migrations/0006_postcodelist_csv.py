# Generated by Django 2.2.3 on 2019-07-15 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pc_tool', '0005_postcodelist_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='postcodelist',
            name='csv',
            field=models.TextField(default=''),
        ),
    ]
