# Generated by Django 3.0.6 on 2020-07-05 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0007_remove_signup_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='signup',
            name='user',
            field=models.CharField(choices=[('consumer', 'provider')], max_length=240, null=True),
        ),
        migrations.AlterField(
            model_name='signin',
            name='email',
            field=models.EmailField(max_length=140),
        ),
        migrations.AlterField(
            model_name='signup',
            name='email',
            field=models.EmailField(max_length=140),
        ),
        migrations.AlterField(
            model_name='signup',
            name='first_name',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='signup',
            name='password',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='signup',
            name='second_name',
            field=models.CharField(max_length=250),
        ),
    ]
