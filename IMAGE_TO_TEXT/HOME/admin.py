from django.contrib import admin
from HOME.models import Uploads

# Register your models here.
@admin.register(Uploads)
class UploadAdmin(admin.ModelAdmin):
    list_display = ['id','Images','Texts']
