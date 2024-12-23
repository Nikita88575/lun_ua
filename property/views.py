from django.conf import settings
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.paginator import Paginator
from django.http import HttpRequest, HttpResponse, HttpResponseForbidden
from django.shortcuts import get_object_or_404, redirect, render
from django.utils.translation import gettext_lazy as _
from django.views import View
from django.views.generic import DeleteView

from property.models import Apartaments, Houses, Properties
from users.models import LunUser, RieltorWorkShedule


class PropertyListView(View):
    template_name = "property/property_list.html"

    def get(self, request: HttpRequest) -> HttpResponse:
        offers = Properties.objects.filter(is_active=True).order_by("-created_at")

        user = LunUser.objects.filter(username=self.request.user.username).first()

        paginator = Paginator(offers, settings.OFFERS_PAGINATION_PER_PAGE)

        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)

        return render(request, self.template_name, {"user": user, "page_obj": page_obj})


class PropertyDetailsView(View):
    template_name = "property/property_details.html"

    def get(self, request: HttpRequest, property_slug: str) -> HttpResponse:
        user = LunUser.objects.filter(username=self.request.user.username)

        return render(
            request,
            self.template_name,
            {"user": user},
        )
