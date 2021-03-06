# Generated by Django 3.0.5 on 2020-04-07 15:38

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
            name='Priority',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('orders', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=40)),
                ('done', models.BooleanField(default=False)),
                ('create', models.DateField(auto_now_add=True)),
                ('update', models.DateField(auto_now_add=True)),
                ('assigned_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assigned', to=settings.AUTH_USER_MODEL)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created', to=settings.AUTH_USER_MODEL)),
                ('priority', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='todolist_app.Priority')),
                ('update_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='updated', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
