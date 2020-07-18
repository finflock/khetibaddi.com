from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include

from .routers import router
from api.rest_auth_viewsets import (LoginView, LogoutView, PasswordResetView,
                                    PasswordResetConfirmView, PasswordChangeView)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/v1/', include(router.urls)),
    url(r'^api/v1/rest-auth/password/reset/$', PasswordResetView.as_view(),
        name='rest_password_reset'),
    url(r'^api/v1/rest-auth/password/reset/confirm/$', PasswordResetConfirmView.as_view(),
        name='rest_password_reset_confirm'),
    url(r'^api/v1/rest-auth/login/$', LoginView.as_view(), name='rest_login'),
    url(r'^api/v1/rest-auth/logout/$', LogoutView.as_view(), name='rest_logout'),
    url(r'^api/v1/rest-auth/password/change/$', PasswordChangeView.as_view(),
        name='rest_password_change'),
]
