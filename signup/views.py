from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import UserForm, UserProfileForm
from .models import UserProfile
def index(request):
	registered = False
	if request.method == 'POST':
		user_form = UserForm(data = request.POST)
		profile_form = UserProfileForm(data = request.POST)
		if user_form.is_valid() and profile_form.is_valid():
			print user_form
			print profile_form
			user = user_form.save()
			user.set_password(user.password)
			user.save()
			user_profile = profile_form.save(commit = False)

			user_profile.user = user
			user_profile.save()
			registered=True
		else:
			print user_form.errors, profile_form.errors

	else:
		user_form = UserForm()
		profile_form = UserProfileForm()
	return render(request,'launchapp/index.html',{'user_form':user_form,'profile_form':profile_form, 'registered':registered})

def about(request):
	return render(request,'launchapp/aboutus.html',{})

def privacy(request):
	return render(request,'launchapp/privacy-policy.html',{})

def terms(request):
	return render(request,'launchapp/terms.html',{})


