from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.templatetags.static import static
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from core.models import SlugModel


# Create your models here.
class Properties(SlugModel):
    title = models.CharField(max_length=128)
    bio = RichTextUploadingField(max_length=1024)
    rieltor = models.ForeignKey("users.LunUser", on_delete=models.CASCADE)
    location = models.CharField(max_length=50)
    address = models.CharField(max_length=256)
    price = models.IntegerField(null=True, blank=True)
    area = models.FloatField(null=True, blank=True)
    bedrooms_count = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = "property"
        verbose_name = "Property"
        verbose_name_plural = "Properties"

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self) -> str:
        return reverse("property:details", kwargs={"property_slug": self.slug})


class Houses(models.Model):
    STATES = (
        (_("builded"), _("builded")),
        (_("build"), _("build")),
    )
    offer = models.OneToOneField(
        "Properties", on_delete=models.CASCADE, related_name="house"
    )
    house_state = models.CharField(choices=STATES)
    floors_count = models.IntegerField(null=True)

    class Meta:
        db_table = "houses"
        verbose_name = "House"
        verbose_name_plural = "Houses"


class Apartaments(models.Model):
    CHOICES = (
        (_("1-room"), _("1-room")),
        (_("2-room"), _("2-room")),
        (_("3-room"), _("3-room")),
        (_("4-room"), _("4-room")),
        (_("5-room"), _("5-room")),
    )
    offer = models.OneToOneField(
        "Properties", on_delete=models.CASCADE, related_name="apartament"
    )
    apartament_type = models.CharField(choices=CHOICES)
    station = models.CharField(max_length=50, null=True, blank=True)
    floor = models.IntegerField()

    class Meta:
        db_table = "apartaments"
        verbose_name = "Apartament"
        verbose_name_plural = "Apartaments"


class PropertyPhoto(models.Model):
    offer = models.ForeignKey(
        "Properties", on_delete=models.CASCADE, related_name="property_property"
    )
    photo = models.ImageField(upload_to="property/", null=True, blank=True)

    class Meta:
        db_table = "property_photos"
        verbose_name = "Property Photo"
        verbose_name_plural = "Properties Photos"

    def get_image_url(self) -> str:
        if self.offer and self.photo:
            return self.photo.url
        else:
            return static("images/default_render_uk.png")
