# Generated by Django 4.2.10 on 2024-03-27 23:32

from django.db import migrations

def create_logins(apps, schema_editor):
    User = apps.get_model('edu_app', 'User')
    User.objects.create(username='admin', password='pass', email='admin', name='admin')
    User.objects.create(username='nash', password='plaintext', email='nash@heck.com', name='Nash E')
    User.objects.create(username='fred', password='bingo', email='fred@heck.com', name='Fred T')

class Migration(migrations.Migration):

    dependencies = [
        ('edu_app', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_logins),
    ]