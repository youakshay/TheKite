# Generated by Django 4.0.3 on 2022-03-30 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kite', '0003_userdata_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=30)),
                ('type', models.CharField(default='', max_length=30)),
                ('description', models.CharField(max_length=400)),
                ('photo', models.ImageField(default='', upload_to='kite/photos')),
                ('price', models.IntegerField(default=0)),
            ],
        ),
    ]
