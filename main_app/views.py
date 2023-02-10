from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Swordsmith, Warrior
from .forms import SwordForm

# Create your views here.
def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html') 

@login_required
def swordsmiths_index(request):
    swordsmiths = Swordsmith.objects.filter(user=request.user)
    return render(request, 'swordsmiths/index.html', {
        'swordsmiths': swordsmiths
    })

@login_required
def swordsmiths_detail(request, swordsmith_id):
    swordsmith = Swordsmith.objects.get(id=swordsmith_id)
    id_list = swordsmith.warriors.all().values_list('id')
    warriors_swordsmith_doesnt_have = Warrior.objects.exclude(id__in=id_list)
    sword_form = SwordForm()
    return render(request, 'swordsmiths/detail.html', { 
        'swordsmith': swordsmith, 'sword_form': sword_form, 'warriors': warriors_swordsmith_doesnt_have
    })

@login_required
def add_sword(request, swordsmith_id):
    form = SwordForm(request.POST)
    if form.is_valid():
        new_sword = form.save(commit=False)
        new_sword.swordsmith_id = swordsmith_id
        new_sword.save()
    return redirect('detail', swordsmith_id=swordsmith_id)   

class SwordsmithCreate(LoginRequiredMixin, CreateView):
    model = Swordsmith
    fields = ['name', 'origin']
    # success_url = '/swordsmiths'
    def form_valid(self, form):
      return super().form_valid(form)

class SwordsmithUpdate(LoginRequiredMixin, UpdateView):
    model = Swordsmith
    fields = ['name', 'origin']
    # success_url = '/swordsmiths'

class SwordsmithDelete(LoginRequiredMixin, DeleteView):
    model = Swordsmith
    success_url = '/swordssmiths'   

class WarriorList(LoginRequiredMixin, ListView):
  model = Warrior

class WarriorDetail(LoginRequiredMixin, DetailView):
  model = Warrior

class WarriorCreate(LoginRequiredMixin, CreateView):
  model = Warrior
  fields = '__all__'

class WarriorUpdate(LoginRequiredMixin, UpdateView):
  model = Warrior
  fields = '__all__'

class WarriorDelete(LoginRequiredMixin, DeleteView):
  model = Warrior
  success_url = '/warriors'

@login_required
def assoc_warrior(request, swordsmith_id, warrior_id):
  Swordsmith.objects.get(id=swordsmith_id).warriors.add(warrior_id)
  return redirect('detail', swordsmith_id=swordsmith_id)

@login_required
def disassoc_warrior(request, swordsmith_id, warrior_id):
  Swordsmith.objects.get(id=swordsmith_id).warriors.remove(warrior_id)
  return redirect('detail', swordsmith_id=swordsmith_id)