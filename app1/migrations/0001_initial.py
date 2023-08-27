# Generated by Django 3.2.5 on 2023-02-25 11:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cname', models.CharField(max_length=50)),
                ('dur', models.IntegerField()),
                ('fee', models.IntegerField()),
                ('trainer', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sname', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=50)),
                ('city', models.CharField(max_length=30)),
                ('contact', models.SmallIntegerField()),
                ('course', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='students', to='app1.course')),
            ],
        ),
    ]