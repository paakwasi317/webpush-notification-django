from django.urls import path , include
from . import views
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter
# from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt import views as jwt_views
from django.conf import settings
from django.conf.urls.static import static

from Users import views

urlpatterns = [
        # path('user/login/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
        path('user/getinfo/', views.GetUserInfo, name='getUserInfo'),
        path('user/login/', views.UserLogin, name='userlogin'),
        path('user/verifycode/', views.CodeVerification, name='codeverification'),
        path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
        path('user/', views.UserList.as_view()),
        path('user/<int:pk>/', views.UserDetail.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)

# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)