# Generated by Django 2.2.6 on 2019-11-14 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0005_auto_20191111_1124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='full_name',
            field=models.CharField(max_length=255),
        ),
    ]
