# Generated by Django 3.0 on 2019-12-12 15:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=32, null=True)),
                ('phone', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hobby', models.CharField(blank=True, max_length=32, null=True)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='boo', to='testapp.Person')),
            ],
        ),
    ]