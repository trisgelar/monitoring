# Generated by Django 2.2 on 2019-05-17 08:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import documents.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=200, unique=True)),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('overview', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='documents_created', to=settings.AUTH_USER_MODEL)),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='documents', to='documents.Subject')),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True)),
                ('order', documents.fields.OrderField(blank=True)),
                ('document', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chapters', to='documents.Document')),
            ],
            options={
                'ordering': ['order'],
            },
        ),
    ]
