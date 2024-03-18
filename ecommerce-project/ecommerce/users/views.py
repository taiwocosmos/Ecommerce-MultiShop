from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegistrationForm, UserUpdateForm, ProfileUpdateForm
from django.contrib import messages # so as to show messages letting the user know his/her has successfully created an account or entered the wrong password
from django.contrib.auth.decorators import login_required #so as to restrict the user from viewin his/her profile without logging in
# Create your views here.
def Signup(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            ## we need to display a message if the inmformation is correct
            # to use this message, we need to import it.
            messages.success(request, f'Registration Successful for {username}')
            return redirect('login') #this will return user to homepage
    else:
        form = UserRegistrationForm()

    form_dict = {'form': form}
    return render(request, 'users/register.html', context= form_dict)

@login_required(login_url="login")
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
        request.FILES,
        instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Profile updated Successfully')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    update_dict = {'u_form': u_form, 'p_form': p_form}
    return render(request, 'users/profile.html', context= update_dict)