from django.contrib import admin

# Register your models here.
# mmup / 1234
from .models import contents, survey

admin.site.register(contents)
admin.site.register(survey)