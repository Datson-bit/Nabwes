from django.contrib import admin
from .models import Event,Blog, Gallery, Sponsor,Comment, GalleryImage, Executives, Parliamentary, Registration, EventPass


admin.site.register(Blog)
admin.site.register(Comment)

@admin.register(Executives)
class ExecutivesAdmin(admin.ModelAdmin):
    model = Executives
    list_display= ('name', 'position')
    
@admin.register(Parliamentary)
class ExecutivesAdmin(admin.ModelAdmin):
    model = Parliamentary
    list_display= ('name', 'position')

class GalleryImageInline(admin.TabularInline):  # Use StackedInline for vertical forms
    model = GalleryImage
    extra = 3  # Number of empty forms to display for new images
    fields = ('image', 'caption')

@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    inlines = [GalleryImageInline]

@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ('gallery', 'caption')

class SponsorInine(admin.TabularInline):
    model = Sponsor
    extra = 1

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    inlines = [SponsorInine]
    list_display = ['title', 'date', 'venue', ]

admin.register(Sponsor)
class SponsorAdmin(admin.ModelAdmin):
    list_display = ('name', 'event')

@admin.register(Registration)
class RegistrationAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'email', 'event', 'registered_at']

@admin.register(EventPass)
class EventPassAdmin(admin.ModelAdmin):
    list_display = ['registration', 'pass_code']