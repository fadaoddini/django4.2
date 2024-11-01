# Generated by Django 4.2 on 2024-10-29 15:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('transport', '0001_initial'),
        ('catalogue', '0002_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gateway',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('gateway_request_url', models.CharField(blank=True, max_length=150, null=True)),
                ('gateway_verify_url', models.CharField(blank=True, max_length=150, null=True)),
                ('gateway_code', models.CharField(choices=[('zarrinpal', 'zarrinpal'), ('melat', 'melat'), ('meli', 'meli')], default='zarrinpal', max_length=12)),
                ('is_enable', models.BooleanField(default=True)),
                ('auth_data', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Gateway',
                'verbose_name_plural': 'Gateways',
            },
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('faktor_number', models.UUIDField(unique=True)),
                ('amount', models.PositiveIntegerField()),
                ('gateway', models.CharField(default='zarinpal', max_length=40)),
                ('is_paid', models.BooleanField(default=False)),
                ('payment_log', models.TextField(blank=True)),
                ('authority', models.CharField(blank=True, max_length=64)),
                ('num_bids', models.PositiveIntegerField(default=0)),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalogue.product')),
                ('transport', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='transport.transportreq')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Payment',
                'verbose_name_plural': 'Payments',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.PositiveIntegerField()),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('updated_time', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='order', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]