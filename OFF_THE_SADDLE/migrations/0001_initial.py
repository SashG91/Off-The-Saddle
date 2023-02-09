# Generated by Django 3.2.16 on 2023-02-09 13:18

import cloudinary.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, unique=True)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('content', models.TextField()),
                ('featured_image', cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image')),
                ('excerpt', models.TextField(blank=True)),
                ('status', models.IntegerField(choices=[(0, 'Draft'), (1, 'Published')], default=0)),
                ('climb_difficulty', models.CharField(choices=[('1', 'A moderate ascend that can get challenging, weather and pace affect!'), ('2', 'For those who are starting to take it seriously'), ('3', "An absolute beast that requires you to give it all you've got")], default='1', max_length=250)),
                ('climb_surface', models.CharField(choices=[('ASPHALT', 'A purely asphalt surface'), ('ASPHALTCOBBLED', 'A combination of asphalt and cobble surface')], default='1', max_length=250)),
                ('climb_length', models.DecimalField(decimal_places=1, max_digits=5, null=True)),
                ('climb_elevationgain', models.DecimalField(decimal_places=1, max_digits=5, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blog_posts', to=settings.AUTH_USER_MODEL)),
                ('likes', models.ManyToManyField(blank=True, related_name='blog_likes', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('email', models.EmailField(max_length=254)),
                ('body', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('approved', models.BooleanField(default=False)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='OFF_THE_SADDLE.post')),
            ],
            options={
                'ordering': ['created_on'],
            },
        ),
    ]
