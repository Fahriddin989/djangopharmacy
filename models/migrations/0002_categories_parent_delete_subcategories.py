# Generated by Django 4.2 on 2023-05-03 13:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='categories',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='models.categories', verbose_name='Подкатегория'),
        ),
        migrations.DeleteModel(
            name='SubCategories',
        ),
    ]
