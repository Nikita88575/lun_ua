# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, HttpResponse, HttpResponseForbidden
from django.shortcuts import get_object_or_404, render
from django.views import View

from newbuilding.models import NewBuildingsProjects

from .models import NewBuildingsProjectsFavorite


class NewBuildingProjectAddToFavorite(LoginRequiredMixin, View):
    ui_template_name = "ui/favorite/add_to_favorite.html"

    def post(self, request: HttpRequest, project_id: int) -> HttpResponse:
        if not request.user.is_authenticated:
            # respone status 403
            return HttpResponseForbidden("You must be logged in")

        project = get_object_or_404(NewBuildingsProjects, id=project_id)

        favorite = NewBuildingsProjectsFavorite.objects.filter(
            user=request.user,
            project=project,
            offer=project.offer,
        )

        if not favorite:
            NewBuildingsProjectsFavorite.objects.create(
                user=request.user,
                project=project,
                offer=project.offer,
            )
        else:
            favorite.delete()

        return render(
            request,
            self.ui_template_name,
            {"project": project, "user": request.user},
        )
