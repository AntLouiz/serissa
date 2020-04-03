# Generated by Django 3.0.3 on 2020-03-31 12:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('captures', '0009_auto_20200331_0911'),
    ]

    operations = [
        migrations.RenameField(
            model_name='capturepack',
            old_name='user',
            new_name='profile',
        ),
        migrations.RemoveField(
            model_name='faceimagecapture',
            name='user',
        ),
        migrations.AlterField(
            model_name='faceimagecapture',
            name='pack',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='captures.CapturePack'),
            preserve_default=False,
        ),
    ]