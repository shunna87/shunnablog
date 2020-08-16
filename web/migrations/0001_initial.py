# Generated by Django 3.0.8 on 2020-08-16 17:38

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Imprint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', ckeditor.fields.RichTextField()),
            ],
            options={
                'verbose_name': 'Imprint',
                'verbose_name_plural': 'Imprints',
            },
        ),
    ]
