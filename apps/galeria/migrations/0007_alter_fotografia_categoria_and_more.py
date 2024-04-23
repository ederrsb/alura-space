# Generated by Django 5.0.3 on 2024-04-23 00:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0006_fotografia_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fotografia',
            name='categoria',
            field=models.CharField(choices=[('NEBULOSA', 'Nebulosa'), ('ESTRELA', 'Estrela'), ('GAL�XIA', 'Galáxia'), ('PLANETA', 'Planeta')], default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='fotografia',
            name='publicada',
            field=models.BooleanField(default=True),
        ),
    ]
