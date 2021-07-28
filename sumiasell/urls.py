from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from sumiacart.views import OrdersListView
from sumiacart.views import RefundView
from sumiacheckout.views import ShippingAddressUpdateView


urlpatterns = [
    path('', include('sumiaproducts.urls')),
    path('cart/', include('sumiacart.urls')),
    path('checkout/', include('sumiacheckout.urls')),
    path('accounts/', include('allauth.urls')),
    path('admin/', admin.site.urls),
    path('accounts/orders/', OrdersListView.as_view(), name='show-orders'),
    path('accounts/profile/', ShippingAddressUpdateView.as_view(), name='profile'),
    path('refund/', RefundView.as_view(), name='refund')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)