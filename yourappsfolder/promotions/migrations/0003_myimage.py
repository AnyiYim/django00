# Generated by Django 2.0.5 on 2018-08-07 09:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('promotions', '0002_auto_20150604_1450'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyImage',
            fields=[
                ('image_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='promotions.Image')),
                ('detail', models.CharField(max_length=55)),
            ],
            options={
                'verbose_name': 'Promotion',
                'verbose_name_plural': 'Promotions',
                'abstract': False,
            },
            bases=('promotions.image',),
        ),
    ]
