from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Sword

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html') 

def swords_index(request):
    swords = Sword.objects.all()
    return render(request, 'swords/index.html', {
        'swords': swords
    })

def swords_detail(request, sword_id):
    sword = Sword.objects.get(id=sword_id)
    return render(request, 'swords/detail.html', { 'sword': sword })

class SwordCreate(CreateView):
    model = Sword
    fields = '__all__'
    # success_url = '/swords'

class SwordUpdate(UpdateView):
    model = Sword
    fields = '__all__'
    # success_url = '/swords'

class SwordDelete(DeleteView):
    model = Sword
    success_url = '/swords'    