# from django import urls
from django.urls import path

from . import views
app_name = "encyclopedia"
urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/search",views.search, name= "search"),
    path("wiki/create_entry", views.create_entry, name="create_entry"),
    path("<str:title>", views.view_entry, name='view_entry'),
    path("wiki/edit_entry/<str:title>", views.edit_entry, name="edit_entry"),
    path("wiki/save_and_view",views.save_and_view, name = "save_and_view"),
    path("wiki/random_page",views.random_page,name = "random_page")
    
    # path("create_entry",)
    
]
