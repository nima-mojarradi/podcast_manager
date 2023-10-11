# Generated by Django 4.2.5 on 2023-09-29 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rss_parser', '0013_remove_modelparser_id_alter_modelparser_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='modelparser',
            name='id',
            field=models.BigAutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='modelparser',
            name='title',
            field=models.CharField(max_length=255),
        ),
    ]