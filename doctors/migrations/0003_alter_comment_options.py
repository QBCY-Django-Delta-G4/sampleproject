# Generated by Django 5.1.1 on 2024-09-05 06:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0002_comment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ('created',)},
        ),
    ]
