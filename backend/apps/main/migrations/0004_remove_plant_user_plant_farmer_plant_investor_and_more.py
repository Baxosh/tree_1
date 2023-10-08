# Generated by Django 4.1.5 on 2023-06-18 12:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0003_order_count_alter_order_farmer_alter_order_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plant',
            name='user',
        ),
        migrations.AddField(
            model_name='plant',
            name='farmer',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='farmer_plants', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='plant',
            name='investor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='investor_plants', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='plant',
            name='status',
            field=models.CharField(choices=[('created', 'Created'), ('in_order', 'In Order'), ('done', 'Done')], default='created', max_length=255),
        ),
        migrations.AlterField(
            model_name='plant',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
