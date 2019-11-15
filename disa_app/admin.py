# -*- coding: utf-8 -*-

from django.contrib import admin
from disa_app.models_DISA import ExtPeople, ExtReferents


# ===========================
# external DBs
# ===========================


class MultiDBModelAdmin(admin.ModelAdmin):
    # <https://docs.djangoproject.com/en/1.11/topics/db/multi-db/>

    # A handy constant for the name of the alternate database.
    using = 'disa_non_managed'

    def get_queryset(self, request):
        # Tell Django to look for objects on the 'other' database.
        return super(MultiDBModelAdmin, self).get_queryset(request).using(self.using)


class ExtPeopleAdmin(MultiDBModelAdmin):
    search_fields = ['id', 'first_name', 'last_name']
    list_display = ['id', 'first_name', 'last_name', 'comments']
admin.site.register(ExtPeople, ExtPeopleAdmin)


class ExtReferentsAdmin(MultiDBModelAdmin):
    search_fields = ['id', 'age', 'sex', 'primary_name']
    list_display = ['id', 'age', 'sex', 'primary_name']
admin.site.register(ExtReferents, ExtReferentsAdmin)
