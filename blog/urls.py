from django.conf.urls import url
from django.urls import path

from blog import views

urlpatterns = [
    path('(<id>/post_edit/', views.post_edit, name="post_edit"),
    path('(<id>/post_delete/', views.post_delete, name="post_delete"),
    path('<id>/<slug>/', views.post_detail, name="post_detail"),
    path('post_create/', views.post_create, name="post_create"),
    path('edit_profile/', views.edit_profile, name="edit_profile"),
    # url(r'(?P<id>\d+)/favourite_post/$', views.favourite_post, name="favourite_post"),
    # url(r'favourites/$', views.post_favourite_list, name="post_favourite_list"),

]
