from django.conf.urls import include
from django.contrib import admin
from django.contrib.auth import views as auth_views, logout
from django.urls import path

from blog import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.post_list, name="post_list"),
    path('blog/', include(('blog.urls', 'blog'), namespace="blog")),
    path('like/', views.like_post, name="like_post"),

    path('login/', views.user_login, name="user_login"),
    path('logout/', views.user_logout, name="user_logout"),
    path('register/', views.register, name="register"),

    # Password Reset Url's
    path('password_reset/', auth_views.PasswordResetView.as_view(),
         {'template_name':'registration/password_reset_form.html'}, name="password_reset"),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(),
         {'template_name':'registration/password_reset_done.html'}, name="password_reset_done"),
    path('password-reset/confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(),
         {'template_name' : 'registration/password_reset_confirm.html'}, name="password_reset_confirm"),
    path('password-reset/complete/', auth_views.PasswordResetCompleteView.as_view(),
         {'template_name' : 'registration/password_reset_complete.html'}, name="password_reset_complete"),

    # path('oauth/', include('social_django.urls', namespace="social")),
    # path('', include('social_django.urls', namespace='social')),

    # social logins url
    # path('', include('django.contrib.auth.urls')),
    # path('oauth/', include('social_django.urls', namespace="social")),
    # path('logout/', logout, {'next_page': settings.LOGOUT_REDIRECT_URL},name='logout'),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

