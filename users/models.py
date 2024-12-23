from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.templatetags.static import static
from django_resized import ResizedImageField


class LunUser(AbstractUser):
    bio = RichTextUploadingField(max_length=500, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    is_rieltor = models.BooleanField(default=False)
    phone_number = models.CharField(null=True, blank=True)
    avatar = ResizedImageField(
        size=[256, 256], null=True, blank=True, upload_to="avatars/"
    )

    def get_avatar_url(self) -> str:
        if self.avatar:
            return self.avatar.url
        else:
            return static("images/default_avatar.png")


class RieltorWorkShedule(models.Model):
    user = models.ForeignKey(
        "LunUser", on_delete=models.CASCADE, related_name="work_shedule"
    )
    workdays_starts_at = models.TimeField(null=True, blank=True)
    workdays_ends_at = models.TimeField(null=True, blank=True)
    weekend_starts_at = models.TimeField(null=True, blank=True)
    workend_ends_at = models.TimeField(null=True, blank=True)

    class Meta:
        db_table = "work_shedule"
        verbose_name = "Work Shedule"
        verbose_name_plural = "Work Shedules"
