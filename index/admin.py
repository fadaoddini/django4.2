from django.contrib import admin
from django.contrib.admin import register

from index.models import SettingApp, RuleCategory, Rule


@register(SettingApp)
class SettingAppAdmin(admin.ModelAdmin):
    list_display = ('title', 'tel', 'mobile', 'email', 'is_active')
    list_editable = ('is_active',)


@admin.register(RuleCategory)
class RuleCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')  # ستون‌هایی که نمایش داده می‌شوند
    search_fields = ('name',)  # امکان جستجو بر اساس نام
    list_per_page = 20  # تعداد آیتم‌ها در هر صفحه



@admin.register(Rule)
class RuleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'is_active', 'created_at', 'updated_at')  # ستون‌های نمایش
    list_filter = ('category', 'is_active', 'created_at')  # فیلتر بر اساس دسته‌بندی و وضعیت فعال بودن
    search_fields = ('title', 'content')  # امکان جستجو بر اساس عنوان و متن
    list_editable = ('is_active',)  # ویرایش مستقیم وضعیت فعال بودن از لیست
    date_hierarchy = 'created_at'  # امکان فیلتر زمانی
    autocomplete_fields = ('category',)  # جستجوی سریع برای انتخاب دسته‌بندی
    ordering = ('-created_at',)  # ترتیب نمایش قوانین


