# Generated by Django 3.0.3 on 2020-03-01 08:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_language'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'ordering': ['first_name', 'last_name']},
        ),
    ]
