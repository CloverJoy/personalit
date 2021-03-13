from django.contrib import admin
from .models import Classification, Personality


class ClassificationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class PersonalityAdmin(admin.ModelAdmin):
    exclude = ('date_created',)
    list_display = ('mbtitype', 'name')


admin.site.register(Classification, ClassificationAdmin)
admin.site.register(Personality, PersonalityAdmin)
