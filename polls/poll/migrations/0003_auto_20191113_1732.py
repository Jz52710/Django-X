# Generated by Django 2.2.7 on 2019-11-13 09:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0002_auto_20191113_1701'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='choice',
            options={'verbose_name': '选项', 'verbose_name_plural': '选项'},
        ),
        migrations.AlterModelOptions(
            name='question',
            options={'verbose_name': '问题', 'verbose_name_plural': '问题'},
        ),
        migrations.AlterModelTable(
            name='choice',
            table='choice',
        ),
        migrations.AlterModelTable(
            name='question',
            table='question',
        ),
    ]