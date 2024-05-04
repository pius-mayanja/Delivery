
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('jumia.urls')),
    path('inbox/', include('chart.urls')),
    path('cart/', include('cart.urls')),
    path('', include('user.urls')),
    path('order/', include('orders.urls')),
    path('business/', include('business.urls')),

    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
