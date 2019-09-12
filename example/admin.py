from django.contrib import admin

from example.models import FileSystemElement
from example.query import FileSystemQuerySet
from sneak.admin import SneakAdmin


class FileSystemAdmin(SneakAdmin):
    QuerySet = FileSystemQuerySet

    list_display = ('path',)


admin.site.register([FileSystemElement], FileSystemAdmin)
