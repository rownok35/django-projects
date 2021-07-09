from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls', namespace='home')),
    path('property/', include('property.urls', namespace='property')),
    path('agents/', include('agents.urls', namespace='agents')),
    path('about/', include('about.urls', namespace='about')),
    path('contact/', include('contact.urls', namespace='contact'))
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = "HOTEL RESERVATION ADMIN"
admin.site.site_title = "HOTEL RESERVATION ADMIN"
admin.site.site_index_title = "Welcome To Hotel Reservation Admin"
