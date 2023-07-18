from django.contrib import admin
from .models import *
from .form import formacc
# Register your models here.

admin.site.register(sections)
admin.site.register(initiatives)
admin.site.register(login_user)
admin.site.register(login_admin)
admin.site.register(post)
admin.site.register(department)
admin.site.register(accountForm)
admin.site.register(services)
