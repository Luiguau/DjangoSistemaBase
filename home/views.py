from django.shortcuts import render, redirect
from django.contrib import messages
from login.models import User
from .models import *

# importación que sirve para ajustar la zona horaria cuando se pide la fecha y/o actuales
# y se tiene la configuración de soporte de zona horaria activado (USE_TZ=True en el archivo settings.py)
from django.utils import timezone

# importación para poder realizar operaciones con las fechas, ejemplo de sumar dias a una fecha
from datetime import timedelta

# Create your views here.
def home(request):
	#se obtiene el objeto cuyo ID es igual al del usuario que inicio sesion
	reg_user = User.objects.get(id=request.session['user_id'])

	# se obtienen todas las citas que pertenecen a ese usuario y se guardan en una lista
	appointments_list = Cita.objects.filter(usuario=reg_user)

	# se crean 2 listas que estaran vacias en las cuales se almacenaran las citas:
	# past_list -> tendra las citas que tenga una fecha anterior a la fecha de hoy
	# actual_list -> guarada todas las citas que esten vigentes
	actual_list_list=[]
	past_list = []
	
	# se obtiene la fecha actual del sistema y se le resta un dia
	# timezone.now().date() -> obtiene solo la fecha actual con zona horaria UTC
	# timedelta(days=1) -> objeto de la clase datetime que representa a un dia
	now=timezone.now().date() - timedelta(days=1)
	
	# se recorre la lista de citas obtenidas anteriormente y se consulta si la fecha es menor
	# al dia de ayer (se deja como limite el dia de ayer, ya que se comprobo que el if se comporta
	# como si fuera un menor o igual)
	for a in appointments_list:
		if a.fecha < now:
			# en el caso que se cumpla el if, la cita se almacena en la lista de citas expiradas
			past_list.append(a)
		else:
			# en el caso contrario, la cita se guarda en la lista de citas vigentes
			actual_list_list.append(a)
	
	# se prepara el context que se pasara a la pagina home.html ubicada en la app home
	context = {
		"active_user": reg_user,
		"lista_citas": actual_list_list,
		"lista_citas_pasadas": past_list,
	}
	
	return render(request, 'home/home.html', context)
