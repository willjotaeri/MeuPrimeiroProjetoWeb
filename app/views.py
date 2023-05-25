from django.shortcuts import render
from app.forms import LoginForm
from app.models import User
from app.models import Solicitado
from django.contrib.auth.decorators import login_required


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            valor_atribut = User.objects.get(name=username, password=password)
            atribut = valor_atribut.atribut
            valor_unid = User.objects.get(name=username, password=password)
            unid = valor_unid.unid
            valor_serv = User.objects.get(name=username, password=password)
            serv = valor_serv.serv
            return home(request, username, atribut, unid, serv)
   
    else:
        form = LoginForm()
    
    return render(request, 'app/login.html', {'form': form})

def solicitado(request):
    registros = Solicitado.objects.all()
    return render(request, 'app/solicitado_list.html', {'registros': registros})
    
def home(request, username, atribut, unid, serv):
    if atribut == "solicitante":
        return render(request, 'app/home_solicitante.html', {'username': username, 'atribut': atribut, 'unid': unid, 'serv': serv})
    else:
        pass

def solicitado_solicitante_list(request):
    unid = request.GET.get('unid')
    registros_solicitante = Solicitado.objects.filter(unidade_solicitante=unid)
    return render(request, 'app/solicitado_solicitante_list.html', {'registros_solicitante': registros_solicitante})