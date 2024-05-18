# Generated by Django 5.0.6 on 2024-05-18 19:45

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Carpet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('size', models.CharField(max_length=50)),
                ('material', models.CharField(blank=True, max_length=50, null=True)),
                ('style', models.CharField(choices=[('herringbone', 'Herringbone'), ('saxony', 'Saxony'), ('twist', 'Twist'), ('woven', 'Woven'), ('velvet', 'Velvet')], max_length=20)),
                ('color', models.CharField(choices=[('red', 'Red'), ('blue', 'Blue'), ('green', 'Green'), ('yellow', 'Yellow'), ('purple', 'Purple'), ('pink', 'Pink'), ('brown', 'Brown'), ('gray', 'Gray'), ('black', 'Black'), ('white', 'White')], max_length=20)),
                ('suitability', models.CharField(choices=[('living_room', 'Living Room'), ('bedroom', 'Bedroom'), ('dining_room', 'Dining Room'), ('bathroom', 'Bathroom'), ('hallway', 'Hallway')], max_length=20)),
                ('image', models.ImageField(blank=True, upload_to='carpet_images')),
                ('is_sold', models.BooleanField(default=False)),
                ('location', models.CharField(default='algeria', max_length=100)),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='carpets', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]