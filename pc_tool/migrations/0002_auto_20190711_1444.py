# Generated by Django 2.2.3 on 2019-07-11 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pc_tool', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postcodelist',
            name='text',
            field=models.TextField(),
        ),
    ]
