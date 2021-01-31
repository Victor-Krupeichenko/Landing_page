from django.db import models


class Landing(models.Model):
    header_title_1 = models.CharField(max_length=31, verbose_name='Первый заголовок')
    header_title_2 = models.CharField(max_length=42, verbose_name='Второй заголовок', blank=True,
                                      help_text='Это поле необязательно к заполнению')
    header_content = models.TextField(max_length=110, verbose_name='Содержание')
    inspire_title_1 = models.CharField(max_length=27, verbose_name='Первый заголовок')
    inspire_title_2 = models.CharField(max_length=42, verbose_name='Второй заголовок', blank=True,
                                       help_text='Это поле необязательно к заполнению')
    django_content = models.TextField(max_length=281, verbose_name='Контент')
    bootstrap_content = models.TextField(max_length=281, verbose_name='Контент')
    css_content = models.TextField(max_length=281, verbose_name='Контент')
    django_img = models.ImageField(upload_to='images/django/%Y/%m/%d/', blank=True, verbose_name='Изображение',
                                   help_text='Это поле необязательно к заполнению')
    bootstrap_img = models.ImageField(upload_to='images/bootstrap/%Y/%m/%d/', blank=True, verbose_name='Изображение',
                                      help_text='Это поле необязательно к заполнению')
    css_img = models.ImageField(upload_to='images/css/%Y/%m/%d/', blank=True, verbose_name='Изображение',
                                help_text='Это поле необязательно к заполнению')
    attainment_django_num = models.CharField(max_length=7, verbose_name='Достижение в цифрах')
    attainment_django_title = models.CharField(max_length=31, verbose_name='Заголовок')
    attainment_django_content = models.TextField(max_length=111, verbose_name='Контент')
    attainment_bootstrap_num = models.CharField(max_length=7, verbose_name='Достижение в цифрах')
    attainment_bootstrap_title = models.CharField(max_length=31, verbose_name='Заголовок')
    attainment_bootstrap_content = models.TextField(max_length=111, verbose_name='Контент')
    attainment_css_num = models.CharField(max_length=7, verbose_name='Достижение в цифрах')
    attainment_css_title = models.CharField(max_length=31, verbose_name='Заголовок')
    attainment_css_content = models.TextField(max_length=111, verbose_name='Контент')
    is_published = models.BooleanField(default=False, verbose_name='Опубликовано')
    lets_title_1 = models.CharField(max_length=18, verbose_name='Певый заголовок')
    lets_title_2 = models.CharField(max_length=42, verbose_name='Второй заголовок', blank=True,
                                    help_text='Это поле необязательно к заполнению')
    lets_content = models.TextField(max_length=171, verbose_name='Контент')
    crm_title_1 = models.CharField(max_length=32, verbose_name='Первый заголовок')
    crm_title_2 = models.CharField(max_length=43, verbose_name='Второй заголовок', blank=True,
                                   help_text='Это поле необязательно к заполнению')
    crm_content = models.TextField(max_length=221, verbose_name='Контент')
    crm_section_1 = models.CharField(max_length=14, verbose_name='Заголовок')
    crm_section_content = models.TextField(max_length=110, verbose_name='Контент')
    crm_section_2 = models.CharField(max_length=14, verbose_name='Заголовок')
    crm_section_2_content = models.TextField(max_length=110, verbose_name='Контент')
    crm_video_1 = models.TextField(verbose_name='Видео', blank=True,
                                   help_text='Это поле необязательно к заполнению')
    crm_video_2 = models.TextField(verbose_name='Видео', blank=True,
                                   help_text='Это поле необязательно к заполнению')

    # def __str__(self):
    #     return self.header_title_1
