# Generated by Django 3.0.5 on 2020-05-04 13:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0009_auto_20200503_1000'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='entry',
            unique_together={('topic', 'text')},
        ),
    ]
