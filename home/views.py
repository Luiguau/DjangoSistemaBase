from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils import timezone
from login.models import User
from .models import *
from datetime import timedelta

# Create your views here.
def home(request):
	reg_user = User.objects.get(id=request.session['user_id'])
	appointments_list = Cita.objects.filter(usuario=reg_user)
	appointment_list=[]
	past_list = []
	now=timezone.now().date()- timedelta(days=1)
	for a in appointments_list:
		if a.fecha < now:
			past_list.append(a)
		else:
			appointment_list.append(a)
	context = {
		"active_user": reg_user,
		"lista_citas": appointment_list,
		"lista_citas_pasadas": past_list,
	}

	return render(request, 'home/home.html', context)
