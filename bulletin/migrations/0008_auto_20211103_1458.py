# Generated by Django 3.2.8 on 2021-11-03 13:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bulletin', '0007_auto_20211103_1455'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='note',
            name='classes',
        ),
        migrations.AddField(
            model_name='note',
            name='classe',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='bulletin.classe'),
        ),
    ]