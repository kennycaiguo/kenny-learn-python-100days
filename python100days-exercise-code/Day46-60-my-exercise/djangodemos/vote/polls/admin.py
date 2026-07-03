from django.contrib import admin
from .models import Subject, Teacher


class SubjectModelAdmin(admin.ModelAdmin):
    list_display = ('no', 'name', 'intro', 'is_hot')
    search_fields = ('name',)
    ordering = ('no',)


class TeacherModelAdmin(admin.ModelAdmin):
    list_display = ('no', 'name', 'sex', 'birth', 'gcount', 'bcount', 'subject')
    search_fields = ('name',)
    ordering = ('no',)


# Register your models here.
admin.site.register(Subject, SubjectModelAdmin)
admin.site.register(Teacher, TeacherModelAdmin)
