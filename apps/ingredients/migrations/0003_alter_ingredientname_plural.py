# Generated by Django 3.2 on 2021-04-19 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ingredients', '0002_auto_20210419_0703'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredientname',
            name='plural',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
