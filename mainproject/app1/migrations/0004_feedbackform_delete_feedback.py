# Generated by Django 5.0.3 on 2024-05-09 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_rename_psw2_admission_pass01'),
    ]

    operations = [
        migrations.CreateModel(
            name='feedbackform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(default='', max_length=20)),
                ('lname', models.CharField(default='', max_length=20)),
                ('contact', models.CharField(default='', max_length=50)),
                ('subject', models.CharField(default='', max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='feedback',
        ),
    ]
