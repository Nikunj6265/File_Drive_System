from django.contrib import admin

# Register your models here.
from .models import Folder, File


class FileInline(admin.TabularInline):
    model = File
    extra = 0
    readonly_fields = ("created_at", "updated_at")
    fields = ("file", "owner", "created_at", "updated_at")


@admin.register(Folder)
class FolderAdmin(admin.ModelAdmin):
    list_display = ("name", "owner", "created_at")
    search_fields = ("name", "owner__username")
    list_filter = ("created_at",)
    ordering = ("-created_at",)
    readonly_fields = ("created_at", "updated_at")

    inlines = [FileInline]


@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    list_display = ("file", "folder", "owner", "created_at")
    search_fields = ("file", "folder__name", "owner__username")
    list_filter = ("created_at", "folder")
    ordering = ("-created_at",)
    readonly_fields = ("created_at", "updated_at")
