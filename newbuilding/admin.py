from django.contrib import admin

from newbuilding.models import NewBuildings, NewBuildingsPhoto, NewBuildingsProjects

# Register your models here.
admin.site.register(NewBuildings)
admin.site.register(NewBuildingsPhoto)
admin.site.register(NewBuildingsProjects)
