from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from ..logandreg.models import User
from .models import Plan, Travel
from datetime import datetime
# Create your views here.
def index(request):
	travel = Travel.objects.filter(user=request.session['id'])
	travel2 = Travel.objects.filter(user=request.session['id']).values_list("plan", flat=True)
	plan = Plan.planManager.exclude(id__in=travel2)
	context = {
		'plan' : plan,
		'travel' : travel
	}
	return render(request, 'travel/index.html', context)
def logout(request):
	request.session.clear()
	return redirect(reverse('main'))
def add(request):
	return render(request, 'travel/add.html')
def addtravel(request):
	if request.method == 'POST':
		cancreate = Plan.planManager.validate(request.POST['destination'], request.POST['description'], request.POST['start'], request.POST['end'])
		user_object = User.userManager.get(id= request.session['id'])
		if not cancreate[0]:
			context={'errors': cancreate[1]}
			return render(request, 'travel/add.html', context)
		elif cancreate[0]:
			Plan.planManager.create(user=user_object, destination=request.POST['destination'], description=request.POST['description'], start=request.POST['start'], end=request.POST['end'])
			plan = Plan.planManager.latest('created_at')
			Travel.objects.create(user=user_object, plan=plan)
			return redirect(reverse('travel'))
def destination(request, id):
	destination = Plan.planManager.get(id=id).destination
	plan = Plan.planManager.get(id=id)
	dest_object = Plan.planManager.filter(destination=destination)
	context = {
		'people' : Plan.planManager.filter(destination=destination),
		'destination' : destination,
		'plan' : plan,
		'travel': Travel.objects.filter(plan=dest_object)
	}
	print Travel.objects.filter(plan=dest_object)
	return render(request, 'travel/info.html', context)
def join(request, id):
	user_object = User.userManager.get(id=request.session['id'])
	dest_object = Plan.planManager.get(id=id)
	Travel.objects.create(user=user_object, plan=dest_object)
	return redirect(reverse('travel'))
