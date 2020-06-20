from django.contrib import admin

# Register your models here.
from .models import signup,signin

admin.site.register(signup),
admin.site.register(signin),
# admin.site.register(Rental),

