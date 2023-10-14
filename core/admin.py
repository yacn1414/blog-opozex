from django.contrib import admin
from core.models import (
    cat,
    Site,
    posts,
    Socials
    )
# Register your models here.
admin.site.register(cat)
admin.site.register(Site)
admin.site.register(posts)
admin.site.register(Socials)