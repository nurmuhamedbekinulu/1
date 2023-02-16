from django.urls import path
from webapp.views.base import index_view
from webapp.views.articles import add_view, detail_view


urlpatterns =[
    path("", index_view),
    path("article/add/", add_view),
    path("article/", detail_view)
]