from django.contrib import admin

# Register your models here.
from recommendations.models import Games, Attributes, Profile

admin.site.register(Games)
admin.site.register(Attributes)
admin.site.register(Profile)
