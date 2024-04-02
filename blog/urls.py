from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
# API to Post a Comment

    path('postComment', views.postComment, name="postComment"),

    # path('admin/', admin.site.urls),
    path('', views.blogHome, name="bloghome"),
    path('<str:slug>', views.blogPost, name="blogPost"),


]
