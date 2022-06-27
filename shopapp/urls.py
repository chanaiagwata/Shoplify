from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path(r'', views.index, name = 'indexpage'),
    path('accounts/profile/',views.profile,name = 'profile'),
    path(r'update_profile', views.update_profile, name='update'),
    path(r'search/', views.search_product, name='search_product'),
    path('product/',views.product,name = 'product'),

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)