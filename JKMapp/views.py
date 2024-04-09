from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
# Create your views here.
from JKMapp.form import StuForm, UserRegistrationForm,  PersonalDetailsForm, LoginForm
from .models import Student, PersonalDetails
from django.contrib.auth.decorators import login_required
from django.contrib import messages
 # Create your views here.
def Home(request):
    return render(
        request,
        "home.html"
    )



def index(request):

    return render(
        request,
        "index.html", 
    )



def student_list(request):
    students = Student.objects.all()
    return render(request, 'student.html', {'students': students})



def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  # Redirect to login page after successful registration
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})

@login_required
def update_personal_details(request):
    personal_details, created = PersonalDetails.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = PersonalDetailsForm(request.POST, instance=personal_details)
        if form.is_valid():
            form.save()
            return redirect('personal_details')  # Redirect to a profile or another relevant page
    else:
        form = PersonalDetailsForm(instance=personal_details)
    return render(request, 'update_personal_details.html', {'form': form})


@login_required
def personal_details(request):
    personal_details_instance, created = PersonalDetails.objects.get_or_create(user=request.user)
    return render(request, 'personal_details.html', {"personal_details": personal_details_instance, "user": request.user})

def custom_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('personal_details')
            else:
                messages.error(request, 'Invalid username or password')

    else:
        form = LoginForm()
    return render(request, 'login.html', {"form": form})