# Generated by Django 2.2.6 on 2019-10-24 02:18

import json

from django.db import migrations

from src.models import Room


def my_function(apps, schema_editor):
    data = []
    print(11111111111111111)
    with open('src/fakerdata/room.json') as f:
        seats = json.load(f)
        for item in seats:
            print(item)
            seat = Room(name=item['name'], location=item['location'], max_student=item['max_student'])
            data.append(seat)
        Room.objects.bulk_create(data)


class Migration(migrations.Migration):
    dependencies = [
        ('src', '0007_auto_20191114_2313'),
    ]

    operations = [
        migrations.RunPython(my_function)
    ]
