# Generated by Django 4.1.2 on 2022-10-23 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menus', '0003_alter_menu_file_contant'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='file_contant',
            field=models.FileField(null=True, upload_to='content/'),
        ),
    ]
