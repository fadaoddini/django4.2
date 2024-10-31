from rest_framework import serializers

from catalogue.models import Product
from .models import Bid


class BidSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    mobile = serializers.SerializerMethodField()
    sellbuy = serializers.SerializerMethodField()
    total = serializers.SerializerMethodField()
    image_url = serializers.SerializerMethodField()
    rank = serializers.SerializerMethodField()

    class Meta:
        model = Bid
        fields = ['product', 'price', 'user', 'result', 'mobile', 'sellbuy', 'total', 'image_url', 'weight', 'rank']

    def get_image_url(self, obj):
        request = self.context.get('request')  # گرفتن request از context
        if obj.user.image and request:
            return request.build_absolute_uri(obj.user.image.url)  # ایجاد URL کامل
        return None

    def get_user(self, obj):
        if (obj.user.first_name == "" and obj.user.last_name == ""):
            return "ناشناس"
        return f"{obj.user.first_name} {obj.user.last_name}"

    def get_mobile(self, obj):
        return obj.user.mobile

    def get_sellbuy(self, obj):
        return obj.product.sell_buy

    def get_total(self, obj):
        return obj.weight * obj.price

    def get_rank(self, obj):
        related_bids = Bid.objects.filter(product=obj.product)

        if obj.product.sell_buy == Product.SELL:
            # برای فروش: ترتیب صعودی
            rank = related_bids.filter(price__gt=obj.price).count() + 1
        else:
            # برای خرید: ترتیب نزولی
            rank = related_bids.filter(price__lt=obj.price).count() + 1

        return rank


