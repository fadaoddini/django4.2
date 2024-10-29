# Generated by Django 4.2 on 2024-10-29 15:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tolid',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sum_tolid', models.BigIntegerField(default=0)),
                ('year', models.CharField(max_length=10)),
                ('month', models.CharField(max_length=10)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tolid', to='company.location')),
            ],
            options={
                'verbose_name': 'Tolid',
                'verbose_name_plural': 'Tolids',
            },
        ),
        migrations.CreateModel(
            name='SettingHoghoogh',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price_bime_in_day', models.IntegerField(default=0)),
                ('start_end_hoghoogh', models.CharField(max_length=32)),
                ('num_day', models.IntegerField(default=31)),
                ('darsad_all', models.IntegerField(default=0)),
                ('darsad_sarparast', models.IntegerField(default=0)),
                ('pele_one_day', models.IntegerField(default=0)),
                ('pele_one_darsad', models.IntegerField(default=0)),
                ('pele_two_day', models.IntegerField(default=0)),
                ('pele_two_darsad', models.IntegerField(default=0)),
                ('pele_three_day', models.IntegerField(default=0)),
                ('pele_three_darsad', models.IntegerField(default=0)),
                ('location', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='company.location')),
            ],
            options={
                'verbose_name': 'SettingHoghoogh',
                'verbose_name_plural': 'SettingHoghooghs',
            },
        ),
        migrations.CreateModel(
            name='Sarparasti',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sum_day_sarparast', models.IntegerField(default=0)),
                ('role', models.IntegerField(default=0)),
                ('year', models.CharField(max_length=10)),
                ('month', models.CharField(max_length=10)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sarparast', to='company.location')),
                ('staff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.staff')),
            ],
            options={
                'verbose_name': 'Sarparasti',
                'verbose_name_plural': 'Sarparastiha',
            },
        ),
        migrations.CreateModel(
            name='ListPrice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=42)),
                ('price', models.IntegerField()),
                ('value_type', models.PositiveSmallIntegerField(choices=[(1, 'dates'), (2, 'etc')], default=1)),
                ('is_active', models.BooleanField(choices=[(True, 'active'), (False, 'inactive')], default=True)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='listprice', to='company.location')),
            ],
            options={
                'verbose_name': 'ListPrice',
                'verbose_name_plural': 'ListPrices',
            },
        ),
        migrations.CreateModel(
            name='HoghooghArchive',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sum_calculate', models.BigIntegerField()),
                ('sum_all', models.BigIntegerField()),
                ('days', models.IntegerField()),
                ('pele_price', models.BigIntegerField(default=0)),
                ('total_pay', models.BigIntegerField(default=0)),
                ('sarparasti', models.BigIntegerField(default=0)),
                ('mosaede', models.BigIntegerField(default=0)),
                ('vam', models.BigIntegerField(default=0)),
                ('bime', models.BigIntegerField(default=0)),
                ('tashvighi', models.BigIntegerField(default=0)),
                ('year', models.CharField(max_length=10)),
                ('month', models.CharField(max_length=10)),
                ('karaee', models.FloatField(default=0)),
                ('amar', models.JSONField()),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hoghoogharchives', to='company.location')),
                ('staff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.staff')),
            ],
            options={
                'verbose_name': 'HoghooghArchive',
                'verbose_name_plural': 'HoghooghArchives',
            },
        ),
        migrations.CreateModel(
            name='Hoghoogh',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sum_calculate', models.BigIntegerField()),
                ('sum_all', models.BigIntegerField()),
                ('days', models.IntegerField()),
                ('pele_price', models.BigIntegerField(default=0)),
                ('total_pay', models.BigIntegerField(default=0)),
                ('sarparasti', models.BigIntegerField(default=0)),
                ('mosaede', models.BigIntegerField(default=0)),
                ('vam', models.BigIntegerField(default=0)),
                ('bime', models.BigIntegerField(default=0)),
                ('tashvighi', models.BigIntegerField(default=0)),
                ('year', models.CharField(max_length=10)),
                ('month', models.CharField(max_length=10)),
                ('karaee', models.FloatField(default=0)),
                ('amar', models.JSONField()),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hoghooghs', to='company.location')),
                ('staff', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='company.staff')),
            ],
            options={
                'verbose_name': 'Hoghoogh',
                'verbose_name_plural': 'Hoghooghs',
            },
        ),
        migrations.CreateModel(
            name='AmarArchive',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=42)),
                ('price', models.IntegerField()),
                ('tedad', models.FloatField()),
                ('type', models.CharField(max_length=42)),
                ('year', models.CharField(max_length=10)),
                ('month', models.CharField(max_length=10)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='amarlocation', to='company.location')),
            ],
            options={
                'verbose_name': 'AmarArchive',
                'verbose_name_plural': 'AmarArchives',
            },
        ),
        migrations.CreateModel(
            name='Amar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=42)),
                ('price', models.IntegerField()),
                ('tedad', models.FloatField()),
                ('type', models.CharField(max_length=42)),
                ('is_sarparast', models.BooleanField(choices=[(True, 'yes'), (False, 'no')], default=True)),
                ('tarikh', models.CharField(max_length=42)),
                ('listprice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='amarlist', to='hoghoogh.listprice')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='amar', to='company.location')),
                ('staff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='amar', to='company.staff')),
            ],
            options={
                'verbose_name': 'Amar',
                'verbose_name_plural': 'Amars',
            },
        ),
    ]
