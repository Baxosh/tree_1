# Generated by Django 4.2.2 on 2023-06-27 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_remove_user_dispatch_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='dispatch_id',
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]
