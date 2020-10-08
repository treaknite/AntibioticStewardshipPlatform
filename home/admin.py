from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Record,approvals
# Register your models here.
@admin.register(Record)
@admin.register(approvals)
class viewAdmin(ImportExportModelAdmin):
      pass