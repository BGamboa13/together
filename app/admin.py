from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from .models import Blog, Gallery, GalleryImage, DonationCampaign

# Register your models here.
admin.site.register(Gallery)
admin.site.register(GalleryImage)


@admin.register(Blog)
class BlogAdmin(TranslationAdmin):
    list_display = ('title',)

    class Media:
        js = (
            'https://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'https://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


@admin.register(DonationCampaign)
class DonationCampaignAdmin(TranslationAdmin):
    list_display = ('title',)

    class Media:
        js = (
            'https://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'https://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }
