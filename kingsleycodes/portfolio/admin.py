from django.contrib import admin
from .models import Project, Blog, Service, ContactMessage
from django.utils.html import format_html


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'is_published', 'created_at')
    list_filter = ('is_published',)
    search_fields = ('title', 'author')
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'icon', 'created_at')
    prepopulated_fields = {'slug': ('title',)}


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('status_badge', 'name_display', 'email', 'created_at')
    list_filter = ('is_read', 'created_at')
    search_fields = ('name', 'email', 'message')
    actions = ['mark_as_read']

    @admin.action(description="Mark selected messages as read ✅")
    def mark_as_read(self, request, queryset):
        updated = queryset.update(is_read=True)
        self.message_user(request, f"{updated} message(s) marked as read")

    # 💬 Status Badge
    def status_badge(self, obj):
        if not obj.is_read:
            return format_html(
                '<span style="color:#3B82F6; font-size:22px;">●</span>'
            )  # Blue dot for unread
        return format_html(
            '<span style="color:#22C55E; font-size:18px;">✓</span>'
        )  # Green check for read
    status_badge.short_description = "Status"

    # 🧍 Name display (bold if unread)
    def name_display(self, obj):
        if not obj.is_read:
            return format_html('<strong>{}</strong>', obj.name)
        return obj.name
    name_display.short_description = "Name"

    # 📅 Order messages by latest first
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.order_by('-created_at')
