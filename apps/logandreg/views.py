from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from .models import User
# Create your views here.
def index(request):
	return render(request, 'logandreg/index.html')
def register(request):
	if request.method == "POST":
		user = User.userManager.register(request.POST['name'], request.POST['username'], request.POST['password'], request.POST['confirm_password'])
		context = {'errors' : user[1]}
		if user[0]:
			request.session['id'] = user[1].id
			request.session['name'] = user[1].name
	return render(request, 'logandreg/index.html', context)
def login(request):
	if request.method == "POST":
		user = User.userManager.login(request.POST['username'], request.POST['password'])
		context = {'login' : user[1]}
		if user[0]:
			request.session['id'] = user[1].id
			request.session['name'] = user[1].name
			return redirect(reverse('travel'))
		else:
			print "does not work"
			return render(request, 'logandreg/index.html', context)
