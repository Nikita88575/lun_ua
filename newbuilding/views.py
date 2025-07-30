from django.conf import settings
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.paginator import Paginator
from django.db.models import Exists, F, IntegerField, Max, Min, OuterRef, Subquery
from django.db.models.functions import Cast
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.template.loader import render_to_string
from django.templatetags.static import static
from django.utils.translation import gettext_lazy as _
from django.views import View

from favorite.models import NewBuildingsProjectsFavorite
from newbuilding.forms import NewBuildingsForm
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
                min_price_per_sqrm=Min("price_per_sqrm"),
                max_price_per_sqrm=Max("price_per_sqrm"),
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
                min_price_per_sqrm=Min("price_per_sqrm"),
                max_price_per_sqrm=Max("price_per_sqrm"),
            )
            .order_by("apartament_type")
        )
        photos = NewBuildingsPhoto.objects.filter(offer_id=project.id)
        rieltor = get_object_or_404(LunUser, id=project.rieltor.id)
        user = LunUser.objects.filter(username=self.request.user.username).first()
        shedule = RieltorWorkShedule.objects.filter(user_id=rieltor.id)

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
    ui_template_name = "ui/newbuildings/newbuildings_project_details_list.html"

    def get(
        self, request: HttpRequest, newbuilding_slug: str, rooms_count: str
    ) -> HttpResponse:

        project = get_object_or_404(NewBuildings, slug=newbuilding_slug)

        area_from = request.GET.get("area_from")
        area_to = request.GET.get("area_to")

        projects = NewBuildingsProjects.objects.filter(
            offer_id=project.id, apartament_type=rooms_count
        ).annotate(
            project_price=Cast(
                F("price_per_sqrm") * F("area"), output_field=IntegerField()
            ),
            is_favorited=Exists(
                NewBuildingsProjectsFavorite.objects.filter(
                    user=self.request.user, project=OuterRef("pk")
                )
            ),
        )

        area_min = projects.aggregate(Min("area"))["area__min"]
        area_max = projects.aggregate(Max("area"))["area__max"]

        area_from_val = int(area_from) if area_from else area_min
        area_to_val = int(area_to) if area_to else area_max

        if area_from:
            projects = projects.filter(area__gte=area_from)
        if area_to:
            projects = projects.filter(area__lte=area_to)

        paginator = Paginator(
            projects.order_by("-created_at"), settings.OFFERS_PAGINATION_PER_PAGE
        )
        page_number = request.GET.get("page", 1)
        page_obj = paginator.get_page(page_number)

        context = {
            "new_building": project,
            "page_obj": page_obj,
            "rooms_count": rooms_count,
            "area_min": area_min,
            "area_max": area_max,
            "area_from": area_from_val,
            "area_to": area_to_val,
        }

        if request.headers.get("x-requested-with") == "XMLHttpRequest":
            html = render_to_string(self.ui_template_name, context, request)
            return JsonResponse({"html": html, "has_next": page_obj.has_next()})

        return render(request, self.template_name, context)


class NewBuildingProjectDetailsModalView(View):
    ui_template_name = "ui/newbuildings/project_details_modal_window.html"

    def get(
        self,
        request: HttpRequest,
        newbuilding_slug: str,
        rooms_count: str,
        room_id: int,
    ) -> HttpResponse:
        project = get_object_or_404(NewBuildings, slug=newbuilding_slug)
        project_info = get_object_or_404(
            NewBuildingsProjects.objects.annotate(
                project_price=Cast(
                    F("price_per_sqrm") * F("area"), output_field=IntegerField()
                )
            ),
            offer_id=project.id,
            apartament_type=rooms_count,
            id=room_id,
        )
        project_images = [
            static("images/image.png"),
            static("images/image.png"),
            static("images/image.png"),
        ]

        if request.headers.get("x-requested-with") == "XMLHttpRequest":
            html = render_to_string(
                self.ui_template_name,
                {"project": project_info, "project_images": project_images},
                request,
            )
            return HttpResponse(html)

        return redirect(
            "newbuilding:project-details",
            newbuilding_slug=newbuilding_slug,
            rooms_count=rooms_count,
        )
