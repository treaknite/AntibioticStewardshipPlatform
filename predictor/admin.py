from django.contrib import admin
from predictor.models import predictor
#from predictor.models import antibiotics_details
#from django.contrib.admin.options import ModelAdmin

#class showantib(ModelAdmin):
 #   list_display = ["antibiotic1", "antibiotic2", "antibiotic3"]
 #   search_fields = ["antibiotic1", "antibiotic2", "antibiotic3"]
    ##list_filter = 

#admin.site.register(antibiotics_details, showantib)
admin.site.register(predictor)

# Register your models here.
