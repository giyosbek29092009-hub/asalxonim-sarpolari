from django.urls import reverse_lazy
from django.views.generic import CreateView
from accounts.forms import CustomUserCreationForm
from django.shortcuts import render


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

def about_view(request):
    return render(request, 'about.html')

def about_view(request):
    return render(request, 'html.html')