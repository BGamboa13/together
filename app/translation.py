from modeltranslation.translator import register, TranslationOptions
from .models import Blog, DonationCampaign


@register(Blog)
class BlogTranslationOptions(TranslationOptions):
    fields = ('title', 'content', 'category')


@register(DonationCampaign)
class DonationCampaignTranslationOptions(TranslationOptions):
    fields = ('title', 'content')
