# Generated by Django 3.2.8 on 2021-12-08 23:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20211209_0029'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rezervacija',
            old_name='sifra_apartmana',
            new_name='apartman',
        ),
        migrations.RenameField(
            model_name='rezervacija',
            old_name='sifra_gosta',
            new_name='gost',
        ),
    ]