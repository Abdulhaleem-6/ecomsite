# Generated by Django 4.1.5 on 2023-03-02 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_alter_products_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('items', models.CharField(max_length=2000)),
                ('name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=1000)),
                ('state', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('zipcode', models.CharField(max_length=200)),
            ],
        ),
    ]