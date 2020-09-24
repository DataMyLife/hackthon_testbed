# Generated by Django 3.1.1 on 2020-09-24 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contents_name', models.CharField(max_length=50)),
                ('contents_href', models.CharField(max_length=100)),
                ('contents_type', models.CharField(max_length=50)),
                ('cluster_label', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='survey',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('USER_ID', models.CharField(max_length=50)),
                ('Q_1', models.IntegerField()),
                ('Q_2', models.IntegerField()),
                ('Q_3', models.IntegerField()),
                ('Q_4', models.IntegerField()),
                ('Q_5', models.IntegerField()),
                ('Q_6', models.IntegerField()),
                ('Q_7', models.IntegerField()),
                ('Q_8', models.IntegerField()),
                ('Q_9', models.IntegerField()),
                ('Q_10', models.IntegerField()),
                ('Q_11', models.IntegerField()),
                ('Q_12', models.IntegerField()),
            ],
        ),
    ]
