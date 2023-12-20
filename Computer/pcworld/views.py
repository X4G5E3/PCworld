from django.shortcuts import render, get_object_or_404, redirect
from pcworld.models import *
from .forms import UserRegistrationForm, ContactForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout, login
from django.core.mail import send_mail
from django.conf import settings
from django.views.decorators.csrf import csrf_protect

@csrf_protect
def index(request):
    if request.method == "POST":
       form = ContactForm(data=request.POST)
       if form.is_valid():
            name = request.POST['first_name']
            subject = request.POST['subject']
            email = request.POST['email']
            message = request.POST['message']
            Message = f'User: {name}\nEmail: {email}\nMessage: {message}'
            send_mail(subject, Message, settings.EMAIL_HOST_USER, ['pcworld.1224@mail.ru'], fail_silently=False)
    else:
        form = ContactForm()
    return render(request, 'common/index.html', {'form': form})

def about(request):
    return render(request, 'common/about.html')

class UserAuthForm(LoginView):
    form_class = AuthenticationForm
    template_name = 'common/login.html'

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password'])
            user.save()
            login(request, user)
            return render(request, 'common/index.html')
    else:
        user_form = UserRegistrationForm()
    
    return render(request, 'common/register.html', {'reg_form': user_form})

def service(request):
    return render(request, 'common/service.html')

def works(request):
    return render(request, 'common/works.html')

def upgrade(request):
    return render(request, 'common/upgrade.html')

def repair(request):
    return render(request, 'common/repair.html')

def modding(request):
    return render(request, 'common/modding.html')

def trade(request):
    return render(request, 'common/trade.html')
    
def products(request):
    context = {
        'products': Product.objects.all()
    }
    return render(request, 'common/products.html', context=context)

def product(request, product_slug):
    product = get_object_or_404(Product, slug=product_slug)
    
    data = {
        'product': product
    }
    
    return render(request, 'common/product.html', context=data)

def components(request):
    context = {
        'components': Component.objects.all()
    }
    
    return render(request, 'common/components.html', context=context)

def component(request, component_slug):
    component = get_object_or_404(Component, slug=component_slug)
    
    data = {
        'component': component
    }
    
    return render(request, 'common/component.html', context=data)

def logout_user(request):
    logout(request)
    return redirect('index')