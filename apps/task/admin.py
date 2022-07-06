from django.contrib import admin

from apps.task.models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'completed', 'user')
    list_filter = ('completed',)
    search_fields = ('title', 'description')
    ordering = ('-created_at',)
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('Task', {
            'fields': ('title', 'description', 'completed', 'user')
        }),
        ('Meta', {
            'fields': ('created_at', 'updated_at')
        })
    )
    list_per_page = 10
    list_max_show_all = 100
    list_editable = ('completed',)
    list_select_related = ('user',)
    list_display_links = ('title',)
    list_display_links_details = False
    list_display_details = False
    list_filter_details = False
