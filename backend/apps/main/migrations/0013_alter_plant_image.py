# Generated by Django 4.2.2 on 2023-06-26 18:35

from django.db import migrations, models
import main.utils.files


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_alter_plant_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plant',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=main.utils.files.FilePath('files\\')),
        ),
    ]
