# Generated by Django 4.0.3 on 2022-03-04 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_remove_detail_date_alter_detail_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detail',
            name='title',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]