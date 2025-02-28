from django.contrib import admin
# from wandercritic.models import Place, Tour
from django.contrib.auth.admin import UserAdmin
from .models import User

# from wandercritic.models import UserProfile

# admin.site.register(Place)
# admin.site.register(Tour)


# Register your models here.
admin.site.register(User, UserAdmin)