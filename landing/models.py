from django.db import models


class Landing(models.Model):
    header_title_1 = models.CharField(max_length=31)
    header_title_2 = models.CharField(max_length=42)
    header_content = models.TextField(max_length=110)
    inspire_title_1 = models.CharField(max_length=27)
    inspire_title_2 = models.CharField(max_length=42)
    django_content = models.TextField(max_length=281)
    bootstrap_content = models.TextField(max_length=281)
    css_content = models.TextField(max_length=281)
    django_img = models.ImageField(upload_to='images/django/%Y/%m/%d/', blank=True)
    bootstrap_img = models.ImageField(upload_to='images/bootstrap/%Y/%m/%d/', blank=True)
    css_img = models.ImageField(upload_to='images/css/%Y/%m/%d/', blank=True)
    attainment_django_num = models.CharField(max_length=7)
    attainment_django_title = models.CharField(max_length=31)
    attainment_django_content = models.TextField(max_length=111)
    attainment_bootstrap_num = models.CharField(max_length=7)
    attainment_bootstrap_title = models.CharField(max_length=31)
    attainment_bootstrap_content = models.TextField(max_length=111)
    attainment_css_num = models.CharField(max_length=7)
    attainment_css_title = models.CharField(max_length=31)
    attainment_css_content = models.TextField(max_length=111)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self
