# Generated by Django 3.2 on 2022-03-15 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sample_Paper', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='samplepaper',
            name='question',
            field=models.ManyToManyField(to='Sample_Paper.Question'),
        ),
    ]