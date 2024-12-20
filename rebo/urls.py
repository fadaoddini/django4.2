from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bid/', include('bid.urls')),
    path('info/', include('info.urls')),
    path('transaction/', include('transaction.urls')),
    path('company/', include('company.urls')),
    path('learn/', include('learn.urls')),
    path('transport/', include('transport.urls')),
    path('hoghoogh/', include('hoghoogh.urls')),
    path('order/', include('order.urls')),
    path('', include('index.urls')),
    path('login/', include('login.urls')),
    path('catalogue/', include('catalogue.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
