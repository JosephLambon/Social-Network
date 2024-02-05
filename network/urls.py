
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("profile/<int:profile_id>/", views.profile, name="profile"),
    path("new_post/<int:user_id>/", views.new_post, name="new_post"),
    path("follow/<int:user_id>/<int:profile_id>", views.follow, name="follow"),
    path("unfollow/<int:user_id>/<int:profile_id>", views.unfollow, name="unfollow")
]
