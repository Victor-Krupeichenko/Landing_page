from django.views.generic import ListView
from .models import Landing


class LandingInfo(ListView):
    model = Landing
    template_name = 'index.html'

    def get_queryset(self):
        return Landing.objects.filter(is_published=True)
