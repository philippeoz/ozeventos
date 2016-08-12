from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.views.decorators.csrf import csrf_exempt
from .forms import CadastroForm, CadastroEvento
from django.contrib.auth import logout
from django.shortcuts import redirect

from .models import Evento

# Método para a página index
def index(request):
    return render(request, 'ozapp/index.html', {}) # Abre o template index.html

# @login_required
# Método para a Home page 
def home(request):
    return render(request, 'ozapp/home.html', {}) # Abre o template home.html

# Método para o Cadastro de Uuário
def cadastrar(request):
    if request.method == 'POST':
    	form = CadastroForm(request.POST) # Instancia do Formulário de Cadastro de Usuário na variável form.

    	if form.is_valid(): # Verifica a validade do formulário instanciado anteriormente
    		form.save() # Salva os dados do Cadastro
    		return HttpResponseRedirect("/login/") # Redireciona para o login caso o cadastro seja bem sucedido
    	else:
    		return render(request, "ozapp/cadastrar.html", {"form":form}) # Retorna para o cadstro de usuário, pois deu erro

    return render(request, "ozapp/cadastrar.html", {"form":CadastroForm()})

# Método para o cadastro de um Evento
@login_required(login_url='/login/')
def cadastrar_evento(request):
    if request.method == 'POST':
    	form = CadastroEvento(request.POST) # Instancia do Formulário de Cadastro de Evento na variavel form.

    	if form.is_valid(): # Verifica a validade do formulário
    		form.save() # Salva os dados do Cadastro
    		return HttpResponseRedirect("/home/") # Redireciona para a página inicial do Sistema, pois o cadastro do evento foi bem sucedido
    	else:
    		return render(request, "ozapp/cadastrarevento.html", {"form":form}) # Volta para o cadastro do Evento, pois deu erro

    return render(request, "ozapp/cadastrarevento.html", {"form":CadastroEvento()})

# Método para o login de usuário no Sistema
@csrf_exempt
def logar(request):
	if request.method == 'POST':
		form = AuthenticationForm(data=request.POST) # Instancia do Formulário de Autenticaçao de Usuário na variável form.
		# form.fields['username'].widget.attrs['class'] = "form-signin"
		# form.fields['password'].widget.attrs['class'] = "form-signin"

		if form.is_valid(): # Verifica a validade do Formulário
			login(request, form.get_user()) # Realiza o login no Sistema
			# return HttpResponseRedirect("/")
			return render(request, 'ozapp/user_page.html', {}) # Retorna para a página inicial do usuário pois o login foi bem sucedido 
		else:
			return render(request, "ozapp/login.html", {"form": form}) # Volta para a página de login pois ocorreu erro do mesmo 
	
	return render(request, 'ozapp/login.html', {"form":AuthenticationForm()})
# return render_to_response("home_page.html", context_instance=RequestContext(request))
def logout_view(request):
    logout(request)
    return render(request, 'ozapp/login.html', {})



# Método para a página de Inscrição em Eventos
@login_required(login_url='/login/')
def incricao_evento(request):
    return render(request, 'ozapp/incricao_evento.html', {}) # Abre o template incricao_evento.html

def buscar_evento(request):
    """
    Função que realiza busca de evento de acordo com o qe foi digitado no campo de busca,
    """
    if request.method == 'GET':
        var_busca = request.GET.get('search_box')
        if var_busca is not None and var_busca is not "":
            eventos = Evento.objects.filter(nome__icontains=var_busca).order_by('nome')
        else:
            eventos = Evento.objects.all().order_by('nome')

        return render(request, 'ozapp/lista_eventos.html',{'eventos':eventos})

    return home()
