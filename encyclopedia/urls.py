from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<name_of_title>", views.get_by_title, name="title"),
    path("/edit/<entry>", views.edit_entry, name="edit"),
    path("/create", views.create_entry2, name="create"),
    path("/search_results/<substring>", views.search_results, name="search")

]
