# Generated by Django 4.2.5 on 2023-10-15 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pcworld', '0003_product_alter_contact_email_alter_contact_message_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.IntegerField(null=True),
        ),
    ]
