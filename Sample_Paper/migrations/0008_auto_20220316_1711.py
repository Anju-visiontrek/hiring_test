# Generated by Django 3.2 on 2022-03-16 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sample_Paper', '0007_auto_20220316_1702'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='language',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='samplepaper',
            name='language',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='samplepaper',
            name='level',
            field=models.CharField(default='', max_length=255),
        ),
    ]