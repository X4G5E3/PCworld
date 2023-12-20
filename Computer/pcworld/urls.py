from django.urls import path
from pcworld.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('service/', service, name='service'),
    path('works/', works, name='works'),
    path('service/upgrade/', upgrade, name='upgrade'),
    path('service/repair/', repair, name='repair'),
    path('service/modding/', modding, name='modding'),
    path('service/trade/', trade, name='trade'),
    path('register/', register, name='register'),
    path('login/', UserAuthForm.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('products/', products ,name='products'),
    path('products/<slug:product_slug>/', product ,name='product'),
    path('components/',components ,name='components'),
    path('component/<slug:component_slug>',component ,name='component'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)