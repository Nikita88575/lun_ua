from django.urls import path

from .views import (
    NewBuildingCreateView,
    NewBuildingDetailsView,
    NewBuildingListView,
    NewBuildingProjectDetailsView,
    NewBuildingUpdateView,
)

app_name = "newbuilding"

urlpatterns = [
    path("create/", NewBuildingCreateView.as_view(), name="create"),
    path(
        "update/<slug:newbuilding_slug>/",
        NewBuildingUpdateView.as_view(),
        name="update",
    ),
    path("", NewBuildingListView.as_view(), name="list"),
    path("<slug:newbuilding_slug>/", NewBuildingDetailsView.as_view(), name="details"),
    path(
        "<slug:newbuilding_slug>/<str:rooms_count>/",
        NewBuildingProjectDetailsView.as_view(),
        name="project-details",
    ),
]
