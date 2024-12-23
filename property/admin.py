from django.contrib import admin

from property.models import Apartaments, Houses, Properties, PropertyPhoto

# Register your models here.
admin.site.register(Properties)
admin.site.register(Houses)
admin.site.register(Apartaments)
admin.site.register(PropertyPhoto)
