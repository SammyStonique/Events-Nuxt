
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path,include
from Users import views as user_views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import (
    # TokenObtainPairView,
    TokenRefreshView,
)
from Users.views import MyTokenObtainPairView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='Users/password_reset.html'), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='Users/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="Users/password_reset_confirm.html"), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='Users/password_reset_complete.html'), name='password_reset_complete'),      
    path('login/', auth_views.LoginView.as_view(template_name = 'Users/user_login.html'),name= 'login'),
    path('logout/', auth_views.LogoutView.as_view(template_name = 'Users/logout.html'),name= 'logout'),
    path('api/v1/',include('Users.urls')),
    path('api/v1/',include('Events.urls')),
    path('api/v1/',include('Guest.urls')),
    path('api/v1/',include('djoser.urls')),
    path('api/v1/', include('djoser.urls.jwt')),
    # path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
if settings.DEBUG :
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

