from django.contrib import admin
from .models import customers, users
# Register your models here.
admin.site.register(customers)
admin.site.register(users)