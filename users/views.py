from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import UserRegistrationForm,UserUpdateForm,ProfileUpdateForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash 


def register(request):
	if request.method=='POST':
		form=UserRegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request,"Your Account has been created")
			return redirect('home')
	else:
		form=UserRegistrationForm()
	return render(request,"users/users_form.html",{'form':form})

def profile(request):
	if request.method=="POST":
		u_form=UserUpdateForm(request.POST,instance=request.user)
		p_form=ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
		if u_form.is_valid() and p_form.is_valid():
			u_form.save()
			p_form.save()
			return redirect('profile')

	else:
		u_form=UserUpdateForm(instance=request.user)
		p_form=ProfileUpdateForm(instance=request.user.profile)

	context={
		'u_form':u_form,
		'p_form':p_form
	}
	return render(request,"users/profile.html",context)

def change_password(request):
	if request.method=="POST":
		password_change_form=PasswordChangeForm(request.user,request.POST)
		if password_change_form.is_valid():
			user=password_change_form.save()
			update_session_auth_hash(request,user) #important
			return redirect('home')
	else:
		password_change_form=PasswordChangeForm(request.user)
	return render(request,'users/change_password.html',{'password_change_form':password_change_form})

def member_details(request):
	context={
	'members':User.objects.all()
	}

	return render(request,'users/members.html',context,{'title': 'Members'})