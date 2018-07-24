from django.views import generic
from .models import Computer
from django.views.generic.edit import CreateView
class IndexView(generic.ListView):
    template_name = 'computer/index.html'

    def get_queryset(self):
        return Computer.objects.all()

class ComputerCreate(CreateView):
    model = Computer
    fields = ['name', 'brand', 'price', 'speed', 'computer_image']

class DetailView(generic.DetailView):
    model = Computer
    template_name = 'computer/details.html'