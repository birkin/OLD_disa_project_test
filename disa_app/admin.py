# -*- coding: utf-8 -*-

from django.contrib import admin
from disa_app.models import Document, DocumentColonyState
# from disa_app.models_DISA import ExtPeople, ExtReferents


class DocumentColoniesInline( admin.TabularInline ):
    """ Allows the DocumentAdmin to view/add/edit DocumentColonyState entries,
        _and_ the DocumentColonyStateAdmin to view/add/edit Document entries.
        From <https://docs.djangoproject.com/en/1.11/ref/contrib/admin/#working-with-many-to-many-models>:
        ...The through attribute is a reference to the model that manages the many-to-many relation...
        """
    model = DocumentColonyState.documents.through
    extra = 1


class DocumentAdmin( admin.ModelAdmin ):
    list_display = [ 'default_date', 'display_text' ]
    list_filter = [ 'display_text' ]
    ordering = [ 'display_text' ]
    inlines = [ DocumentColoniesInline ]
    save_on_top = True
admin.site.register( Document, DocumentAdmin )


class DocumentColonyStateAdmin( admin.ModelAdmin ):
    """ From <https://docs.djangoproject.com/en/1.11/ref/contrib/admin/#working-with-many-to-many-models>...
        The `exclude` disables the default admin-widget that would normally offer the Document view/add/edit capabilities,
        because the inline feature will be used.
        """
    list_display = [
        'name' ]
    list_filter = [
        'name', 'documents' ]
    ordering = [ 'name' ]
    inlines = [ DocumentColoniesInline ]
    exclude = [ 'documents' ]  #
    save_on_top = True
admin.site.register( DocumentColonyState, DocumentColonyStateAdmin )






# from django.contrib import admin

# class MembershipInline(admin.TabularInline):
#     model = Group.members.through

# class PersonAdmin(admin.ModelAdmin):
#     inlines = [
#         MembershipInline,
#     ]

# class GroupAdmin(admin.ModelAdmin):
#     inlines = [
#         MembershipInline,
#     ]
#     exclude = ('members',)








# # ===========================
# # external DBs
# # ===========================


# class MultiDBModelAdmin(admin.ModelAdmin):
#     # <https://docs.djangoproject.com/en/1.11/topics/db/multi-db/>

#     # A handy constant for the name of the alternate database.
#     using = 'disa_non_managed'

#     def get_queryset(self, request):
#         # Tell Django to look for objects on the 'other' database.
#         return super(MultiDBModelAdmin, self).get_queryset(request).using(self.using)


# class ExtPeopleAdmin(MultiDBModelAdmin):
#     search_fields = ['id', 'first_name', 'last_name']
#     list_display = ['id', 'first_name', 'last_name', 'comments']
# admin.site.register(ExtPeople, ExtPeopleAdmin)


# class ExtReferentsAdmin(MultiDBModelAdmin):
#     search_fields = ['id', 'age', 'sex', 'primary_name']
#     list_display = ['id', 'age', 'sex', 'primary_name']
# admin.site.register(ExtReferents, ExtReferentsAdmin)
