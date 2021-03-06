# Generated by Django 3.0.6 on 2020-05-30 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_auto_20200529_1530'),
    ]

    operations = [
        migrations.CreateModel(
            name='signin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(default='enter email', max_length=140)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='signup',
            name='email',
            field=models.EmailField(default='enter email', max_length=140),
        ),
        migrations.AddField(
            model_name='signup',
            name='password',
            field=models.CharField(default='email', max_length=50),
            preserve_default=False,
        ),
    ]
