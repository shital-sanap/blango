# Generated by Django 3.2.5 on 2022-07-22 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_remove_comment_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='content',
            field=models.TextField(default='What a great post?'),
            preserve_default=False,
        ),
    ]
