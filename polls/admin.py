from django.contrib import admin

# Register your models here.
from .models import	Output
from import_export.admin import ImportExportModelAdmin

@admin.register(Output)
class ViewAdmin(ImportExportModelAdmin):
	pass