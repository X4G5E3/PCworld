# Generated by Django 4.2.5 on 2023-10-30 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pcworld', '0010_alter_contact_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='message',
            field=models.TextField(),
        ),
    ]