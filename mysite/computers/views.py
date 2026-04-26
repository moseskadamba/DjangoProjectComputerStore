from django.views import generic
from .models import Computer
from django.shortcuts import render


def IndexView(request):
    computer = Computer.objects.all()
    return render(request, "computer/index.html", {"computer":computer})
    
# class ComputerCreate(CreateView):
#    model = Computer
#    fields = ['name', 'brand', 'price', 'speed', 'computer_image']

# class DetailView(generic.DetailView):
#    model = Computer
#    template_name = 'computer/details.html'