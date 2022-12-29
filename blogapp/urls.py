
from django.contrib import admin
from django.urls import path
from blogapp import views

urlpatterns = [
    path("viewblog/",views.viewblog, name="/blogapp/viewblog/"),
    path("newpost/",views.CreatePost.as_view(),name="/blogapp/newpost/"),
    path("signup/",views.signup,name="/blogapp/signup/"),
]