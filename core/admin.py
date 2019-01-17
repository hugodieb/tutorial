from django.contrib import admin

from core.models import ActivityLog, Todo, City, Person, Book, Video, Tutorial


class ActivityLogAdmin(admin.ModelAdmin):
    list_display = ('type', 'logged_user', 'created_at')

class TodoAdmin(admin.ModelAdmin):
    list_display = ('description',)


class CityAdmin(admin.ModelAdmin):
    list_display = ('name',)

class PersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'hometown')


class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'author',)

class VideoAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ['title']

class TutorialAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ['title']
    filter_horizontal = ('similar', 'videos')


admin.site.register(ActivityLog, ActivityLogAdmin)
admin.site.register(Todo, TodoAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(Person, PersonAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Video, VideoAdmin)
admin.site.register(Tutorial, TodoAdmin)