from django.shortcuts import render,redirect
from django.contrib.auth.models import auth
from django.contrib import messages
from .forms import UserForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from .forms import PersonalInfoForm
from .models import PersonalInfo
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template.loader import get_template
from django.views import View
from xhtml2pdf import pisa
import io

# Create your views here.

def home(request):
    context = {}
    return render(request, 'home.html', context)


def register(request):
    form_name = UserForm()
    if request.method =="POST":
        form_name = UserForm(request.POST)
        if form_name.is_valid():
            form_name.save()
            messages.success(request, "You have registered successfully")
            return redirect('signin')
        else:
            messages.error(request, 'Password not secure') 
            return redirect('register')
    else:
        context = {'form_name':form_name}
        
    return render(request, 'register.html', context )

def signin(request):
    if request.method == 'POST':
            form = AuthenticationForm(request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('createresume')
            else:
                messages.info(request, 'Invalid username or password.. Please try again.')
                return redirect('signin')
    form = AuthenticationForm()
    context = {'form':form}
        
    return render(request, 'login.html', context)


@login_required(login_url='signin')
def createresume(request):
    try:
        personal_info = PersonalInfo.objects.get(username=request.user)
        
    except PersonalInfo.DoesNotExist:
        personal_info = PersonalInfo(username=request.user)

    if request.method == 'POST':
        form = PersonalInfoForm(request.POST, instance=personal_info)
        if form.is_valid():
            form.save()
            return redirect('cvtemplate')
    else:
        form = PersonalInfoForm()

    return render(request, 'createresume.html', {'form': form})


@login_required(login_url='signin')
def cvtemplate(request):
    log_user = request.user
    template = PersonalInfo.objects.filter(username=log_user)
    template_data = {'template': template}

    template_path = 'cvtemplate.html'
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="cvtemplate.pdf"'

    template = get_template(template_path)
    html = template.render(template_data)
    pdf = pisa.CreatePDF(io.StringIO(html), response)

    if pdf.err:
        return HttpResponse('Error generating PDF')
    else:
        return response

def logout(request):
    auth.logout(request)
    return redirect('signin')



