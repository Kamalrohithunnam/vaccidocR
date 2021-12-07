# Generated by Django 3.2.9 on 2021-11-29 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AssessmentForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default='0000000', max_length=100)),
                ('age', models.CharField(max_length=100)),
                ('vaccine', models.CharField(max_length=100)),
                ('chronic', models.CharField(max_length=100)),
                ('tenderness', models.CharField(max_length=100)),
                ('symptoms', models.CharField(max_length=100)),
                ('feeling', models.CharField(max_length=100)),
            ],
        ),
    ]