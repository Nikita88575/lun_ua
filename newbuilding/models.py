from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.templatetags.static import static
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from core.models import SlugModel


# Create your models here.
class NewBuildings(SlugModel):
    APARTAMENTS_CLASSES = (
        (_("Econom"), _("Econom")),
        (_("Comfort"), _("Comfort")),
        (_("Buisnes"), _("Buisnes")),
        (_("Luxury"), _("Luxury")),
    )
    APARTAMENTS_RENOVATIONS = (
        (_("With renovation"), _("With renovation")),
        (_("Without renovation"), _("Without renovation")),
        (
            _("With renovation, Without renovation"),
            _("With renovation, Without renovation"),
        ),
    )
    title = models.CharField(max_length=128)
    bio = RichTextUploadingField(max_length=1024)
    location = models.CharField(max_length=50)
    district = models.CharField(max_length=256)
    metro_station = models.CharField(max_length=50, null=True, blank=True)
    company_name = models.CharField(max_length=128)
    company_web = models.URLField(max_length=512)
    apartament_classes = models.CharField(choices=APARTAMENTS_CLASSES)
    houses_count = models.IntegerField(null=True, blank=True)
    floors_variables = models.CharField(null=True)
    construction_tec = models.CharField(max_length=50, null=True, blank=True)
    walls = models.CharField(max_length=50, null=True, blank=True)
    walls_insulation = models.CharField(max_length=100, null=True, blank=True)
    project_heating = models.CharField(max_length=100, null=True, blank=True)
    ceiling_height = models.FloatField(null=True)
    apartament_count = models.IntegerField(null=True)
    housing_condition = models.CharField(choices=APARTAMENTS_RENOVATIONS)
    parking = models.CharField(max_length=100, null=True, blank=True)
    parking_places = models.IntegerField(null=True)
    backup_power_supply = models.CharField(max_length=100, null=True, blank=True)
    shelter = models.CharField(max_length=100, null=True, blank=True)
    first_apartamen_floor = models.IntegerField(null=True, blank=True)
    last_apartamen_floor = models.IntegerField(null=True, blank=True)
    rieltor = models.ForeignKey("users.LunUser", on_delete=models.CASCADE)
    company_image = models.ImageField(
        upload_to="companies_logos/", null=True, blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = "new_buildings"
        verbose_name = "New Building"
        verbose_name_plural = "New Buildings"

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self) -> str:
        return reverse("newbuilding:details", kwargs={"newbuilding_slug": self.slug})


class NewBuildingsPhoto(models.Model):
    offer = models.ForeignKey(
        "NewBuildings", on_delete=models.CASCADE, related_name="photos"
    )
    photo = models.ImageField(upload_to="company_project/", null=True, blank=True)

    class Meta:
        db_table = "new_buildings_photos"
        verbose_name = "New Building Photo"
        verbose_name_plural = "New Buildings Photos"

    def get_image_url(self) -> str:
        if self.offer and self.photo:
            return self.photo.url
        else:
            return static("images/default_render_uk.png")


class NewBuildingsProjects(models.Model):
    CHOICES = (
        (_("1-room"), _("1-room")),
        (_("2-room"), _("2-room")),
        (_("3-room"), _("3-room")),
        (_("4-room"), _("4-room")),
        (_("5-room"), _("5-room")),
    )
    STATES = (
        (_("Builded"), _("Builded")),
        (_("Build"), _("Build")),
    )
    offer = models.ForeignKey(
        "NewBuildings", on_delete=models.CASCADE, related_name="rieltor_offer"
    )
    apartament_type = models.CharField(choices=CHOICES)
    state = models.CharField(choices=STATES)
    price_per_sqrm = models.IntegerField(null=True, blank=True)
    area = models.FloatField(null=True, blank=True)
    solded = models.BooleanField(default=False)
    apartamen_floor = models.CharField(null=True, blank=True)
    last_apartamen_floor = models.IntegerField(null=True, blank=True)
    apartamen_number = models.CharField(null=True, blank=True)
    final_build_date = models.DateField(null=True, blank=True)
    aprtament_bedrooms_count = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = "new_buildings_projects"
        verbose_name = "New Building Project"
        verbose_name_plural = "New Buildings Projects"
