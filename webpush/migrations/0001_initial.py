# Generated by Django 3.1.4 on 2021-01-16 05:29

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
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='SubscriptionInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('browser', models.CharField(max_length=100)),
                ('endpoint', models.URLField(max_length=500)),
                ('auth', models.CharField(max_length=100)),
                ('p256dh', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='PushInformation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='webpush_info', to='webpush.group')),
                ('subscription', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='webpush_info', to='webpush.subscriptioninfo')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='webpush_info', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
