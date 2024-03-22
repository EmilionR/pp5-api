# Generated by Django 3.2.24 on 2024-03-22 16:16

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
            name='Block',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('target', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blocked', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_on'],
                'unique_together': {('owner', 'target')},
            },
        ),
    ]
