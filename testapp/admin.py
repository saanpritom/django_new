from django.contrib import admin
from testapp.models import AccessRecords, Topic, Webpage

# Register your models here.
admin.site.register(AccessRecords)
admin.site.register(Webpage)
admin.site.register(Topic)
