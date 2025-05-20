from django.urls import path

from properties.views import PropertyDetailsView, PropertyListView

app_name = "properties"

urlpatterns = [
    path("", PropertyListView.as_view(), name="list"),
    path("<slug:property_slug>/", PropertyDetailsView.as_view(), name="details"),
]
