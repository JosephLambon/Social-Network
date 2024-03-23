
from django.urls import path

from . import views

from .views import update_post, like_post, unlike_post

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("profile/<int:profile_id>/", views.profile, name="profile"),
    path("new_post/<int:user_id>/", views.new_post, name="new_post"),
    path("follow/<int:user_id>/<int:profile_id>", views.follow, name="follow"),
    path("unfollow/<int:user_id>/<int:profile_id>", views.unfollow, name="unfollow"),
    path("following", views.following, name="following"),
    path("update-post/", update_post, name="update_post"),
    path("like-post/", like_post, name="like_post"),
    path("unlike-post/", unlike_post, name="unlike_post")
]
