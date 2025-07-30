from django.urls import path

from .views import NewBuildingProjectAddToFavorite

app_name = "favorite"

urlpatterns = [
    path(
        "<int:project_id>/",
        NewBuildingProjectAddToFavorite.as_view(),
        name="add-to-favorite",
    ),
]
