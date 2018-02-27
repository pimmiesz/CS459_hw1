from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from .forms import PersonForm , RentForm
from .models import Person , User , Rent , Car
from django.shortcuts import render
from django.contrib.auth.models import User

from django.shortcuts import render
# Create your views here.
# def Car_list(request):
# 	car = Car.objects.filter()
#     return render(request, 'myproject/templates/rent.html', {})

# class CreateProfileView(CreateView):
# 	queryset = User()
# 	template_name='user.html'
# 	form_class = UserForm
# 	success_url = '/admin'

class CreatePersonView(CreateView):
	queryset = Person()
	template_name='create.html'
	form_class = PersonForm
	success_url = '/admin'

class CreateRentView(CreateView):
	queryset = Rent()
	template_name='rent.html'
	form_class = RentForm
	success_url = '/rent'
	def form_valid(self,form):
  		form.instance.user = self.request.user
  		return super(CreateRentView, self).form_valid(form)

class ListPersonView(ListView):
    model = Person
    template_name='list.html'

def	getAllCar(request):
	cars = Car.objects.all()
	return render(request, 'car.html', {'object_list':cars})

# def addRent(request):
# 	print("+++++++++++++++++++++++")
# 	model = Rent()
# 	car = Car()
# 	car.name = "toyata"
# 	car.price = 1222
# 	car.detail ="eweweqw"
# 	car.save()
#
# 	model.user= request.user
# 	model.car = car
# 	model.start_datetime = '2018-02-21'
# 	model.stop_datetime ='2018-02-24'
# 	model.fee='200'
# 	model.save()
# 	return render(request, 'rent.html')

# class RentView(ListView):
# 	model = Car
# 	template_name='rent.html'
