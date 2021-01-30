from django.contrib import admin
from .models import Landing


class LandingAdmin(admin.ModelAdmin):
    list_display = ['header_title_1', 'is_published']
    list_editable = ['is_published']
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
        ('Опубликовать', {
            'fields': ('is_published',),
            'description': 'Чтобы опубликовать второй вариант заполнения - НЕОБХОДИМО СНЯТЬ ОПУБЛИКОВАНО С '
                           'ПРЕДЫДУЩЕГО ВАРИАНТА',
            'classes': ['collapse']
        }),

    )


admin.site.register(Landing, LandingAdmin)
