from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView
from users import views

router = DefaultRouter()

urlpatterns = [
    # path('', include(router.urls)),
    path('auth/', include('rest_framework.urls', namespace="rest_framework")),
    path("customersignupapi/", views.CustomerSignupApi.as_view(),name='customersignup'),
    path("customerprofileapi/<int:pk>/", views.CustomerProfileUpdate.as_view(),name='customerprofile'),
    path("customerpasswordupdateapi/<int:pk>/", views.CustomerPasswordUpdate.as_view(),name='customerpasswordupdate'),
    path("loginapi/", views.MyTokenObtainPairviewApi.as_view(),name='login'),
    path("refreshtokenapi/", TokenRefreshView.as_view(),name='refreshtoken'),
    path("restaurantownersignupapi/", views.RestaurantOwnerSignupApi.as_view(),name='restaurantownersignup'),
    path("restaurantownerprofileapi/<int:pk>/", views.RestaurantOwnerProfileUpdate.as_view(),name='restaurantownerprofile'),
    path("restaurantownerpasswordupdateapi/<int:pk>/", views.RestaurantOwnerPasswordUpdate.as_view(),name='restaurantownerpasswordupdate'),
]

