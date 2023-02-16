# Generated by Django 3.0.5 on 2021-10-10 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MemberRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=50)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('phonenumber', models.CharField(blank=True, max_length=50, null=True)),
                ('department', models.CharField(max_length=50)),
                ('birthday', models.DateField(blank=True, null=True)),
                ('added', models.DateField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Member Records',
            },
        ),
    ]