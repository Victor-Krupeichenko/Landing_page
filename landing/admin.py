from django.contrib import admin
from .models import Landing
from django.forms import TextInput, Textarea
from django.db import models


class LandingAdmin(admin.ModelAdmin):
    list_display = ['header_title_1', 'is_published']
    list_editable = ['is_published']
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '50'})},
        models.TextField: {'widget': Textarea(attrs={'rows': 5, 'cols': 80})},
    }
    fieldsets = (
        ('Настройки Header(первый экран) - заголовки', {
            'fields': ('header_title_1', 'header_title_2', 'header_content')
        }),
        ('Настройки Inspire (второй экран) - заголовки', {
            'fields': ('inspire_title_1', 'inspire_title_2')
        }),
        ('Настройки Inspire (второй экран) - заполнение контента для секции Django', {
            'fields': ('django_content', 'django_img')
        }),
        ('Настройки Inspire (второй экран) - заполнение контента для секции Bootstrap', {
            'fields': ('bootstrap_content', 'bootstrap_img')
        }),
        ('Настройки Inspire (второй экран) - заполнение контента для секции CSS', {
            'fields': ('css_content', 'css_img')
        }),
        ('Настройки attainment (низ второго экрана) - заполнение контента для Django(левый блок)', {
            'fields': ('attainment_django_num', 'attainment_django_title', 'attainment_django_content')
        }),
        ('Настройки attainment (низ второго экрана) - заполнение контента для Bootstrap (центральный блок)', {
            'fields': ('attainment_bootstrap_num', 'attainment_bootstrap_title', 'attainment_bootstrap_content')
        }),
        ('Настройки attainment (низ второго экрана) - заполнение контента для CSS (правый блок)', {
            'fields': ('attainment_css_num', 'attainment_css_title', 'attainment_css_content')
        }),
        ('Настройки lets(третий экран)', {
            'fields': ('lets_title_1', 'lets_title_2', 'lets_content')
        }),
        ('Настройка секкции CRM (вторая половина третьего экрана)',{
            'fields': ('crm_title_1', 'crm_title_2', 'crm_content')
        }),
        ('Настройка секции CRM (колонки) - первая полонка', {
            'fields': ('crm_section_1', 'crm_section_content')
        }),
        ('Настройка секции CRM (колонки) - вторя полонка', {
            'fields': ('crm_section_2', 'crm_section_2_content')
        }),
        ('Настройка секции CRM (блок видео)',{
            'fields': ('crm_video_1', 'crm_video_2'),
            'description': 'Сюда вставляются ссылки на видео с видио-хостинга YouTube'
        }),
        ('Опубликовать', {
            'fields': ('is_published', ),
            'description': 'Чтобы опубликовать второй вариант заполнения - НЕОБХОДИМО СНЯТЬ ОПУБЛИКОВАНО С '
                           'ПРЕДЫДУЩЕГО ВАРИАНТА',
            'classes': ['collapse']
        }),

    )

admin.site.register(Landing, LandingAdmin)
