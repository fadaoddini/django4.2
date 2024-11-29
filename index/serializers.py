from rest_framework import serializers

from index.models import SettingApp, RuleCategory, Rule


class SettingsSerializer(serializers.ModelSerializer):

    class Meta:
        model = SettingApp
        fields = ('id', 'title', 'description', 'favicon', 'logo', 'login_text', 'tel', 'mobile', 'address', 'email',
                  'about_text', 'footer_text', 'is_active')



class RuleCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = RuleCategory
        fields = ['id', 'name', 'description']


class RuleSerializer(serializers.ModelSerializer):
    category = RuleCategorySerializer()  # برای نمایش جزئیات دسته‌بندی

    class Meta:
        model = Rule
        fields = ['id', 'title', 'category', 'content', 'is_active', 'created_at', 'updated_at']


class RuleCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rule
        fields = ['id', 'title', 'category', 'content', 'is_active']