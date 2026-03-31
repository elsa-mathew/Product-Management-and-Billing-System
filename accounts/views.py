from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import UserProfile

def user_management(request):

    error = ""

    # DELETE USER
    if request.GET.get('delete_user'):
        user_id = request.GET.get('delete_user')
        User.objects.filter(id=user_id).delete()
        return redirect('/users/')

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        role = request.POST.get('role')

        if not username or not password or not role:
            error = "All fields are required"
        else:
            if User.objects.filter(username=username).exists():
                error = "User already exists"
            else:
                user = User.objects.create_user(
                    username=username,
                    password=password
                )

                UserProfile.objects.create(
                    user=user,
                    role=role
                )

                return redirect('/users/')

    # 🔥 SPLIT USERS BY ROLE
    admins = UserProfile.objects.filter(role='admin')
    managers = UserProfile.objects.filter(role='manager')
    staffs = UserProfile.objects.filter(role='staff')

    return render(request, 'user_management.html', {
        'admins': admins,
        'managers': managers,
        'staffs': staffs,
        'error': error
    })