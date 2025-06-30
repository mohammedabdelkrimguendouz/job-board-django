from django.shortcuts import redirect, render
from django.contrib.auth import logout
from django.urls import reverse
from .form import SignupForm
from django.contrib.auth import authenticate , login
from .models import Profile
from .form import ProfileForm,UserForm


def signup(request):
    if(request.method == 'POST'):
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user= authenticate(username=username,password=password)
            login(request,user)
            return redirect('/accounts/profile')



    else:
        form = SignupForm()
    return render(request, 'registration/signup.html',{'form':form})


def profile(request):
    profile = Profile.objects.get(user=request.user)
    return render(request,'accounts/profile.html',{'profile':profile})


def profile_edit(request):
    profile = Profile.objects.get(user=request.user)
    if(request.method == 'POST'):
        userForm = UserForm(request.POST , instance=request.user)
        profileForm = ProfileForm(request.POST,request.FILES,instance=profile)
        if userForm.is_valid() and profileForm.is_valid():
            userForm.save()
            myprofile = profileForm.save(commit=False)
            myprofile.user = request.user
            myprofile.save()
            return redirect(reverse('accounts:profile'))


    else:
        userForm = UserForm(instance=request.user)
        profileForm = ProfileForm(instance=profile)

    context = {'userForm':userForm,'profileForm':profileForm}

    return render(request,'accounts/profile_edit.html',context)


def logout_view(request):
    logout(request)
    return redirect(reverse('jobs:job_list'))
