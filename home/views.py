from django.shortcuts import render, HttpResponse
from django.views.decorators.cache import never_cache
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='login')
def dashboard(request):
    return render(request, 'home.html')
@login_required(login_url='login')
def read(request):
    return render(request, 'about.html')
@login_required(login_url='login')
def contact(request):
    return render(request, 'contact.html')
@login_required(login_url='login')
def project(request):
    return render(request, 'project.html')
@login_required(login_url='login')
def index(request):
    return render(request, 'index.html')
@login_required(login_url='login')
def dm(request):
    return render(request, 'dm.html')
@login_required(login_url='login')
def clfn(request):
    return render(request, 'clfn.html')
@login_required(login_url='login')
def clfn_easy(request):
    return render(request, 'clfn_easy.html')




from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log in the user after signup
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('login')  