from django.urls import re_path
from github import views


urlpatterns = [
    re_path(r'^Authors/$', views.Authors.as_view()),
    re_path(r'^Books/$', views.Books.as_view()),
    re_path(r'^Authors/(?P<name>[a-zA-Z0-9_-]{2,20})/$', views.AuthorsOL.as_view()),
    re_path(r'^Books/(?P<bookname>[a-zA-Z0-9_-]{2,20})/$', views.BooksOL.as_view()),

]