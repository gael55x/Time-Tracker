# Generated by Django 5.0.2 on 2024-02-25 03:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('user_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='AppUser',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=50, unique=True)),
                ('username', models.CharField(max_length=50)),
                ('user_id', models.AutoField(default=334, primary_key=True, serialize=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, related_name='app_users', related_query_name='app_user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, related_name='app_users', related_query_name='app_user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TimeEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hours', models.DecimalField(decimal_places=2, max_digits=5)),
                ('description', models.TextField()),
                ('date_time', models.DateTimeField(auto_now_add=True)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='time_tracker_app.project')),
                ('user', models.ForeignKey(db_column='user_id', on_delete=django.db.models.deletion.CASCADE, to='time_tracker_app.appuser')),
            ],
        ),
        migrations.CreateModel(
            name='TaskDescription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('time_entry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='time_tracker_app.timeentry')),
            ],
        ),
    ]