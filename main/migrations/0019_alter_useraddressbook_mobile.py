# Generated by Django 4.1.7 on 2023-04-06 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_alter_productreview_options_alter_wishlist_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraddressbook',
            name='mobile',
            field=models.PositiveIntegerField(max_length=50, null=True),
        ),
    ]
