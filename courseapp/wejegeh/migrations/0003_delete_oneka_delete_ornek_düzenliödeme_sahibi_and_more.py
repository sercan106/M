# Generated by Django 4.1.3 on 2023-11-04 11:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wejegeh', '0002_oneka'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Oneka',
        ),
        migrations.DeleteModel(
            name='Ornek',
        ),
        migrations.AddField(
            model_name='düzenliödeme',
            name='sahibi',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='wejegeh.sahibi'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ödemedetay',
            name='sahibi',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='wejegeh.sahibi'),
            preserve_default=False,
        ),
    ]
