from django.contrib import admin
from .models import *

admin.site.register(Doctor)

admin.site.register(Comment)

admin.site.register(Specialize)

admin.site.register(AvailableTime)

admin.site.register(VisitCost)