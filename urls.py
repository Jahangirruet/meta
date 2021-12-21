from django.contrib import admin
from django.urls import include, path
from django.conf import settings

urlpatterns = [
    path('', include('facebook.urls')),
    path('admin/', admin.site.urls),
]