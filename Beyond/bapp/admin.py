from django.contrib import admin

# Register your models here.
from . import models
admin.site.site_header="Automation tool for Digital Marketing"
admin.site.site_title="Digital Marketing"
admin.site.index_title="Manage Online Marketing"
admin.site.register(models.Contact)
