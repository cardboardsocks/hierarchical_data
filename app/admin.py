from django.contrib import admin

from mptt.admin import MPTTModelAdmin , DraggableMPTTAdmin

from app.models import File

admin.site.register(File, DraggableMPTTAdmin)