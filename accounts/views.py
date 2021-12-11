
from django.views.generic import TemplateView
from .forms import CustomUserCreationForm
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView



class HomePageView(TemplateView):
    template_name = 'index.html'

class SignUpView(CreateView):
    template_name = 'registration/signup.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    
    