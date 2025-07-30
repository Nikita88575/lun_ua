from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.paginator import Paginator
from django.db.models import Exists, F, IntegerField, Max, Min, OuterRef
from django.db.models.functions import Cast
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.template.loader import render_to_string
from django.utils.translation import gettext_lazy as _
from django.views import View

from favorite.models import NewBuildingsProjectsFavorite
from newbuilding.models import NewBuildingsProjects
from users.forms import LunUserForm
from users.models import LunUser


class ProfileView(LoginRequiredMixin, UserPassesTestMixin, View):
    template_name = "user/user_details.html"
    ui_template_name = "ui/user/favorite_projects_list.html"

    def test_func(self) -> bool:
        profile_slug = self.kwargs.get("profile")
        profile = get_object_or_404(LunUser, username=profile_slug)
        return profile.username == self.request.user.username

    def get(self, request: HttpRequest, profile: str) -> HttpResponse:
        user = get_object_or_404(LunUser, username__iexact=profile)

        favorite = NewBuildingsProjectsFavorite.objects.filter(
            user=user, project=OuterRef("pk")
        ).values("project")

        projects = (
            NewBuildingsProjects.objects.annotate(is_favorited=Exists(favorite))
            .filter(is_favorited=True)
            .annotate(
                project_price=Cast(
                    F("price_per_sqrm") * F("area"), output_field=IntegerField()
                ),
                min_price=Min(
                    F("price_per_sqrm") * F("area"), output_field=IntegerField()
                ),
                max_price=Max(
                    F("price_per_sqrm") * F("area"), output_field=IntegerField()
                ),
                min_price_per_sqrm=Min("price_per_sqrm"),
                max_price_per_sqrm=Max("price_per_sqrm"),
            )
            .order_by("apartament_type")
        )

        user_form = LunUserForm(instance=user)

        paginator = Paginator(projects, settings.OFFERS_PAGINATION_PER_PAGE)
        page_number = request.GET.get("page", 1)
        page_obj = paginator.get_page(page_number)

        context = {
            "user": user,
            "user_form": user_form,
            "page_obj": page_obj,
            "has_next": page_obj.has_next(),
        }

        if request.headers.get("x-requested-with") == "XMLHttpRequest":
            html = render_to_string(self.ui_template_name, context, request)
            return JsonResponse({"html": html, "has_next": page_obj.has_next()})

        return render(request, self.template_name, context)

    def post(self, request: HttpRequest, profile: str) -> HttpResponse:

        user = get_object_or_404(LunUser, username__iexact=profile)
        user_form = LunUserForm(request.POST, instance=user)

        if user_form.is_valid():
            edit_profile = user_form.save(commit=False)
            edit_profile.save()
            return redirect("users:profile", profile=user.username)
