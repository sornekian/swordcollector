from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Swordsmith, Warrior
from .forms import SwordForm

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html') 

def swordsmiths_index(request):
    swordsmiths = Swordsmith.objects.all()
    return render(request, 'swordsmiths/index.html', {
        'swordsmiths': swordsmiths
    })

def swordsmiths_detail(request, swordsmith_id):
    swordsmith = Swordsmith.objects.get(id=swordsmith_id)
    id_list = swordsmith.warriors.all().values_list('id')
    warriors_swordsmith_doesnt_have = Warrior.objects.exclude(id__in=id_list)
    sword_form = SwordForm()
    return render(request, 'swordsmiths/detail.html', { 
        'swordsmith': swordsmith, 'sword_form': sword_form, 'warriors': warriors_swordsmith_doesnt_have
    })

def add_sword(request, swordsmith_id):
    form = SwordForm(request.POST)
    if form.is_valid():
        new_sword = form.save(commit=False)
        new_sword.swordsmith_id = swordsmith_id
        new_sword.save()
    return redirect('detail', swordsmith_id=swordsmith_id)   

class SwordsmithCreate(CreateView):
    model = Swordsmith
    fields = '__all__'
    # success_url = '/swords'

class SwordsmithUpdate(UpdateView):
    model = Swordsmith
    fields = '__all__'
    # success_url = '/swords'

class SwordsmithDelete(DeleteView):
    model = Swordsmith
    success_url = '/swordssmiths'   

class WarriorList(ListView):
  model = Warrior

class WarriorDetail(DetailView):
  model = Warrior

class WarriorCreate(CreateView):
  model = Warrior
  fields = '__all__'

class WarriorUpdate(UpdateView):
  model = Warrior
  fields = '__all__'

class WarriorDelete(DeleteView):
  model = Warrior
  success_url = '/warriors'

def assoc_warrior(request, swordsmith_id, warrior_id):
  Swordsmith.objects.get(id=swordsmith_id).warriors.add(warrior_id)
  return redirect('detail', swordsmith_id=swordsmith_id)

def disassoc_warrior(request, swordsmith_id, warrior_id):
  Swordsmith.objects.get(id=swordsmith_id).warriors.remove(warrior_id)
  return redirect('detail', swordsmith_id=swordsmith_id)