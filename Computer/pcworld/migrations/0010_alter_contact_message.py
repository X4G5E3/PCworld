# Generated by Django 4.2.5 on 2023-10-30 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pcworld', '0009_contact_delete_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='message',
            field=models.CharField(max_length=500),
        ),
    ]
