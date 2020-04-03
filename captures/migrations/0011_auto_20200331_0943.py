# Generated by Django 3.0.3 on 2020-03-31 12:43

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('captures', '0010_auto_20200331_0935'),
    ]

    operations = [
        migrations.AddField(
            model_name='capturepack',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='capturepack',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='capturepack',
            name='updated_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='faceimageattempt',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='faceimagecapture',
            name='is_active',
            field=models.BooleanField(default=True),
        )
    ]