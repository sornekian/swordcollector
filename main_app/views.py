from django.shortcuts import render

swords = [
    {'name': '', 'category': 'Katana', 'age': 'Mid-Late 14th century', 'origin': 'Bizen Province', 'swordsmith': 'Yoshikage', 'blade_material': 'Tamahagane Carbon Steel', 'blade_length': '29.7"'},
    {'name': '', 'category': 'Tachi', 'age': 'Early-Mid 14th century', 'origin': 'Bizen Province', 'swordsmith': 'Osafune Hidemitsu', 'blade_material': 'Tamahagane Carbon Steel', 'blade_length': '25.6"'},
    {'name': '', 'category': 'Wakizashi', 'age': 'Late 13th-Early 14th century', 'origin': 'Higo Province', 'swordsmith': 'Enjyu Kunisuke', 'blade_material': 'Tamahagane Carbon Steel', 'blade_length': '13.07"'},
]

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html') 

def swords_index(request):
    return render(request, 'swords/index.html', {
        'swords': swords
    })
