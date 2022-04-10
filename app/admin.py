from django.contrib import admin
from django.utils.safestring import mark_safe
from django import forms
from .models import *

from ckeditor_uploader.widgets import CKEditorUploadingWidget


# Register your models here.


class NumbersAdminForm(forms.ModelForm):
    subscrible = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Numbers
        fields = '__all__'


class ExcursionAdminForm(forms.ModelForm):
    subscrible = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Excursion
        fields = '__all__'


class MenuAdminForm(forms.ModelForm):
    subscrible = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Menu
        fields = '__all__'


@admin.register(Numbers)
class NumbersAdmin(admin.ModelAdmin):
    form = NumbersAdminForm
    list_display = ('id', 'title', 'del_html_tag_in_subscrible',
                    'enum', 'price', 'get_photo')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'del_html_tag_in_subscrible')
    save_on_top = True

    def get_photo(self, obj):
        if obj.img:
            return mark_safe(f'<img src="{obj.img.url}" width="75">')
        else:
            return '-'

    get_photo.short_description = 'Миниатюра'


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price')
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    save_on_top = True


@admin.register(Excursion)
class ExcursionAdmin(admin.ModelAdmin):
    form = ExcursionAdminForm
    list_display = ('id', 'title', 'del_html_tag_in_subscrible',
                    'program', 'price', 'get_photo')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'del_html_tag_in_subscrible', 'program')
    save_on_top = True

    def get_photo(self, obj):
        if obj.img:
            return mark_safe(f'<img src="{obj.img.url}" width="75">')
        else:
            return '-'

    get_photo.short_description = 'Миниатюра'


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    form = MenuAdminForm
    list_display = ('id', 'title', 'del_html_tag_in_subscrible', 'get_photo')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'del_html_tag_in_subscrible')
    save_on_top = True

    def get_photo(self, obj):
        if obj.img:
            return mark_safe(f'<img src="{obj.img.url}" width="75">')
        else:
            return '-'

    get_photo.short_description = 'Миниатюра'
