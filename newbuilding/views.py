from django.conf import settings
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.paginator import Paginator
from django.db.models import F, IntegerField, Max, Min, OuterRef, Subquery
from django.db.models.functions import Cast
from django.http import HttpRequest, HttpResponse, HttpResponseForbidden
from django.shortcuts import get_object_or_404, redirect, render
from django.utils.translation import gettext_lazy as _
from django.views import View

from newbuilding.forms import NewBuildingsForm, NewBuildingsPhotoForm
from newbuilding.models import NewBuildings, NewBuildingsPhoto, NewBuildingsProjects
from users.models import LunUser, RieltorWorkShedule


class NewBuildingListView(View):
    template_name = "newbuildings/newbuildings_list.html"

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
            .order_by("-updated_at")
        )

        user = LunUser.objects.filter(username=self.request.user.username).first()

        paginator = Paginator(buildings, settings.OFFERS_PAGINATION_PER_PAGE)

        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)

        return render(request, self.template_name, {"user": user, "page_obj": page_obj})


class NewBuildingDetailsView(View):
    template_name = "newbuildings/newbuildings_details.html"

    def get(self, request: HttpRequest, newbuilding_slug: str) -> HttpResponse:
        project = get_object_or_404(NewBuildings, slug=newbuilding_slug, is_active=True)
        project_info = (
            NewBuildingsProjects.objects.filter(offer_id=project.id)
            .values("apartament_type")
            .annotate(
                min_price=Min(
                    F("price_per_sqrm") * F("area"), output_field=IntegerField()
                ),
                max_price=Max(
                    F("price_per_sqrm") * F("area"), output_field=IntegerField()
                ),
                min_area=Min("area"),
                max_area=Max("area"),
            )
            .order_by("apartament_type")
        )

        photos = NewBuildingsPhoto.objects.filter(offer_id=project.id)
        rieltor = get_object_or_404(LunUser, id=project.rieltor.id)

        user = LunUser.objects.filter(username=self.request.user.username).first()
        shedule = RieltorWorkShedule.objects.filter(user_id=rieltor.id)

        newbuilding_form = NewBuildingsForm(instance=project)

        return render(
            request,
            self.template_name,
            {
                "user": user,
                "project": project,
                "info": project_info,
                "photos": photos,
                "rieltor": rieltor,
                "shedule": shedule,
                "newbuilding_form": newbuilding_form,
            },
        )

    def post(self, request: HttpRequest, newbuilding_slug: str) -> HttpResponse:
        project = get_object_or_404(NewBuildings, slug=newbuilding_slug)
        project_info = NewBuildingsProjects.objects.filter(offer_id=project.id)

        newbuilding_form = NewBuildingsForm(request.POST, instance=project)

        if newbuilding_form.is_valid():
            if "delete" in request.POST:
                project.delete()
                project_info.delete()
                messages.success(request, _("Deleted successfully"))
                return redirect("newbuilding:list")

            elif "edit" in request.POST:
                edit_newbuilding = newbuilding_form.save(commit=False)
                edit_newbuilding.save()
                messages.success(request, _("Upadated succwssfully"))
                return redirect(project.get_absolute_url())


class NewBuildingCreateView(LoginRequiredMixin, UserPassesTestMixin, View):
    template_name = "newbuildings/newbuildings_create.html"

    def test_func(self) -> bool:
        username = self.request.user.username
        user = get_object_or_404(LunUser, username=username)
        return user.is_rieltor == True

    def get(self, request: HttpRequest) -> HttpResponse:
        form = NewBuildingsForm()

        return render(request, self.template_name, {"form": form})

    def post(self, request: HttpRequest) -> HttpResponse:
        form = NewBuildingsForm(request.POST)

        if form.is_valid():
            newbuilding = form.save(commit=False)
            newbuilding.rieltor = self.request.user
            newbuilding.save()
            messages.success(request, _("Created successfully"))
            return redirect(newbuilding.get_absolute_url())

        return render(request, self.template_name, {"form": form})


class NewBuildingUpdateView(LoginRequiredMixin, UserPassesTestMixin, View):
    template_name = "newbuildings/newbuildings_update.html"

    def test_func(self) -> bool:
        user = get_object_or_404(LunUser, username=self.request.user.username)
        return user.is_rieltor == True

    def get(self, request: HttpRequest, newbuilding_slug: str) -> HttpResponse:
        user = get_object_or_404(LunUser, username=self.request.user.username)
        project = get_object_or_404(NewBuildings, slug=newbuilding_slug)
        form = NewBuildingsForm(instance=project)

        if user.id != project.rieltor.id:
            return redirect("newbuilding:details", newbuilding_slug=project.slug)

        return render(request, self.template_name, {"form": form})

    def post(self, request: HttpRequest, newbuilding_slug: str) -> HttpResponse:
        project = get_object_or_404(NewBuildings, slug=newbuilding_slug)
        form = NewBuildingsForm(request.POST, instance=project)

        if form.is_valid():
            newbuilding = form.save(commit=False)
            newbuilding.rieltor = self.request.user
            newbuilding.save()
            messages.success(request, _("Updated successfully"))
            return redirect(newbuilding.get_absolute_url())

        return render(request, self.template_name, {"form": form})


class NewBuildingProjectDetailsView(View):
    template_name = "newbuildings/newbuildings_project_details.html"

    def get(
        self, request: HttpRequest, newbuilding_slug: str, rooms_count: str
    ) -> HttpResponse:

        project = get_object_or_404(NewBuildings, slug=newbuilding_slug)
        projects = NewBuildingsProjects.objects.filter(
            offer_id=project.id, apartament_type=rooms_count
        )

        return render(request, self.template_name)
