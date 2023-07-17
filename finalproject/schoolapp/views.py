from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render, redirect



def home(request):
    return render(request, 'home.html')


def login_view(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('formland')
        else:
            messages.info(request,"Invalid Credentials")
            return redirect('login')
    return render(request, 'login.html')


def register(request):
    if request.method== 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['password1']
        if password==confirm_password:
           if User.objects.filter(username=username).exists():
                messages.info(request,"Username Taken")
                return redirect('register')
           user=User.objects.create_user(username=username,password=password)
           user.save();
           print('user created ')
        else:
           messages.info(request,"Password Not Match")
           return redirect('register')
        return redirect ('login')
    return render(request,'register.html')


def dashboard(request):
    return render(request, 'dashboard.html')

def formland(request):
    # Implement login view logic here
    return render(request, 'formland.html')

def forms(request):
    if request.method == 'POST':
        department = request.POST.get('department')
        course = request.POST.get('course')
        age = request.POST.get('age')
        gender = request.POST.get('gender')

        if all([department, course, age, gender]):
            # All fields are filled, display success message
            messages.success(request, 'Order Submitted')
        else:
            # Some fields are not filled, display error message
            messages.error(request, 'Order Submitted')

        return redirect('forms')

    return render(request, 'forms.html')



def logout(request):
    auth.logout(request)

    return redirect('home')


def department_wikipedia(request, dept):
    # Implement department Wikipedia logic here
    return redirect('home.html')

def get_courses(request):
    selected_department = request.GET.get('department')

    if selected_department == 'computer':
        courses = [
            {'id': 1, 'name': 'BCA'},
            {'id': 2, 'name': 'MCA'},
            # Add more computer science courses here
        ]
    elif selected_department == 'commerce':
        courses = [
            {'id': 1, 'name': 'BCom'},
            {'id': 2, 'name': 'MBA'},
            # Add more commerce courses here
        ]
    elif selected_department == 'science':
        courses = [
            {'id': 1, 'name': 'Btech'},
            {'id': 2, 'name': 'Mtech'},
            # Add more science courses here
        ]
    elif selected_department == 'physics':
        courses = [
            {'id': 1, 'name': 'Bsc Physics'},
            {'id': 2, 'name': 'Msc Physics'},
            # Add more physics courses here
        ]
    elif selected_department == 'chemistry':
        courses = [
            {'id': 1, 'name': 'Bsc Chemistry'},
            {'id': 2, 'name': 'Msc Chemistry'},
            # Add more chemistry courses here
        ]
    else:
        courses = []  # Return empty list for unknown department

    response = {'courses': courses}
    return JsonResponse(response)

