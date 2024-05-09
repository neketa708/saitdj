from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
import logging
from .forms import UserForm
logger = logging.getLogger(__name__)


def index(request):
    return HttpResponse("Hello, world!")
def about(request):
    return HttpResponse("About us")

def my_view(request):
    context = {"name": "John"}
    return render(request, "myapp/my.html", context)

class TemplIf(TemplateView):
    template_name = "myapp/if.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = "Привет, мир!"
        context['number'] = 5
        return context


def user_form(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            age = form.cleaned_data['age']
        # Делаем что-то с данными
            logger.info(f'Получили {name=}, {email=}, {age=}.')
    else:
        form = UserForm()
    return render(request, 'myapp/form.html', {'form': form})