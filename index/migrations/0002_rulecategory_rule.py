# Generated by Django 4.2 on 2024-11-29 11:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RuleCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='نام دسته\u200cبندی')),
                ('description', models.TextField(blank=True, null=True, verbose_name='توضیحات')),
            ],
            options={
                'verbose_name': 'دسته\u200cبندی قانون',
                'verbose_name_plural': 'دسته\u200cبندی قوانین',
            },
        ),
        migrations.CreateModel(
            name='Rule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='عنوان قانون')),
                ('content', models.TextField(verbose_name='متن قانون')),
                ('is_active', models.BooleanField(default=True, verbose_name='فعال بودن قانون')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='تاریخ به\u200cروزرسانی')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rules', to='index.rulecategory', verbose_name='دسته\u200cبندی')),
            ],
            options={
                'verbose_name': 'قانون',
                'verbose_name_plural': 'قوانین',
                'ordering': ['-created_at'],
            },
        ),
    ]
