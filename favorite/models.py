from django.db import models


# Create your models here.
class NewBuildingsProjectsFavorite(models.Model):
    user = models.ForeignKey(
        "users.LunUser", on_delete=models.CASCADE, related_name="user"
    )
    offer = models.ForeignKey(
        "newbuilding.NewBuildings", on_delete=models.CASCADE, related_name="offer_count"
    )
    project = models.ForeignKey(
        "newbuilding.NewBuildingsProjects",
        on_delete=models.CASCADE,
        related_name="project_count",
    )

    class Meta:
        db_table = "project_favorite"
        verbose_name = "Favorite Project"
        verbose_name_plural = "Favorite Projects"
