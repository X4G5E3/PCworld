# Generated by Django 4.2.5 on 2023-10-30 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pcworld', '0008_delete_contact_component_fulldesc_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('message', models.TextField(max_length=500)),
            ],
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]