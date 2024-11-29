from django.db import models


class SettingApp(models.Model):
    ACTIVE = True
    INACTIVE = False

    STATUS_OPEN = (
        (ACTIVE, 'active'),
        (INACTIVE, 'inactive'),
    )
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True)
    favicon = models.ImageField(upload_to='settings/', null=True, blank=True)
    logo = models.ImageField(upload_to='settings/', null=True, blank=True)
    login_text = models.TextField(blank=True)
    tel = models.CharField(max_length=15, blank=True, null=True)
    mobile = models.CharField(max_length=11, blank=True, null=True)
    address = models.TextField(blank=True)
    email = models.CharField(max_length=30, blank=True, null=True)
    about_text = models.TextField(blank=True)
    footer_text = models.TextField(blank=True)
    is_active = models.BooleanField(choices=STATUS_OPEN, default=ACTIVE)

    class Meta:
        verbose_name = 'setting'
        verbose_name_plural = 'settings'

    def __str__(self):
        return self.title



class RuleCategory(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name="نام دسته‌بندی")
    description = models.TextField(null=True, blank=True, verbose_name="توضیحات")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "دسته‌بندی قانون"
        verbose_name_plural = "دسته‌بندی قوانین"


class Rule(models.Model):

    title = models.CharField(max_length=255, verbose_name="عنوان قانون")
    category = models.ForeignKey(
        RuleCategory,
        on_delete=models.CASCADE,
        related_name="rules",
        verbose_name="دسته‌بندی",
    )
    content = models.TextField(verbose_name="متن قانون")
    is_active = models.BooleanField(default=True, verbose_name="فعال بودن قانون")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ایجاد")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="تاریخ به‌روزرسانی")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "قانون"
        verbose_name_plural = "قوانین"
        ordering = ["-created_at"]