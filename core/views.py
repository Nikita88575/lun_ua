# Create your views here.
from django.db.models import F, IntegerField, OuterRef, Subquery
from django.db.models.functions import Cast
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.utils.translation import gettext_lazy as _
from django.views import View

from favorite.models import NewBuildingsProjectsFavorite
from newbuilding.models import NewBuildings, NewBuildingsPhoto, NewBuildingsProjects
from users.models import LunUser


class HomePageView(View):
    template_name = "home.html"

    def get(self, request: HttpRequest) -> HttpResponse:
        latest_building = (
            NewBuildingsProjects.objects.filter(
                offer_id=OuterRef("id"),
                solded=False,
            )
            .annotate(
                min_price_value=Cast(
                    F("price_per_sqrm") * F("area"), output_field=IntegerField()
                )
            )
            .order_by("min_price_value")
        )

        buildings = (
            NewBuildings.objects.all()
            .annotate(
                min_price_value=Subquery(
                    latest_building.filter(offer_id=OuterRef("id")).values(
                        "min_price_value"
                    )[:1]
                ),
                image=Subquery(
                    NewBuildingsPhoto.objects.filter(offer=OuterRef("id"))
                    .order_by("id")
                    .values("photo")[:1]
                ),
            )
            .order_by("?")[:4]
        )

        user = LunUser.objects.filter(username=self.request.user.username)

        return render(
            request, self.template_name, {"user": user, "buildings": buildings}
        )
