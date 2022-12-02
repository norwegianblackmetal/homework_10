# Generated by Django 4.1.3 on 2022-11-13 13:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RecordGenre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='RecordLabel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artist', models.CharField(max_length=30)),
                ('album', models.CharField(max_length=40)),
                ('year', models.IntegerField()),
                ('condition', models.CharField(max_length=3)),
                ('genre', models.ManyToManyField(to='records.recordgenre')),
                ('record_label', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='records.recordlabel')),
            ],
        ),
    ]