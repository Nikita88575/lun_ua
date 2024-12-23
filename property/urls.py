from django.urls import path

from .views import PropertyDetailsView, PropertyListView

app_name = "property"

urlpatterns = [
    path("", PropertyListView.as_view(), name="list"),
    path("<slug:property_slug>/", PropertyDetailsView.as_view(), name="details"),
]
