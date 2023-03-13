from rest_framework.authtoken import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.urls import path
from users.views.register import RegisterView

urlpatterns = [
    path('register/', RegisterView.as_view() ,name='auth_register'),
    path('bareaer-token/', views.obtain_auth_token),
    path('jwt-token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('jwt-token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]