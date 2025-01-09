
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from users import views


router = DefaultRouter()


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users.urls'))
]
