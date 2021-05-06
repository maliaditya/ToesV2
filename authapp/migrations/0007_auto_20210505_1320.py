# Generated by Django 3.1.4 on 2021-05-05 13:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0006_auto_20210107_1433'),
    ]

    operations = [
        migrations.RenameField(
            model_name='jobdetails',
            old_name='job_Description',
            new_name='job_description',
        ),
        migrations.CreateModel(
            name='Inbox',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('receiver_id', models.IntegerField()),
                ('last_msg', models.CharField(max_length=255)),
                ('seen', models.BooleanField(default=False)),
                ('unseen', models.IntegerField()),
                ('sender_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('receiver_id', models.IntegerField()),
                ('msg', models.CharField(max_length=500)),
                ('sender_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
