from django.contrib import admin
from django.urls import path
from .views import home, contact

urlpatterns = [
    path('admin/', admin.site.urls),
]
