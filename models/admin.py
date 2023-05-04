from django.contrib import admin
from .models import Categories, Manufactures, ActiveSubstances, Medicines

admin.site.register(Medicines)
admin.site.register(Categories)
admin.site.register(Manufactures)
admin.site.register(ActiveSubstances)
