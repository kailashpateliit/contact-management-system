# Generated by Django 3.1.4 on 2022-02-05 06:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FamilyHead',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('family_code', models.CharField(max_length=14)),
                ('full_name', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=150)),
                ('birthday', models.DateField(blank=True, null=True)),
                ('phone_number', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='FamilyMembers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=150)),
                ('relationship', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=200)),
                ('age', models.PositiveIntegerField()),
                ('familyhead', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='family.familyhead')),
            ],
        ),
    ]
