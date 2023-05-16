from django.contrib import admin
from .models import Category, Games, StarkTournirs, CyberiumTournirs, CyberArenaTournirs, TournirsCategory

# Register your models here.

admin.site.register(Category)
admin.site.register(Games)
admin.site.register(StarkTournirs)
admin.site.register(CyberiumTournirs)
admin.site.register(CyberArenaTournirs)
admin.site.register(TournirsCategory)
