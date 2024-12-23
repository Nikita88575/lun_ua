import re

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Column, Layout, Row, Submit
from django import forms
from django.utils.translation import gettext_lazy as _

from newbuilding.models import NewBuildings, NewBuildingsPhoto, NewBuildingsProjects


class NewBuildingsForm(forms.ModelForm):
    class Meta:
        model = NewBuildings
        fields = [
            "title",
            "bio",
            "company_name",
            "company_web",
            "location",
            "district",
            "metro_station",
            "apartament_classes",
            "houses_count",
            "floors_variables",
            "construction_tec",
            "walls",
            "walls_insulation",
            "project_heating",
            "ceiling_height",
            "housing_condition",
            "apartament_count",
            "parking",
            "parking_places",
            "backup_power_supply",
            "shelter",
        ]
        labels = {
            "title": _("Title*"),
            "bio": _("Bio*"),
            "company_name": _("Company name*"),
            "company_web": _("Company web*"),
            "location": _("Location*"),
            "district": _("District*"),
            "metro_station": _("Metro station"),
            "apartament_classes": _("Apartament classes*"),
            "houses_count": _("Houses count"),
            "floors_variables": _("Floors variables*"),
            "construction_tec": _("Construction technology"),
            "walls": _("Walls"),
            "walls_insulation": _("Walls insulation"),
            "project_heating": _("Project heating"),
            "ceiling_height": _("Ceiling height*"),
            "housing_condition": _("Housing condition*"),
            "apartament_count": _("Apartament count"),
            "parking": _("Parking"),
            "parking_places": _("Parking places*"),
            "backup_power_supply": _("Reserve power supply"),
            "shelter": _("Shelter"),
        }

    def __init__(self, *args: tuple, **kwargs: dict) -> None:
        super(NewBuildingsForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = "post"
        self.helper.layout = Layout(
            Row(
                Column("title", css_class="col s12"),
                Column("bio", css_class="col s12"),
                Column("company_name", css_class="col s6"),
                Column("company_web", css_class="col s6"),
            ),
            Row(
                Column("location", css_class="col s12"),
                Column("district", css_class="col s12"),
                Column("metro_station", css_class="col s12"),
            ),
            Row(
                Column("apartament_classes", css_class="col s12"),
                Column("houses_count", css_class="col s12"),
                Column("floors_variables", css_class="col s12"),
            ),
            Row(
                Column("construction_tec", css_class="col s12"),
                Column("walls", css_class="col s12"),
                Column("walls_insulation", css_class="col s12"),
                Column("project_heating", css_class="col s12"),
            ),
            Row(
                Column("ceiling_height", css_class="col s6"),
                Column("housing_condition", css_class="col s6"),
                Column("apartament_count", css_class="col s12"),
            ),
            Row(
                Column("parking", css_class="col s6"),
                Column("parking_places", css_class="col s6"),
            ),
            Row(
                Column("backup_power_supply", css_class="col s12"),
                Column("shelter", css_class="col s12"),
            ),
        )
        self.field_order = [
            "title",
            "bio",
            "company_name",
            "company_web",
            "location",
            "district",
            "metro_station",
            "apartament_classes",
            "houses_count",
            "floors_variables",
            "construction_tec",
            "walls",
            "walls_insulation",
            "project_heating",
            "ceiling_height",
            "housing_condition",
            "apartament_count",
            "parking",
            "parking_places",
            "backup_power_supply",
            "shelter",
        ]

    def clean(self) -> dict:
        cleaned_data = super().clean()

        houses_count = cleaned_data.get("houses_count")
        floors_variables = cleaned_data.get("floors_variables")
        ceiling_height = cleaned_data.get("ceiling_height")
        apartament_count = cleaned_data.get("apartament_count")
        parking_places = cleaned_data.get("parking_places")

        if houses_count and houses_count < 1:
            self.add_error(
                "houses_count",
                _("Invalid houses count."),
            )

        if floors_variables:
            floors = list(map(int, re.findall(r"-?\d+", floors_variables)))
            min_floor, max_floor = min(floors), max(floors)

            if min_floor < 1:
                self.add_error(
                    "floors_variables",
                    _("Invalid floors variables count."),
                )

        if ceiling_height and ceiling_height < 2:
            self.add_error(
                "ceiling_height",
                _("Invalid ceiling height."),
            )

        if apartament_count and apartament_count < 1:
            self.add_error(
                "apartament_count",
                _("Invalid apartament count."),
            )

        if parking_places and parking_places < 1:
            self.add_error(
                "parking_places",
                _("Invalid parking places count."),
            )

        return cleaned_data


class NewBuildingsPhotoForm(forms.ModelForm):
    photo = forms.ImageField(required=False)

    class Meta:
        model = NewBuildingsPhoto
        fields = ["photo"]
        label = [_("Project photos")]
