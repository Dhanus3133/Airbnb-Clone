from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models
from rooms import models as rooms

class RoomInline(admin.TabularInline):
    model = rooms.Room


@admin.register(models.User)
class CustomUserAdmin(UserAdmin):

    """ Custom User Admin """

    inlines = (RoomInline,)

    fieldsets = UserAdmin.fieldsets + (
        (
            "Custom Profile",
            {
                "fields": (
                    "avatar",
                    "gender",
                    "bio",
                    "birthdate",
                    "language",
                    "currency",
                    "superhost",
                )
            }
        ),
    )

    list_display = (
        "username",
        "first_name",
        "last_name",
        "email",
        "is_active",
        "language",
        "currency",
        "superhost",
        "is_staff",
        "is_superuser",
        "email_verified",
        "email_secret",
    )

    list_filter = UserAdmin.list_filter+ (
        "superhost",
    )
