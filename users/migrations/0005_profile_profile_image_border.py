# Generated by Django 4.1.1 on 2022-10-03 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_profile_delete_users'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='profile_image_border',
            field=models.ImageField(blank=True, default='profiles/user-default.png', null=True, upload_to='profiles/'),
        ),
    ]
