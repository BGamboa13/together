from autoslug import AutoSlugField
from django.db import models
from django.utils.translation import gettext as _
from django_ckeditor_5.fields import CKEditor5Field


# Create your models here.


class ContactMessage(models.Model):
    name = models.CharField(_('name'), max_length=100)
    email = models.EmailField(_('email'))
    message = models.TextField(_('message'))
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Blog(models.Model):
    title = models.CharField(max_length=200, verbose_name=_('Title'))
    content = CKEditor5Field(_('Content'), config_name='extends', blank=True)
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name=_('Publication Date'))
    category = models.CharField(max_length=100, verbose_name=_('Category'))
    author = models.CharField(max_length=100, verbose_name=_('Author'))
    main_image = models.ImageField(upload_to='img/gallery/', blank=True, null=True,
                                   verbose_name=_('Main Image'))
    enabled = models.BooleanField(default=True, verbose_name=_('Enabled'))
    slug = AutoSlugField(unique=True, populate_from='title', verbose_name=_('Slug'))

    def __str__(self):
        return self.title

    def get_main_image_url(self):
        return self.main_image.url.split('/static/', 1)[-1] if self.main_image else ''


class DonationCampaign(models.Model):
    title = models.CharField(max_length=200, verbose_name=_('Title of the Campaign'))
    content = CKEditor5Field(_('Content'), config_name='extends', blank=True)
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name=_('Publication Date'))
    author = models.CharField(max_length=100, verbose_name=_('Author'))
    target_amount = models.DecimalField(max_digits=10, decimal_places=2)
    current_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    main_image = models.ImageField(upload_to='img/gallery/', blank=True, null=True,
                                   verbose_name=_('Main Image'))
    enabled = models.BooleanField(default=True, verbose_name=_('Enabled'))
    slug = AutoSlugField(unique=True, populate_from='title', verbose_name=_('Slug'))

    def __str__(self):
        return self.title

    def get_main_image_url(self):
        return self.main_image.url.split('/static/', 1)[-1] if self.main_image else ''


class Donations(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=30)
    transaction_number = models.CharField(max_length=100, blank=True, null=True)


class GalleryImage(models.Model):
    image = models.ImageField(upload_to='img/gallery/', verbose_name=_('Gallery Image'))
    description = models.CharField(max_length=255, verbose_name=_('Description'))
    galleries = models.ManyToManyField('Gallery', related_name='images')

    def __str__(self):
        return self.description

    def get_image_url(self):
        return self.image.url.split('/static/', 1)[-1] if self.image else ''


class Gallery(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
