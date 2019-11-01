# Generated by Django 2.2.6 on 2019-10-23 17:08

from django.db import migrations
from  src.models.user import User
import  json
from  django.contrib.auth import hashers
def my_function(apps, schema_editor):
    data = []
    print(11111111111111111)
    with open('src/fakerdata/user.json') as f:

        users = json.load(f)
        for item in users:

            item['username'] = str(item['username'])
            item['code'] = str(item['code'])
            item['password'] = str(item['password'])
            user = User(username= item['username'],password = hashers.SHA1PasswordHasher().encode(item['password'],salt='1123'),code =item['code'],full_name=item['full_name'],role =item['role'])
            data.append(user)
    print(data[0])
    User.objects.bulk_create(data)

class Migration(migrations.Migration):

    dependencies = [
        ('src', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(my_function),
    ]