from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from shop import views
from django.conf import settings
from django.conf.urls.static import static

router = DefaultRouter()
router.register(r'products', views.ProductViewSet)
router.register(r'orders', views.OrderViewSet)
router.register(r'customers', views.CustomerViewSet)
router.register(r'contactmessaage',views.CreateContactMessageViewSet)
router.register(r'contact',views.CreateContactViewSet)
router.register(r'profile',views.ProfileDetailViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)