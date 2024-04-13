from django.views.generic import TemplateView, FormView, ListView

from apps.forms import UserForm
from apps.models import Video, Photo


class UserTemplateView(TemplateView):
    template_name = 'main.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['videos'] = Video.objects.all()
        return context
